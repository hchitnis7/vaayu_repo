from pyfirmata import Arduino ,SERVO  #,util
from time import sleep
port = 'COM7'
pin=10
board= Arduino(port)
board.digital[pin].mode=SERVO
def rotateservo(pin,angle):
    board.digital[pin].write(angle)
    sleep(0.015)
k = 0
while True:
    x=input("enter the servo angle")
    rotateservo(pin, x)