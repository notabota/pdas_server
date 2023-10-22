import cv2
import numpy as np
import matplotlib.pyplot as plt
import collections
from tkinter import *
import datetime
import threading

user = {
    "name": 'Lê Đức Nam Khánh',
    "MBN": 17,
}

root = Tk()
root.geometry('500x400')
labl_0 = Label(root, text="Nhập thông tin học sinh", width=20, font=("bold", 20))
labl_0.place(x=90, y=53)

NameVar = StringVar()
MbnVar = StringVar()

list_x = []
list = []
list_y = []
counting = [0, 0]
check = 0
dict = {}
ex1 = 0
ey1 = 0
ew1 = 0
eh1 = 0
x1 = 0
y1 = 0
w1 = 0
h1 = 0
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


def saveInfo():
    def start_command(command):
        def detect():
            global list_x, list, list_y, ex1, ey1

            # global check, dict, ex1, ey1, ew1, eh1, eye_cascade, cap, x1, y1, w1, h1
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            eyes = eye_cascade.detectMultiScale(frame)
            dict = {}
            for (ex, ey, ew, eh) in eyes:
                area = (ew * eh)
                dict[area] = (ex, ey, ew, eh)
            dict = collections.OrderedDict(sorted(dict.items(), reverse=True)[:2])
            # dict = take(2,dict.items())
            for key in dict.keys():
                ex1, ey1, ew1, eh1 = dict[key]
                # cv2.rectangle(frame, (ex1, ey1), (ex1 + ew1, ey1 + eh1), (0, 255, 0), 2)
                break
            print(dict)
            # list_x=[]
            # list = []
            # list_y = []
            # ew1 = 35
            # eh1 = 35
            ex1 = ex1 + 10
            ey1 = ey1 + 10
            while True:
                ret, img = cap.read()
                if ret is False:
                    continue
                # frame[y:x]
                # eyes = eye_cascade.detectMultiScale(frame)
                '''ex, ey, ew, eh = eyes[0]
                ex1, ey1, ew1, eh1 = eyes[1]
                cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                cv2.rectangle(frame, (ex1, ey1), (ex1 + ew, ey1 + eh), (0, 255, 0), 2)'''
                '''dict = {}
                for (ex,ey,ew,eh) in eyes:
                    area = (ew * eh)
                    dict[area]=(ex,ey,ew,eh)
                dict = collections.OrderedDict(sorted(dict.items(), reverse=True)[:2])
                #dict = take(2,dict.items())
                print(dict)
                for key in dict.keys():
                    ex1, ey1, ew1, eh1 = dict[key]
                    #cv2.rectangle(frame, (ex1, ey1), (ex1 + ew1, ey1 + eh1), (0, 255, 0), 2)
                    break
            '''
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
        def counter():
            if sta_btn['text'] != 'Bắt Đầu':
                counting[0] += 1

                if counting[0] == 100:
                    counting[1] += 1
                    counting[0] = 0
                    counting_num.config(text=f'{datetime.timedelta(seconds=counting[1])}:00')

                else:
                    counting_num.config(text=f'{datetime.timedelta(seconds=counting[1])}:{counting[0]}')
            else:
                counting_num.config(text='0:00:00:0')
            root.after(10, counter)

        # sta_btn2 = Button(root, text = "Kết thúc", command=, font=("bold", 12))
        # sta_btn2.place(x=300,y=530)
        def ketqua():
            global list_y, list_x, counting

            print(list_y)
            # list_y = [10, 12, 10, 12, 10, 12]
            # list_x = [10, 10, 11, 11, 12, 12]
            # plt.plot(list_y,list_x)
            # plt.title(f" \n Họ và tên: {user['name']} \n Mã học sinh: {user['MBN']} \n Thời gian: {counting[1]} giây")
            # plt.show()
            img = cv2.imread("res.png")
            cv2.imshow("Ket qua", img)

        global check, list, list_x, list_y
        det = threading.Thread(target=detect, args=())
        if command == 'start':
            sta_btn.config(text="Kết thúc", command=lambda: start_command('stop'))
            det.start()
            counting_num.config(text='0:00:00:0')
            check = 0
            list_x = []
            list = []
            list_y = []
            counter()
        elif command == 'stop':
            sta_btn.config(text="Bắt Đầu", command=lambda: start_command('start'))
            ketqua()
            # cv2.destroyAllWindows()
            check = 1

    user["name"] = NameVar.get()
    user["MBN"] = MbnVar.get()
    # print(NameVar.get())
    labl_0.destroy()
    name.destroy()
    e1.destroy()
    Mbn.destroy()
    e2.destroy()
    btn.destroy()
    root.geometry('700x600')
    heading = Label(root, text="Hãy đọc đoạn văn sau", width=20, font=("bold", 20))
    heading.place(x=185, y=70)
    counting_text = Label(root, text="Thời gian: ", font=("bold", 17))
    counting_text.place(x=400, y=130)
    counting_num = Label(root, text="0:00:00:0", font=("bold", 17))
    counting_num.place(x=520, y=130)
    text_file = open("vanmau.txt", 'r', encoding="utf8")
    content = text_file.read()
    doanvan = Text(root, width=61, heigh=15, font=("bold", 14), wrap=WORD)
    doanvan.place(x=10, y=170)
    doanvan.insert(END, content)
    text_file.close()
    sta_btn = Button(root, text="Bắt Đầu", command=lambda: start_command('start'), font=("bold", 12))
    sta_btn.place(x=300, y=530)


