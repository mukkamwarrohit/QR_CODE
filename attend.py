from asyncore import read, write
from email.generator import DecodedGenerator
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import sys
import time
import pybase64

#start webcam

cap = cv2.VideoCapture(0)

names =[]

# attendance file

fob= open('attendance.txt','a+')
def enterData(z):
    if z in names:
        pass
    else:
        names.append(z)
        z=''.join(str(z))
        fob.write(z+'-present''\n')
        return names
print('STARTING WEBCAM..!')



#function data present or not

def checkData(data):
    data = str(data)
    if data in names:
        print('Already Present')
    else:
        print('\n'+str(len(names)+1)+'\n'+'Marked Present')
    enterData(data)

while True:
    _,frame= cap.read()
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        checkData(obj.data)
        time.sleep(1)

    cv2.imshow('Frame',frame)


    #close

    if cv2.waitKey(1)&0xFF == ord('s'):
            cv2.destroyAllWindows()
            break
    

fob.close()
