#include <Servo.h>

Servo servo;
int pinSwitch = 4;
int positionServo = 0;
int state =0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  servo.attach(9);
  pinMode(pinSwitch, INPUT_PULLUP);
}

void loop() {
  positionServo = 0;
  servo.write(positionServo);
  //state = digitalRead(pinSwitch);
  Serial.println(digitalRead(pinSwitch));
  if(digitalRead(pinSwitch) == 0){
    positionServo = 30;
    servo.write(positionServo);
      delay(50);
  }
}
