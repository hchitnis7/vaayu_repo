import cv2
import numpy
import math
import numpy as np
global slope
global height
global width

cap = cv2.VideoCapture(1)

colour_ranges = {"RED": [[170, 85, 110], [180, 255, 255], [0, 85, 110], [7, 255, 255]],
                 "BLUE": [[94, 80, 2], [126, 255, 255], [0, 0, 0], [0, 0, 0]],
                 "GREEN": [[49, 30, 45], [85, 255, 255], [0, 0, 0], [0, 0, 0]],
                 "YELLOW": [[15, 40, 50], [40, 255, 255], [0, 0, 0], [0, 0, 0]],
                 "ORANGE": [[10, 100, 20], [25, 255, 255], [0, 0, 0], [0, 0, 0]]}


def centre_grid(frame, h, w):
    cv2.line(frame, (3*w // 10, 0), (3*w // 10, h), (120, 0, 0), 3)
    cv2.line(frame, (3*w // 10, 3*h // 10), (w - 3*w // 10, 3*h // 10), (120, 0, 0), 3)
    cv2.line(frame, (w - 3*w // 10, 0), (w - 3*w // 10, h), (120, 0, 0), 3)
    cv2.line(frame, (3*w // 10, h - 3*h // 10), (w - 3*w // 10, h - 3*h // 10), (120, 0, 0), 3)
    """cv2.line(frame, (w + w // 2, h), (w + w // 2, h + h // 2), (120, 0, 0), 3)
    cv2.line(frame, (w, h + h // 2), (w + w // 2, h + h // 2), (120, 0, 0), 3)
    cv2.line(frame, (w + w // 2, h // 2), (w + w // 2, h), (120, 0, 0), 3)
    cv2.line(frame, (w, h // 2), (w + w // 2, h // 2), (120, 0, 0), 3)
    cv2.line(frame, (w // 2, h * 3 // 2), (w // 2, h), (120, 0, 0), 3)
    cv2.line(frame, (w // 2, h + h // 2), (3 * w // 2, h + h // 2), (120, 0, 0), 3)
    cv2.line(frame, (w // 2, h // 2), (w, h // 2), (120, 0, 0), 3)
    cv2.line(frame, (w // 2, h // 2), (w // 2, h), (120, 0, 0), 3)
    cv2.line(frame, (0, height // 2), (width, height // 2), (255, 0, 0), 3)
    cv2.line(frame, (width // 2, 0), (width // 2, height), (255, 0, 0), 3)"""
    return


def show_nav(cir_x, cir_y, width, height):

    if(cir_x >= width - 3*width // 10):
        print("left down right up (MOVE RIGHT)")
    elif(cir_x <= 3*width//10):
        print("left up right down (MOVE LEFT)")
    elif(cir_y >= height - 3*height // 10 and cir_x >= 3*width // 10 and cir_x <= width - 3*width // 10):
        print("Both down (MOVE DOWN)")
    else:
        print("circle aligned or not found")
    return



def showDirection(circle_x, circle_y, x, y):
    if (circle_x == 0 and circle_y == 0):
        print("cicle is aligned")
    elif (circle_x <= x and circle_y <= y):
        print('Circle is in 1st Quadrant')

    elif (circle_x >= x and circle_y <= y):
        print('Cirlce is in 2nd Quadrant')

    elif (circle_x <= x and circle_y >= y):
        print('Circle is in 3rd Quadrant')

    elif (circle_x >= x and circle_y >= y):
        print('Cirlce is in 4th Quadrant')
    else:
        print("error")
    """if(c_y > height - x // 2 and c_y < height + x //2 and c_x > width - y // 2 and c_x < width + y // 2):
        print('circle withibn bounds')"""

"""
cap.set(cv2.CAP_PROP_FRAME_WIDTH, height)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, width)
"""


def grid(col):
    color = colour_ranges[col]
    low_coul_1 = np.array(color[0])
    high_coul_1 = np.array(color[1])
    low_coul_2 = np.array(color[2])
    high_coul_2 = np.array(color[3])
    while True:
        key = cv2.waitKey(1)
        _, frame = cap.read()
        #_, frame_2 = cap.read()
        height = frame.shape[0]
        width = frame.shape[1]
        #centre_grid(frame, height, width)
        """cropped_image_mask = np.zeros(frame.shape[:2], dtype="uint8")
        cv2.rectangle(cropped_image_mask, (w // 2, h // 2), (w + w // 2, h + h // 2), 255, -1)
        new_cropped = cv2.bitwise_and(frame_2, frame_2, mask=cropped_image_mask)
        new_cropped_hsv = cv2.cvtColor(new_cropped, cv2.COLOR_BGR2HSV)"""
        HSV_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        coul_mask_1 = cv2.inRange(HSV_frame, low_coul_1, high_coul_1)
        coul_mask_2 = cv2.inRange(HSV_frame, low_coul_2, high_coul_2)

        full_coul_mask = coul_mask_2 + coul_mask_1
        kernel = np.ones((10, 10), np.uint8)
        full_coul_mask = cv2.erode(full_coul_mask, kernel)
        #cv2.imshow("cropped frame", new_cropped)
        full_coul_mask = cv2.medianBlur(full_coul_mask, 3)
        #frame_lab = cv2.inRange(HSV_frame, lower, upper)
        frame_gaussian = cv2.GaussianBlur(full_coul_mask, (5, 5), 2, 2)
        circles = cv2.HoughCircles(frame_gaussian, cv2.HOUGH_GRADIENT, 1, frame_gaussian.shape[0] / 8, param1=100, param2=18, minRadius=10, maxRadius=50)
        output_frame = cv2.bitwise_and(frame, frame, mask=full_coul_mask)
        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            cv2.circle(frame, center=(circles[0, 0], circles[0, 1]), radius=circles[0, 2], color=(0, 0, 0), thickness=2)
            cv2.line(frame, (circles[0, 0], circles[0, 1]), (width // 2, height // 2), (0, 255, 0), 3)
            showDirection(circles[0, 0], circles[0, 1], width // 2, height // 2)
            show_nav(circles[0, 0], circles[0, 1], width, height)
            #show_inner(circles[0, 0], circles[0, 1], width // 2, height // 2)
            slope = (width // 2 - circles[0, 0]) / (height // 2 - circles[0, 1])
            cv2.putText(output_frame, "theta : " + str(numpy.arctan(slope)), (0, 20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
            print(math.atan(slope)*(180 / math.pi))
        """contours, heirarchy = cv2.findContours(full_coul_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) != 0:
            for contour in contours:
                if cv2.contourArea(contour) > 10:
                    x, y, w, h = cv2.boundingRect(contour)
                    x = x + 10
                    y = y + 10
                    w = w + 10
                    h = h + 10
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    pts1 = np.float32([[x, y], [x + w, y], [x, y + h], [x + w, y + h]])
                    pts2 = np.float32([[0, 0], [250, 0], [0, 250], [250, 250]])
                    M = cv2.getPerspectiveTransform(pts1, pts2)
                    dst = cv2.warpPerspective(HSV_frame, M, (300, 300))
                    DST_BGR = cv2.cvtColor(dst, cv2.COLOR_HSV2BGR)

                    cv2.imshow("", DST_BGR)"""

        cv2.imshow("Frame", frame)
        cv2.imshow("Output", output_frame)
        if key == 27:
            break


# grid()
print('1. Red \n2. Blue \n3. Green \n4. Yellow \n5. Orange')
ch = int(input('Enter : '))
keys = list(colour_ranges.keys())
grid(keys[ch - 1])



"""def draw_leftTop_Grid(frame, height, width):
    h = height // 2
    w = width // 2
    cv2.line(frame, (w // 2, h // 2), (w, h // 2), (120, 0, 0), 3)
    cv2.line(frame, (w // 2, h // 2), (w // 2, h), (120, 0, 0), 3)
    return


def draw_leftDown_Grid(frame, height, width):
    h = height // 2
    w = width // 2
    cv2.line(frame, (w // 2, h*3//2), (w // 2, h ), (120, 0, 0), 3)
    cv2.line(frame, (w // 2, h + h // 2), (3*w // 2, h + h // 2), (120, 0, 0), 3)
    return


def draw_rightTop_Grid(frame, height, width):
    h = height // 2
    w = width // 2
    cv2.line(frame, (w + w // 2, h //2), (w + w // 2, h), (120, 0, 0), 3)
    cv2.line(frame, (w , h // 2), (w + w // 2, h // 2), (120, 0, 0), 3)
    return


def draw_rightDown_Grid(frame, height, width):
    h = height // 2
    w = width // 2
    cv2.line(frame, (w + w // 2, h), (w + w // 2, h + h // 2), (120, 0, 0), 3)
    cv2.line(frame, (w, h + h // 2), (w + w // 2, h + h // 2), (120, 0, 0), 3)
    return

"""
"""draw_leftTop_Grid(frame, height, width)
        draw_leftDown_Grid(frame, height, width)
        draw_rightTop_Grid(frame, height, width)
        draw_rightDown_Grid(frame, height, width)"""