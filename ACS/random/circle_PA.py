import cv2
import numpy as np

cap = cv2.VideoCapture(1)

colour_ranges = {"RED": [[170, 85, 110], [180, 255, 255], [0, 85, 110], [7, 255, 255]],
                 "BLUE": [[94, 80, 2], [126, 255, 255], [0, 0, 0], [0, 0, 0]],
                 "PURPLE": [[129, 80, 10], [150, 255, 255], [0, 0, 0], [0, 0, 0]],
                 "YELLOW": [[15, 40, 50], [40, 255, 255], [0, 0, 0], [0, 0, 0]],
                 "ORANGE": [[10, 100, 20], [25, 255, 255], [0, 0, 0], [0, 0, 0]]}


def grid(col):
    color = colour_ranges[col]
    low_coul_1 = np.array(color[0])
    high_coul_1 = np.array(color[1])
    low_coul_2 = np.array(color[2])
    high_coul_2 = np.array(color[3])
    while True:
        key = cv2.waitKey(1)
        _, frame = cap.read()

        HSV_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        coul_mask_1 = cv2.inRange(HSV_frame, low_coul_1, high_coul_1)
        coul_mask_2 = cv2.inRange(HSV_frame, low_coul_2, high_coul_2)

        full_coul_mask = coul_mask_2 + coul_mask_1
        kernel = np.ones((10, 10), np.uint8)
        full_coul_mask = cv2.erode(full_coul_mask, kernel)
        full_coul_mask = cv2.medianBlur(full_coul_mask, 3)
        frame_gaussian = cv2.GaussianBlur(full_coul_mask, (5, 5), 2, 2)
        circles = cv2.HoughCircles(frame_gaussian, cv2.HOUGH_GRADIENT, 1, frame_gaussian.shape[0] / 8, param1=100, param2=18, minRadius=10, maxRadius=50)
        output_frame = cv2.bitwise_and(frame, frame, mask=full_coul_mask)
        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            cv2.circle(frame, center=(circles[0, 0], circles[0, 1]), radius=circles[0, 2], color=(0, 0, 0), thickness=2)
            cv2.putText(output_frame, 'Diameter : ' + str(2 * circles[0, 2]), (0, 20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        cv2.imshow("Frame", frame)
        #cv2.imshow("Output", output_frame)
        if key == 27:
            break


print('1. Red \n2. Blue \n3. Purple \n4. Yellow \n5. Orange')
ch = int(input('Enter : '))
keys = list(colour_ranges.keys())
grid(keys[ch - 1])
