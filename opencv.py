import cv2
import numpy as np
key = 0
cap = cv2.VideoCapture(1)
print("Which colour do you want to display?")
colour = int(input("1 = red \n2:blue\n3: green\n4:yellow\n5:orange\n6:all but white"))
if(colour == 1):
    while True:
        _, frame = cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #red
        low_red = np.array([130, 85, 79])
        high_red = np.array([200, 255, 255])
        red_mask = cv2.inRange(hsv_frame, low_red, high_red)
        red = cv2.bitwise_and(frame, frame, mask = red_mask)
        cv2.imshow("Frame", frame)
        cv2.imshow("Red mask", red)
        if key == 27:
            break
        break
elif colour == 2:
    while True:
        _, frame = cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #blue
        low_blue = np.array([94, 80, 2])
        high_blue = np.array([126, 255, 255])
        blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
        blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
        cv2.imshow("Frame", frame)
        cv2.imshow("Blue mask", blue)
        if key == 27:
            break
        break
elif colour == 3:
    while True:
        _, frame = cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # green
        low_green = np.array([50, 52, 50])
        high_green = np.array([102, 255, 255])
        green_mask = cv2.inRange(hsv_frame, low_green, high_green)
        green = cv2.bitwise_and(frame, frame, mask=green_mask)
        cv2.imshow("Frame", frame)
        cv2.imshow("green mask", green)
        if key == 27:
            break
        break
        #yellow
elif  colour == 4:
    while True:
        _, frame = cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        low_yellow = np.array([20, 52, 72])
        high_yellow = np.array([39, 255, 255])
        yellow_mask = cv2.inRange(hsv_frame, low_yellow, high_yellow)
        yellow = cv2.bitwise_and(frame, frame, mask=yellow_mask)
        cv2.imshow("Frame", frame)
        cv2.imshow("yellow mask", yellow)
        if key == 27:
            break
        break
        # orange
elif colour == 5:
    while True:
        _, frame = cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        low_orange = np.array([10, 70, 72])
        high_orange = np.array([18, 255, 255])
        orange_mask = cv2.inRange(hsv_frame, low_orange, high_orange)
        orange = cv2.bitwise_and(frame, frame, mask=orange_mask)
        cv2.imshow("Frame", frame)
        cv2.imshow("orange mask", orange)
        key = cv2.waitKey(1)
        if key == 27:
            break
        break
elif colour == 6:
    while True:
        _, frame = cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #all but white
        low= np.array([0, 42, 0])
        high = np.array([255, 255, 255])
        mask = cv2.inRange(hsv_frame, low, high)
        mask = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow("Frame", frame)
        cv2.imshow("white mask", mask)
        if key == 27:
            break
        break