name = Label(root, text="Họ và tên", width=20, font=("bold", 10))
name.place(x=80, y=130)
e1 = Entry(root, textvariable=NameVar)
e1.place(x=240, y=130)
Mbn = Label(root, text="Mã học sinh", width=20, font=("bold", 10))
Mbn.place(x=68, y=180)
e2 = Entry(root, textvariable=MbnVar)
e2.place(x=240, y=180)
btn = Button(root, text="Gửi", command=saveInfo, font=("bold", 14))
btn.place(x=220, y=240)
root.mainloop()
# eye8 roi = frame[650: 850, 400: 600]
# sakshi roi = frame[700: 900, 100: 400]
# anshul_normal = frame[680: 900, 200: 450]
# video1.mp4 = frame[930: 1100, 270: 480]
# dyslexic sakshi,anshul

# dyslexic
# cap = cv2.VideoCapture("sakshi.mp4")
# cap = cv2.VideoCapture("anshul_dyslexic.mp4")

# non
# cap = cv2.VideoCapture("khanhle.mp4")


# cap = cv2.VideoCapture("anshul_normal.mp4")
# ret,frame = cap.read()
# eyes = eye_cascade.detectMultiScale(frame)
# dict = {}
# for (ex,ey,ew,eh) in eyes:
#     area = (ew * eh)
#     dict[area]=(ex,ey,ew,eh)
# dict = collections.OrderedDict(sorted(dict.items(), reverse=True)[:2])
# #dict = take(2,dict.items())
# for key in dict.keys():
#     ex1, ey1, ew1, eh1 = dict[key]
#     # cv2.rectangle(frame, (ex1, ey1), (ex1 + ew1, ey1 + eh1), (0, 255, 0), 2)
#     break
# print(dict)


