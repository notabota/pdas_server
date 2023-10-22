# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# import collections
#
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
# cap = cv2.VideoCapture(0)
#
#
# while True:
#     ret, frame = cap.read()
#     eyes = eye_cascade.detectMultiScale(frame)
#
#     ex1, ey1, ew1, eh1 = eyes[0]
#
#     ret, frame = cap.read()
#     if ret is False:
#         break
#
#
#     cv2.rectangle(frame, (ex1, ey1), (ex1 + ew1, ey1 + eh1), (0, 255, 0), 2)
#     cv2.imshow("frame",frame)
#     roi = frame[ey1: (ey1 + eh1), ex1: (ex1 + ew1)]
#     rows, cols, _ = roi.shape
#     gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
#     gray_roi = cv2.GaussianBlur(gray_roi, (7, 7), 0)
#
#     _, threshold = cv2.threshold(gray_roi, 70, 255, cv2.THRESH_BINARY_INV)
#     contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
#
#     for cnt in contours:
#         (x, y, w, h) = cv2.boundingRect(cnt)
#
#         cv2.rectangle(roi, (x, y), (x + w, y + h), (8, 0, 0), 2)
#         cv2.line(roi, (x + int(w/2), 0), (x + int(w/2), rows), (0, 255, 0), 2)
#         cv2.line(roi, (0, y + int(h/2)), (cols, y + int(h/2)), (0, 255, 0), 2)
#         cv2.circle(roi, (x + int(w/2),y + int(h/2) ), 1, (0, 0, 255), 2)
#         break
#
#
#     cv2.imshow("Threshold", threshold)
#     cv2.imshow("gray roi", gray_roi)
#     cv2.imshow("Roi", roi)
#     key = cv2.waitKey(30)
#     if key == 27:
#         break
#
# plt.plot(list_y,list_x)
# plt.show()
# while True:
#     ret, frame = cap.read()
#     if ret is False:
#         break
#
#     roi = frame[650: 850, 400: 600]
#
#     key = cv2.waitKey(10)
#     if key == 27:
#         break
#     for x,y in list:
#         print(x,y)
#         cv2.circle(roi, (x,y), 1, (0, 0, 255), 1)
#     cv2.imshow("dots", roi)
#
# cv2.destroyAllWindows()

import numpy as np
import cv2

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow('img', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()