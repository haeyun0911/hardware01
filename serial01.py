import serial
import time
import turtle

s=turtle.getscreen()
t=turtle.Turtle()

t.shape("turtle")

t.speed(1)

connection= None
current_distance=0

def connect_sensor(port='COM3'):
    global connection
    try:
        connection=serial.Serial(port,9600)
        time.sleep(2)
        print("연결 성공")
        return True
    except:
        print("연결 실패")
        return False
    
def read_distance():
    global connection, current_distance
    if connection and connection.in_waiting>0:
        data = connection.readline().decode().strip()
        try:
            distance = float(data)
            current_distance = distance
            return distance
        except:
            pass
        
    return None

def main():
    if connect_sensor():
        while True:
            dist = read_distance()
            if dist:
                print(f"거리: {dist}cm")
                if dist >= 30:
                    t.fd(1)
                else:
                    pass
            time.sleep(0.5)
            
if __name__ == "__main__":
    main()

