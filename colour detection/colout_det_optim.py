import cv2
import numpy as np
colour_ranges = {"RED":[[140, 85, 110], [348, 255, 255]],
          "BLUE" : [[94, 80, 2], [126, 255, 255]],
          "GREEN" : [[50, 52, 50], [85, 255, 260]],
          "YELLOW" : [[15, 40, 50], [40, 255, 255]],
          "ORANGE" : [[10, 100, 20], [25, 255, 255]]}
def colour_det(colour_in):
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
        contours, heirarchy = cv2.findContours(colour_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) != 0:
            for contour in contours:
                if cv2.contourArea(contour) > 500:
                    x, y, w, h = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
        cv2.imshow("detected circles", frame)
        cv2.imshow("Frame", frame)
        cv2.imshow("colour mask", colour)
        if key == 27:
            break
print("Which colour do you want to display?")
colour = input("1 = red \n2:blue\n3: green\n4:yellow\n5:all but white\n")
colour = colour.upper()
keys = list(colour_ranges.keys())
if colour in keys:
    colour_det(colour)
else:
    print("enter a valid colour")
