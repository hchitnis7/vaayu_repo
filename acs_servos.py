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
    move_servo(0,0)
    while True:
        ch = int(input("1 for roll \n2 for pitch up\n3 for pitch down\n"))
        if ch == 1:
            roll()
        if ch == 2:
            pitchup()
        if ch == 3:
            pitchdown()

def roll():
    move_servo(0,0)
    angle1 = int(input("Enter the angle: "))
    if angle1-90<0:
        move_servo(angle1, 90 - angle1)
    else:
        move_servo(angle1, angle1-90)




def pitchup():
    move_servo(0,0)
    angle1 = int(input("Enter the angle: "))
    move_servo(angle1, angle1)
def pitchdown():
    move_servo(0,0)
    angle1 = int(input("Enter the angle: "))
    move_servo(90-angle1,90 - angle1)


main()

