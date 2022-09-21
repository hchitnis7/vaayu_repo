import cv2
import numpy as np
colour_ranges = {"RED":[[140, 85, 110], [348, 255, 255]],
          "BLUE" : [[94, 80, 2], [126, 255, 255]],
          "GREEN" : [[50, 52, 50], [85, 255, 260]],
          "YELLOW" : [[15, 40, 50], [40, 255, 255]],
          "ORANGE" : [[10, 100, 20], [25, 255, 255]]}
def colour_det(colour_in):
    radius = 0
    cap = cv2.VideoCapture(1)
    coul_name = colour_ranges[colour_in]
    low_bound = np.array(coul_name[0])
    high_bound = np.array(coul_name[1])
    while True:
        key = cv2.waitKey(1)
        _, frame = cap.read()
        output_frame = frame.copy()
        HSV_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        HSV_frame = cv2.medianBlur(HSV_frame, 3)
        frame_lab = cv2.inRange(HSV_frame, low_bound, high_bound)
        frame_gaussian = cv2.GaussianBlur(frame_lab, (5, 5), 2, 2)
        #circles = cv2.HoughCircles(frame_gaussian, cv2.HOUGH_GRADIENT, 1, frame_gaussian.shape[0] / 8, param1=100, param2=18, minRadius=10, maxRadius=100)
        circles = cv2.HoughCircles(frame_gaussian, cv2.HOUGH_GRADIENT, 1, 30 , param1=80, param2=53, minRadius=0, maxRadius=0)

        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            cv2.circle(output_frame, center=(circles[0, 0], circles[0, 1]), radius=circles[0, 2], color=(0, 0, 0), thickness=2)
            cv2.putText(output_frame, 'Diameter : ' + str(2 * circles[0, 2]), (0, 20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

        cv2.imshow("detected circles", output_frame)
        cv2.imshow("Frame", frame)
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
