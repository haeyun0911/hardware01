#include <Servo.h>

Servo myservo;

const int buttonPin = 2; // 스위치 핀
int buttonState = HIGH;  // 스위치 상태 (풀업 사용 시 HIGH가 기본값)

void setup() {
  myservo.attach(6);          // 서보모터 핀 (6번 핀)
  pinMode(buttonPin, INPUT_PULLUP); // 내부 풀업 저항 사용
  Serial.begin(9600);         // 시리얼 통신 시작
}

void loop() {
  buttonState = digitalRead(buttonPin);

  if (buttonState == LOW) {   // 스위치를 누르면 동작 (풀업이므로 LOW가 눌림)
    for (int i = 0; i < 2; i++) {  // 10번 반복
      // 0도 -> 180도
      for (int pos = 0; pos <= 180; pos += 1) {
        myservo.write(pos);
        delay(15);
      }
      // 180도 -> 0도
      for (int pos = 180; pos >= 0; pos -= 1) {
        myservo.write(pos);
        delay(15);
      }
    }

    Serial.println("forward"); // 동작 끝나면 전진 명령 전송

    // 스위치를 계속 누르고 있어도 한 번만 동작하도록 대기
    while (digitalRead(buttonPin) == LOW) {
      delay(10);
    }
  }
}
