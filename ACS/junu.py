# import time
# import math

import cv2
import numpy as np
import time
import math
from threading import Thread

check = True
colour_ranges = {"RED": [[140, 85, 110], [348, 255, 255]],
                 "BLUE": [[94, 80, 2], [126, 255, 255]],
                 "GREEN": [[50, 52, 50], [85, 255, 260]],
                 "YELLOW": [[15, 40, 50], [40, 255, 255]],
                 "ORANGE": [[10, 100, 20], [25, 255, 255]]}


def colour_det(colour_in):
    global check
    cap = cv2.VideoCapture(1)
    coul_name = colour_ranges[colour_in]
    low_bound = np.array(coul_name[0])
    high_bound = np.array(coul_name[1])
    while True:
        key = cv2.waitKey(1)
        _, frame = cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        colour_mask = cv2.inRange(hsv_frame, low_bound, high_bound)
        colour = cv2.bitwise_and(frame, frame, mask=colour_mask)
        hsv_frame = cv2.medianBlur(hsv_frame, 3)
        frame_lab = cv2.inRange(hsv_frame, low_bound, high_bound)
        frame_gaussian = cv2.GaussianBlur(frame_lab, (5, 5), 2, 2)
        circles = cv2.HoughCircles(frame_gaussian, cv2.HOUGH_GRADIENT, 1, frame_gaussian.shape[0] / 8, param1=100, param2=18, minRadius=10, maxRadius=100)
        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            for i in circles:
                cv2.circle(frame, center=(circles[0, 0], circles[0, 1]), radius=circles[0, 2], color=(0, 0, 0), thickness=2)
                cv2.putText(frame, 'Diameter : ' + str(2 * circles[0, 2]), (0, 20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
                check = False

        cv2.imshow("detected circles", frame)

        cv2.imshow("detected circles", frame)
        cv2.imshow("Frame", frame)
        cv2.imshow("colour mask", colour)
        if key == 27:
            break
    return


""" print("Which colour do you want to display?")
colour = input("1 = red \n2:blue\n3: green\n4:yellow\n5:all but white\n")
colour = colour.upper()
keys = list(colour_ranges.keys())
if colour in keys:
    colour_det(colour)
else:
    print("enter a valid colour") """


def calc():

    count = 0
    timee = 0
    avg_speed = 0
    history_avg_salary = []
    total_speed = 0

    while (check):
        print(check)
        print('Speed : ', speed[count])
        time.sleep(1)
        timee += 1
        history_avg_salary.append(avg_speed)
        total_speed += speed[count]
        avg_speed = total_speed / timee
        count += 1
        if count == len(speed):
            print('Avg Speed :', avg_speed)
            break

    if avg_speed - math.floor(avg_speed) < 0.5:
        avg_speed = math.floor(avg_speed)
    else:
        avg_speed = math.ceil(avg_speed)

    print('New Avg Speed', avg_speed)
    distance = avg_speed * timee
    print('Distance is :', distance)


speed = [12, 13, 12, 14, 15, 15, 15, 14, 13, 12, 14, 13, 11, 13, 12, 13, 12, 14, 15, 15, 15, 14, 13, 12, 14, 13, 11, 13,
         12, 13, 12, 14, 15, 15, 15, 14, 13, 12, 14, 12, 13, 12, 14, 15, 15, 15, 14, 13, 12, 14, 13, 11, 13, 12, 13, 12,
         14, 15, 15, 15, 14, 13, 12, 14, 13, 11, 13, 12, 13, 12, 14, 15, 15, 15, 14, 13, 12, 14, 13, 11, 13, 13, 11, 13]
# avg_speed,timee = calc()
# if avg_speed - math.floor(avg_speed) < 0.5:
#     avg_speed = math.floor(avg_speed)
# else:
#     avg_speed = math.ceil(avg_speed)
# print('New Avg Speed',avg_speed)
# distance = avg_speed * timee
# print('Distance is :',distance)
a = Thread(target=colour_det, args=('RED',))
b = Thread(target=calc)
a1 = a.start()
b1 = b.start()
