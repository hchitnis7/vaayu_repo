""" servo pyfirmata"""
import pyfirmata
def move_servo(angle1, angle2):
    pin9.write(angle1)
    pin10.write(angle2)


def main():
    global pin9
    global pin10

    board = pyfirmata.Arduino('COM5')
    iter8 = pyfirmata.util.Iterator(board)
    iter8.start()
    pin10 = board.get_pin('d:10:s')
    move_servo(0,180)