# while 1:
#     ret, frame = cap.read()
#     if ret is False:
#         break
#     #frame[y:x]
#     # eyes = eye_cascade.detectMultiScale(frame)
#     # ex, ey, ew, eh = eyes[0]
#     # ex1, ey1, ew1, eh1 = eyes[1]
#     # cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
#     # cv2.rectangle(frame, (ex1, ey1), (ex1 + ew, ey1 + eh), (0, 255, 0), 2)
#     # dict = {}
#     # for (ex,ey,ew,eh) in eyes:
#     #     area = (ew * eh)
#     #     dict[area]=(ex,ey,ew,eh)
#     # dict = collections.OrderedDict(sorted(dict.items(), reverse=True)[:2])
#     # #dict = take(2,dict.items())
#     # print(dict)
#     # for key in dict.keys():
#     #     ex1, ey1, ew1, eh1 = dict[key]
#     #     #cv2.rectangle(frame, (ex1, ey1), (ex1 + ew1, ey1 + eh1), (0, 255, 0), 2)
#     #     break
#     eyes = eye_cascade.detectMultiScale(frame)
#     if not bool(dict):
#         for (ex,ey,ew,eh) in eyes:
#             area = (ew * eh)
#             dict[area]=(ex,ey,ew,eh)
#             ex1 = ex
#             ey1 = ey
#             ew1 = ew
#             eh1 = eh
#     # dict = collections.OrderedDict(sorted(dict.items(), reverse=True)[:2])
#         # print(dict)
#     #dict = take(2,dict.items())
#     if bool(dict):
#         # for key in dict.keys():
#         #     ex1, ey1, ew1, eh1 = dict[key]
#         #     # cv2.rectangle(frame, (ex1, ey1), (ex1 + ew1, ey1 + eh1), (0, 255, 0), 2)
#         #     break
#         # cv2.rectangle(frame, (193, 193), (193 + 60, 193+ 60), (0, 255, 0), 2)
#         cv2.rectangle(frame, (ex1, ey1), (ex1 + ew1, ey1 + eh1), (0, 255, 0), 2)
#         cv2.imshow("frame",frame)
#         roi = frame[ey1: (ey1 + eh1), ex1: (ex1 + ew1)]
#         print(ex1, ey1, eh1, ew1)
#         # roi = frame[269: 795, 537:1416]
#         rows, cols, _ = roi.shape
#         gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
#         gray_roi = cv2.GaussianBlur(gray_roi, (7, 7), 0)

#         _, threshold = cv2.threshold(gray_roi, 70, 255, cv2.THRESH_BINARY_INV)
#         contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#         contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

#         for cnt in contours:
#             (x, y, w, h) = cv2.boundingRect(cnt)

#             #cv2.drawContours(roi, [cnt], -1, (0, 0, 255), 3)
#             cv2.rectangle(roi, (x, y), (x + w, y + h), (8, 0, 0), 2)
#             cv2.line(roi, (x + int(w/2), 0), (x + int(w/2), rows), (0, 255, 0), 2)
#             cv2.line(roi, (0, y + int(h/2)), (cols, y + int(h/2)), (0, 255, 0), 2)
#             cv2.circle(roi, (x + int(w/2),y + int(h/2) ), 1, (0, 0, 255), 2)
#             list.append((x + int(w/2), y + int(h/2)))
#             list_x.append(x + int(w/2))
#             list_y.append(y + int(h/2))
#             break


#         cv2.imshow("Threshold", threshold)
#         cv2.imshow("gray roi", gray_roi)
#         cv2.imshow("Roi", roi)
#         key = cv2.waitKey(30)
#         if key == 27:
#             break

# print(list_y,list_x)
# plt.plot(list_y,list_x)
# plt.title(f"Họ và tên: {user['name']} \n Mã bệnh nhân: {user['MBN']}")
# plt.show()
# cap = cv2.VideoCapture("anshul_normal.mp4")
# cap = cv2.VideoCapture("sakshi.mp4")
# while True:
#     ret, frame = cap.read()
#     if ret is False:
#         break

#     roi = frame[650: 850, 400: 600]

#     key = cv2.waitKey(10)
#     if key == 27:
#         break
#     for x,y in list:
#         print(x,y)
#         cv2.circle(roi, (x,y), 1, (0, 0, 255), 1)
#     cv2.imshow("dots", roi)

# cv2.destroyAllWindows()
