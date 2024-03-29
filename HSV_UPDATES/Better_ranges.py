import cv2
import numpy as np

cap = cv2.VideoCapture(1)
print("Which colour do you want to display?")
colour = int(input("1 = red \n2:blue\n3: violet\n4:yellow\n5:orange \n6:colour mask"))
global full_red
global full_violet
global full_blue
global full_yellow
global full_orange
while True:
    _, frame = cap.read()
    key = cv2.waitKey(1)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #red
    if colour == 1:
        low_red = np.array([170, 85, 110])
        high_red = np.array([180, 255, 255])
        red_mask = cv2.inRange(hsv_frame, low_red, high_red)
        low_red_1 = np.array([0, 85, 110])
        high_red_1 = np.array([9, 255, 255])
        red_mask_2 = cv2.inRange(hsv_frame, low_red_1, high_red_1)
        full_red = red_mask + red_mask_2
        red = cv2.bitwise_and(frame, frame, mask=full_red)
        contours, heirarchy = cv2.findContours(full_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) != 0:
            for contour in contours:
                if cv2.contourArea(contour) > 500:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
        """cv2.imshow("Frame", frame)
        cv2.imshow("Red mask_high range", red)
        low_red_1 = np.array([0, 85, 110])
        high_red_1= np.array([15, 255, 255])
        red_mask_2 = cv2.inRange(hsv_frame, low_red_1, high_red_1)
        red_1 = cv2.bitwise_and(frame, frame, mask=red_mask)
        contours, heirarchy = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) != 0:
            for contour in contours:
                if cv2.contourArea(contour) > 500:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)"""
        cv2.imshow("Frame", frame)
        """cv2.imshow("Red mask_low range", red_1)"""
        cv2.imshow("Red mask_high range", red)

    elif colour == 2:
        # blue
        low_blue =  np.array([94, 80, 2])
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
        full_blue = blue_mask
        cv2.imshow("Blue mask", blue)
    elif colour == 3:
        # violet
        low_violet = np.array([130, 40, 60])
        high_violet = np.array([140, 255, 255])
        violet_mask = cv2.inRange(hsv_frame, low_violet, high_violet)
        violet = cv2.bitwise_and(frame, frame, mask=violet_mask)
        contours, heirarchy = cv2.findContours(violet_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) != 0:
            for contour in contours:
                if cv2.contourArea(contour) > 500:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
        cv2.imshow("Frame", frame)
        full_violet = violet_mask
        cv2.imshow("violet mask", violet)
    elif colour == 4:
        # yellow
        low_yellow = np.array([30, 40, 50])
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
        full_yellow = yellow_mask
    elif colour == 5:
        # orange
        low_orange = np.array([7, 90, 305
                               ])
        high_orange = np.array([11, 255, 255])
        orange_mask = cv2.inRange(hsv_frame, low_orange, high_orange)
        orange = cv2.bitwise_and(frame, frame, mask=orange_mask)
        contours, heirarchy = cv2.findContours(orange_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) != 0:
            for contour in contours:
                if cv2.contourArea(contour) > 500:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
        cv2.imshow("Frame", frame)
        full_orange = orange_mask
        cv2.imshow("orange mask", orange)
    else:
        # all but white
        low = np.array([0, 42, 0])
        high = np.array([180, 255, 255])
        mask_col = cv2.inRange(hsv_frame, low, high)
        mask_ = cv2.bitwise_and(frame, frame, mask=mask_col)
        cv2.imshow("Frame", frame)
        #cv2.imshow("white minus", mask_)

    if key == 27:
        break