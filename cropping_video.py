import cv2
import numpy as np
from skimage import io
import matplotlib.pyplot as plt


vidcap = cv2.VideoCapture(r'C:\Users\dorlev\Emotion_recognition_system-master\videos\video1.mp4')
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite(r"C:\Users\dorlev\Emotion_recognition_system-master\check\\" + "image"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames
sec = 0
frameRate = 1.0 #//it will capture image in each 0.5 second
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)