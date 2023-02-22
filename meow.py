import cv2
import numpy as np
# Load the cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# initialize face count to 0
total_face_count = 0
#global meow
# Open the webcam
video_capture = cv2.VideoCapture(1)
global c
meow = 0
while True:
    # Read a frame from the webcam
    _, frame = video_capture.read()
    l_bound = [0, 255, 0]

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

    # Draw a rectangle around the faces
    flag = False
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2
        flag = True
    if flag == True:
        meow+=1
        print(meow)
    # Show the frame and the number of faces detected
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = f'{len(faces)} faces detected'
    c = int(len(faces))
    #print(c)
    #meow = 0

    cv2.putText(frame, text, (10, 50), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # counting
    num_faces = len(faces)
    total_face_count += c


    cv2.putText(frame, f'Total number of faces: {total_face_count}', (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow('Webcam', frame)
    # Check if the user pressed the 'q' key
    flag = False
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam
video_capture.release()
cv2.destroyAllWindows()