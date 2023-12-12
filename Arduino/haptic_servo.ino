#include <Servo.h>

Servo myservo;

void setup() {
  // put your setup code here, to run once:
  myservo.attach(3);
  Serial.begin(9600);

}

void loop() {

  /////////////숫자를 입력하면 그 값이 delay에 걸려 속도로 인식 (ex 20입력시 보다 5 입력시 빠르게 작동, 현재 움직임 0~120도 한번 왕복하게 되어있음)
  while (Serial.available()) {  // checks if data is available to read
    String speedString = Serial.readStringUntil('\n');  // reads the incoming string until a newline
    int speed = speedString.toInt();  // converts the string to an integer
    //put your main code here, to run repeatedly:
    for(int i=0;i<120;i++){
      myservo.write(i);
      delay(speed);
    }
    for(int i=120;i>0;i--){
      myservo.write(i);
      delay(speed);
    }
    
  }
  
  
  


}

/////////////////// 입력한 숫자 각도로 이동 //////////////// 90도가 손가락과 평행할 때로 맞춰놈
// void serialEvent() {
//   while (Serial.available()) {
//     if (Serial.available()) {  // checks if data is available to read
//     String posString = Serial.readStringUntil('\n');
//     int pos = posString.toInt();
//     Serial.println(pos);
//     if (pos >= 0 && pos <= 180) { // checks if number is in the range of servo movement
//       myservo.write(pos);  // tells servo to go to the position in degrees
//     }
//     Serial.println(pos);
//   }
//   }
// }
