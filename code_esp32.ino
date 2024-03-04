#include <PubSubClient.h>
#include <WiFi.h>  

const char *ssid = "hani";      // Replace with  WiFi SSID
const char *password = "azertyazerty";  // Replace with  WiFi password
const char *mqtt_server = "192.168.43.238";  // Replace with  MQTT broker IP address

const int buttonPin = 4;
const int ledPin = 23;
const int ledPinv = 5;
const int capteurPin = 33;   // analog pin A0
const int capteurPin2 = 22;  //  analog pin A3

int buttonState;
int seuilValeur = 1200;
unsigned long lastMillis = 0;
const long interval = 1000;  // publish MQTT message (in milliseconds)

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  Serial.begin(115200);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  // Set up MQTT
  client.setServer(mqtt_server, 1883);

  // Initialize the LED pins as outputs
  pinMode(ledPin, OUTPUT);
  pinMode(ledPinv, OUTPUT);

  // Initialize the pushbutton pin as an input
  pinMode(buttonPin, INPUT_PULLUP);
}

void loop() {
  unsigned long currentMillis = millis();

  // Connect to MQTT broker if not connected
  if (!client.connected()) {
    reconnect();
  }

  // Read the state of the pushbutton value
  buttonState = digitalRead(buttonPin);

  // Read sensor values
  int valeurCapteur = analogRead(capteurPin);
  int valeurCapteur2 = analogRead(capteurPin2);

  if (buttonState == HIGH) {
    if (valeurCapteur >= seuilValeur || valeurCapteur2 >= seuilValeur) {
      // Turn LED on
      digitalWrite(ledPinv, LOW);
      digitalWrite(ledPin, HIGH);
    } else {
      // Turn LEDs off
      digitalWrite(ledPin, LOW);
      digitalWrite(ledPinv, HIGH);
    }
  } else {
    // Turn LEDs off
    digitalWrite(ledPin, HIGH);
    digitalWrite(ledPinv, LOW);
  }

  // Publish button state to MQTT 
  if (currentMillis - lastMillis >= interval) {
    publishButtonState();
    lastMillis = currentMillis;
  }

  // Allow the PubSubClient 
  client.loop();
}

void reconnect() {
  // Loop until we're reconnected to the MQTT broker
  while (!client.connected()) {
    Serial.println("Attempting MQTT connection...");
    if (client.connect("arduino-client")) {
      Serial.println("Connected to MQTT broker");
    } else {
      Serial.print("Failed, rc=");
      Serial.print(client.state());
      Serial.println(" Retrying in 5 seconds...");
      delay(5000);
    }
  }
}

void publishButtonState() {
  // Publish button state to the MQTT topic
  String topic = "button_state";
  String message = String(buttonState);
  client.publish(topic.c_str(), message.c_str());
  Serial.println("Button state published to MQTT");
}
