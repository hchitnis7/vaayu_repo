import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    _, frame = cap.read()
    key = cv2.waitKey(1)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_red = np.array([170, 85, 110])
    high_red = np.array([180, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    low_red_1 = np.array([0, 85, 110])
    high_red_1 = np.array([9, 255, 255])
    red_mask_2 = cv2.inRange(hsv_frame, low_red_1, high_red_1)
    full_red = red_mask + red_mask_2
    # blue
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    #blue = cv2.bitwise_and(frame, frame, mask=blue_mask)
    full_blue = blue_mask
    low_green = np.array([49, 30, 45])
    high_green = np.array([85, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)
    full_green = green_mask
    low_yellow = np.array([30, 40, 50])
    high_yellow = np.array([40, 255, 255])
    yellow_mask = cv2.inRange(hsv_frame, low_yellow, high_yellow)
    yellow = cv2.bitwise_and(frame, frame, mask=yellow_mask)
    full_yellow = yellow_mask
    # orange
    low_orange = np.array([9, 90, 90])
    high_orange = np.array([11, 255, 255])
    orange_mask = cv2.inRange(hsv_frame, low_orange, high_orange)
    full_orange = orange_mask
    full_coul = full_orange+full_yellow+full_blue+full_green+full_red
    full_meow = cv2.bitwise_and(frame, frame, mask=full_coul)
    frame_gaussian = cv2.GaussianBlur(full_coul, (5, 5), 2, 2)

    circles = cv2.HoughCircles(frame_gaussian, cv2.HOUGH_GRADIENT, 1, 100, param1=100, param2=30, minRadius=10, maxRadius=100)
    if circles is not None:
        circles = np.uint16(np.around(circles))

        for i in circles:
            cv2.circle(frame, center=(circles[i, 0], circles[i, 1]), radius=circles[i, 2], color=(0, 0, 0),
                           thickness=2)
            cv2.putText(frame, 'Diameter : ' + str(2 * circles[i, 2]), (0, 20), cv2.FONT_HERSHEY_COMPLEX,
                            0.5, (0, 0, 0))
        #cv2.line(frame, (circles[0, 0], circles[0, 1]), (width // 2, height // 2), (0, 255, 0), 3)
    cv2.imshow("sab ka baap", full_meow)
    cv2.imshow("chutiya", frame)

    if key == 27:
        break