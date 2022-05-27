import cv2
from pyzbar.pyzbar import decode
import time

# img = cv2.imread('qr_scan.png')
# =============================

# print(decode(img))
# =============================
# for code in decode(img):
#     print(code.type)
#     print(code.data.decode('utf-8'))
# =============================

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

used_codes=[]

camera = True
while camera ==True:
    success,frame = cap.read()
    for code in decode(frame):
        if code.data.decode('utf-8') not in used_codes:
            print('Approved. You can enter!')
            print(code.type)
            print(code.data.decode('utf-8'))
            used_codes.append(code.data.decode('utf-8'))
            time.sleep(5)
        elif code.data.decode('utf-8') in used_codes:
            print('Sorry, this code has been already used')
            time.sleep(1)
        else:
            pass

    cv2.imshow("qr scan",frame)
    cv2.waitKey(1)
# =============================
