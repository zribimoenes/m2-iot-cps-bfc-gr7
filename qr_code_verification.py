import cv2
from pyzbar.pyzbar import decode
import time
import paho.mqtt.publish as publish

# Open the default camera (camera index 0)
cap = cv2.VideoCapture(0)

# MQTT Broker details
mqtt_broker_address = "192.168.137.43"
mqtt_username = "esprit"
mqtt_password = "esprit"
mqtt_topic = "qr_code_topic"

def verify_qr_code(decoded_objects):
    for obj in decoded_objects:
        data = obj.data.decode('utf-8')
        print(f"Detected QR code data: {data}")

        # Publish the detected data to MQTT topic
        publish.single(mqtt_topic, data, hostname=mqtt_broker_address,
                       port=1883, auth={'username': mqtt_username, 'password': mqtt_password})

# ...

try:
    while True:
        print("Please place a QR code in front of the camera.")
        
        # Wait for a QR code to be detected
        while True:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            decoded_objects = decode(gray)

            if decoded_objects:
                break

            cv2.imshow("QR Code Reader", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break

        # Verify the detected QR code and publish to MQTT
        verify_qr_code(decoded_objects)

        # Display the image for 10 seconds
        cv2.imshow("QR Code Reader", frame)
        cv2.waitKey(10000)  # Wait for 10 seconds

finally:
    cv2.destroyAllWindows()
    cap.release()
