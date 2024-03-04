import paho.mqtt.client as mqtt
import json
import mysql.connector
import serial
import time
from threading import Thread
from queue import Queue

# MQTT settings
mqtt_broker = "localhost"
mqtt_port = 1883
mqtt_user = "esprit"
mqtt_password = "esprit"

# MQTT topics
topic1 = "sensor1"
buttonTopic = "buttonState"
qr_code_topic = "qr_code_topic"

# MySQL settings
mysql_host = '192.168.137.94'
mysql_user = 'root'
mysql_password = ''
mysql_database = 'bateau'

# Initialize the record_exists variable
record_exists = False
hauteur = 0  # Initialize hauteur

# Create a Queue for the serial thread result
result_queue = Queue()

# Callback when a message is received from MQTT
def on_message(client, userdata, msg):
    global record_exists, hauteur
    payload = msg.payload.decode("utf-8")

    if msg.topic == topic1 or msg.topic == buttonTopic:
        print(f"Message reçu sur le sujet {msg.topic}: {payload}")

        if msg.topic == buttonTopic and payload == "0" and record_exists and result_queue.get() == 1:
            print("État vérifié")
            record_exists = False
            # Add your logic for the verified state here, e.g., send an MQTT message, etc.

    elif msg.topic == qr_code_topic:
        data = json.loads(payload)
        pass_value = data.get("num_pass", "")
        im_value = data.get("voiture_imma", "")
        nom_value = data.get("Nom", "")
        id_bateau_value = data.get("id_bateau", "")
        v_poid_value = data.get("v_poid", "")

        try:
            connection = mysql.connector.connect(
                host=mysql_host,
                user=mysql_user,
                password=mysql_password,
                database=mysql_database
            )

            if connection.is_connected():
                print('Connected to MySQL database')

                # Check if the voyageur exists
                table_name_voyageur = 'voyageur'
                query_voyageur = f"SELECT * FROM {table_name_voyageur} WHERE num_pass = '{pass_value}' AND voiture_immat = '{im_value}' AND Nom = '{nom_value}'"
                cursor_voyageur = connection.cursor()
                cursor_voyageur.execute(query_voyageur)
                rows_voyageur = cursor_voyageur.fetchall()
                record_exists = bool(rows_voyageur)

                print(f"Pass: {pass_value}, IM: {im_value}, Nom: {nom_value}, id_bateau: {id_bateau_value}, v_poid: {v_poid_value}")

                if record_exists:
                    print("Voyageur exists:")
                    for row_voyageur in rows_voyageur:
                        print(row_voyageur)

                    # Retrieve capacity and hauteur from the bateau table
                    table_name_bateau = 'bateau'
                    query_bateau = f"SELECT capacity, hauteur FROM {table_name_bateau} WHERE id = '{id_bateau_value}'"
                    cursor_bateau = connection.cursor()
                    cursor_bateau.execute(query_bateau)
                    rows_bateau = cursor_bateau.fetchall()

                    if rows_bateau:
                        print("Bateau information:")
                        for row_bateau in rows_bateau:
                            print(row_bateau)
                            capacity, hauteur = row_bateau
                            # Add your logic here using capacity and hauteur
                            # For example, print or use them in further processing

                        # Set the global variable hauteur for use in serial_thread
                       

                else:
                    print("Voyageur does not exist")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            if connection and connection.is_connected():
                cursor_voyageur.close()
                cursor_bateau.close()
                connection.close()
                print('MySQL connection closed')


def find_min_zone(max_weight, weight_to_add):
initial_weights = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    # Initial weights for each zone
    zone_weights = initial_weights.copy()

    while sum(zone_weights.values()) < max_weight:
        # Determine the zone with the least weight
        min_zone = min(zone_weights, key=zone_weights.get)

        # Update the zone weight
        zone_weights[min_zone] += weight_to_add

    return min_zone
    
# MQTT Thread
def mqtt_thread():
    mqtt_client = mqtt.Client()
    mqtt_client.username_pw_set(mqtt_user, mqtt_password)
    mqtt_client.on_message = on_message

    mqtt_client.connect(mqtt_broker, mqtt_port, 60)
    mqtt_client.subscribe(topic1)
    mqtt_client.subscribe(buttonTopic)
    mqtt_client.subscribe(qr_code_topic)

    mqtt_client.loop_forever()

# Serial Thread
def serial_thread(result_queue):
    ser = serial.Serial('/dev/ttyS0', 115200, timeout=1)
    try:
        while True:
            line = ser.readline().decode('utf-8').strip()
            print(line)

            # Assuming line is a numeric value received from the serial port
            try:
                serial_value = float(line)

                # Call the function to get the character
                char_result = find_min_zone()

                # Call the function to find the minimum zone
                resulting_zone = find_min_zone(initial_weights, max_weight, weight_to_add)
                print(f"The zone with the least weight after adding {weight_to_add} is: {resulting_zone}")

                # Send the result via UART
                ser.write(char_result.encode('utf-8'))
                print(f"Result sent via UART: {char_result}")

                if serial_value < hauteur:
                    print(f"Serial value ({serial_value}) is less than hauteur ({hauteur})")
                    result_queue.put(1)  # Put the result in the queue
                else:
                    print(f"Serial value ({serial_value}) is greater than or equal to hauteur ({hauteur})")
                    result_queue.put(0)  # Put the result in the queue

            except ValueError:
                print("Invalid serial value format. Should be a numeric value.")

            time.sleep(0.1)
    except KeyboardInterrupt:
        ser.close()
        print("Serial port closed.")

# Start MQTT thread
mqtt_thread = Thread(target=mqtt_thread)
mqtt_thread.start()

# Start Serial thread
serial_thread = Thread(target=serial_thread, args=(result_queue,))
serial_thread.start()

# Wait for both threads to finish
mqtt_thread.join()
serial_thread.join()
