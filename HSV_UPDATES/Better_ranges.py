import cv2
import numpy as np

cap = cv2.VideoCapture(1)
print("Which colour do you want to display?")
colour = int(input("1 = red \n2:blue\n3: green\n4:yellow\n5:orange \n6:colour mask"))

while True:
    _, frame = cap.read()
    key = cv2.waitKey(0)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #red
    if colour == 1:
        low_red = np.array([170, 85, 110])
        high_red = np.array([180, 255, 255])
        red_mask = cv2.inRange(hsv_frame, low_red, high_red)
        red = cv2.bitwise_and(frame, frame, mask=red_mask)
        contours, heirarchy = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) != 0:
            for contour in contours:
                if cv2.contourArea(contour) > 500:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
        cv2.imshow("Frame", frame)
        cv2.imshow("Red mask", red)
    elif colour == 2:
        # blue
        low_blue = np.array([94, 80, 2])
        high_blue = np.array([126, 255, 255])
        blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
        blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
        contours, heirarchy = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) != 0:
            for contour in contours:
                if cv2.contourArea(contour) > 500:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
        cv2.imshow("Frame", frame)
        cv2.imshow("Blue mask", blue)
    elif colour == 3:
        # green
        low_green = np.array([55, 40, 45])
        high_green = np.array([85, 255, 255])
        green_mask = cv2.inRange(hsv_frame, low_green, high_green)
        green = cv2.bitwise_and(frame, frame, mask=green_mask)
        contours, heirarchy = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) != 0:
            for contour in contours:
                if cv2.contourArea(contour) > 500:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
        cv2.imshow("Frame", frame)
        cv2.imshow("green mask", green)
    elif colour == 4:
        # yellow
        low_yellow = np.array([15, 40, 50])
        high_yellow = np.array([40, 255, 255])
        yellow_mask = cv2.inRange(hsv_frame, low_yellow, high_yellow)
        yellow = cv2.bitwise_and(frame, frame, mask=yellow_mask)
        cv2.imshow("Frame", frame)
        contours, heirarchy = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) != 0:
            for contour in contours:
                if cv2.contourArea(contour) > 500:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
        cv2.imshow("yellow mask", yellow)
    elif colour == 5:
        # orange
        low_orange = np.array([10, 100, 20])
        high_orange = np.array([25, 255, 255])
        orange_mask = cv2.inRange(hsv_frame, low_orange, high_orange)
        orange = cv2.bitwise_and(frame, frame, mask=orange_mask)
        contours, heirarchy = cv2.findContours(orange_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) != 0:
            for contour in contours:
                if cv2.contourArea(contour) > 500:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
        cv2.imshow("Frame", frame)
        cv2.imshow("orange mask", orange)
    else:
        # all but white
        low = np.array([0, 42, 0])
        high = np.array([255, 255, 255])
        mask_col = cv2.inRange(hsv_frame, low, high)
        mask_ = cv2.bitwise_and(frame, frame, mask=mask_col)
        cv2.imshow("Frame", frame)
        cv2.imshow("white minus", mask_)
    if key == 27:
        break