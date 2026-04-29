#include <Servo.h>

Servo myServo;
unsigned long actionStartTime = 0;
const int actionDuration = 500; 
bool isMoving = false;

void setup() {
  Serial.begin(9600);
  myServo.attach(A0); //Servomotor Pin ID
  myServo.write(0);
}

void loop() {
  
  if (Serial.available() > 0 && !isMoving) {
    char command = Serial.read();
    
    int blinks = command - '0'; 
    for(int i = 0; i < blinks; i++) {
      digitalWrite(13, HIGH);
      delay(100);
      digitalWrite(13, LOW);
      delay(100);
    }
    //Values are represents angles
    if (command == '1') myServo.write(45);
    else if (command == '2') myServo.write(90);
    else if (command == '3') myServo.write(135);
    else if (command == '4') myServo.write(180);
    else if (command == '0') myServo.write(0);
    
    while(Serial.available() > 0) Serial.read(); 
  }

}
