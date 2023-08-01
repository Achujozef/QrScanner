import cv2
import numpy as np
from pyzbar.pyzbar import decode
import webbrowser
# img = cv2.imread('code.jpg',cv2.IMREAD_COLOR) from inmage

 

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    success,img=cap.read()
   
    code =decode(img)
    print(code)
    for qrcode in code:
        myText=qrcode.data.decode('utf-8')
        pts=np.array([qrcode.polygon],np.int32)
        rp=qrcode.rect
        cv2.polylines(img,[pts],True,(0,255,0),3)
        cv2.putText(img,myText,(rp[0],rp[1]),cv2.FONT_HERSHEY_PLAIN,0.9,(0,255,0),1)
        webbrowser.open(myText)

        print(myText)

    cv2.imshow('Result',img)
    cv2.waitKey(2)
    