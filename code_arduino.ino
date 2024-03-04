#include "Ultrasonic.h"
#include <Wire.h>
#include "rgb_lcd.h"

#define LEDR 2
#define LEDB 3

Ultrasonic ultrasonic(7);
rgb_lcd lcd;

void setup()
{
  pinMode(LEDR, OUTPUT);
  pinMode(LEDB, OUTPUT);
  Serial.begin(115200);
  lcd.begin(16, 2);
  lcd.print("welcome aboard!");
  delay(1000);
  lcd.clear();  // Clear the LCD once 
}

void loop()
{
  long RangeInInches;
  long RangeInCentimeters;

  digitalWrite(LEDR, HIGH);

  String incomingData = "";  // Initialize an empty string 

  // Read data until a newline character is received
  while (Serial.available() > 0) {
    char incomingChar = Serial.read();
    if (incomingChar == '\n') {
      lcd.clear();
      lcd.print("please wait..");
      break;
    }
    incomingData += incomingChar;
  }

  Serial.print("Incoming Data: ");
  Serial.println(incomingData);

  // Display different zones based on the received data
  if (incomingData == "A") {
    Serial.print("ZONE A");
    lcd.setCursor(0, 0); // Set cursor position
    lcd.print("Zone A");
    digitalWrite(LEDR, LOW);
    digitalWrite(LEDB, HIGH);
  } else if (incomingData == "B") {
    Serial.print("ZONE B");
    lcd.setCursor(0, 0);
    lcd.print("Zone B");
    digitalWrite(LEDR, LOW);
    digitalWrite(LEDB, HIGH);
  } else if (incomingData == "C") {
    Serial.print("ZONE C");
    lcd.setCursor(0, 0);
    lcd.print("Zone C");
    digitalWrite(LEDR, LOW);
    digitalWrite(LEDB, HIGH);
  } else if (incomingData == "D") {
    Serial.print("ZONE D");
    lcd.setCursor(0, 0);
    lcd.print("Zone D");
    digitalWrite(LEDR, LOW);
    digitalWrite(LEDB, HIGH);
  } else if (incomingData == "\n") {
    Serial.print("please wait");
    digitalWrite(LEDR, HIGH);
    digitalWrite(LEDB, LOW);
    lcd.clear();
    lcd.print("please wait");
  } else if (incomingData == "F") {
    Serial.print("stop");
    digitalWrite(LEDR, HIGH);
    digitalWrite(LEDB, LOW);
    lcd.setCursor(0, 0);
    lcd.print("Stop");
  }

  delay(1000); 

  Serial.println("The distance to obstacles in front is: ");
  RangeInInches = ultrasonic.MeasureInInches();
  Serial.print(RangeInInches); // 0~157 inches
  Serial.println(" inch");
  delay(250);

  RangeInCentimeters = ultrasonic.MeasureInCentimeters();
  Serial.print(RangeInCentimeters); // 0~400cm
  Serial.println(" cm");
  delay(250);

  lcd.setCursor(0, 1);
  lcd.print(millis() / 1000);
  delay(100);
}
