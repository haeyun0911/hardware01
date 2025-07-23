import serial
import time
import turtle

s = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")

ser = serial.Serial('COM3', 9600)
time.sleep(2)
print("연결 완료")

def check_serial():
    if ser.in_waiting > 0:
        data = ser.readline().decode().strip()
        if data == "forward":
            t.fd(100)
    s.ontimer(check_serial, 50)  # 50ms 후 다시 호출

check_serial()  # 최초 실행
s.mainloop()    # 터틀 메인 루프 실행
