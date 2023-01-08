""" servo pyfirmata"""
import pyfirmata
def move_servo(angle1, angle2):
    pin9.write(angle1)
    pin10.write(angle2)


def main():
    global pin9
    global pin10

    board = pyfirmata.Arduino('COM7')

    iter8 = pyfirmata.util.Iterator(board)
    iter8.start()

    pin9 = board.get_pin('d:9:s')
    pin10 = board.get_pin('d:10:s')
    move_servo(90,90)
    while True:
        ch = int(input("1 for roll \n2 for pitch up\n3 for pitch down\n4 exit"))
        if ch == 1:
            roll()
        if ch == 2:
            pitchup()
        if ch == 3:
            pitchdown()
        if ch == 4:
            move_servo(90, 90)
            exit()

def roll():

    move_servo(90, 90)
    angle1 = int(input("Enter the angle(-45, 45): "))
    if angle1<0:
        move_servo(90 + angle1, 180 + angle1)
        move_servo(90, 90)
    else:
        move_servo(180 - angle1, 90 - angle1)


def pitchup():
    move_servo(90, 90)
    angle1 = int(input("Enter the angle(0-45): "))
    move_servo(90- angle1, 90 - angle1)



def pitchdown():
    move_servo(90, 90)
    angle1 = int(input("Enter the angle(0, 45): "))
    move_servo(90 + angle1,  90 + angle1)

main()