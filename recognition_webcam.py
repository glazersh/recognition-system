#Coded by:- Kushal Bhavsra
#From:- Techmicra IT solution
import time
import cv2
import label_image
import os,random
import subprocess


def count_emotions(ans_arr_emotions):
    count_map = {}
    for emo in ans_arr_emotions:
        if emo in count_map:
            count_map[emo] += 1
        else:
            count_map[emo] = 1
    return count_map

def print_precentage(dict_emotions):
    for emotion in dict_emotions:
        print (emotion + ":" + str(str(float(dict_emotions[emotion]/len(ans_arr_emotions))*100)+"%"))


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

size = 4
ans_arr_emotions = []
# We load the xml file
classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
global text
# Resize the image to speed up detection
files_path=os.listdir(r"C:\Users\dorlev\Emotion_recognition_system-master\check")
i=1
for file_path in files_path:
    i +=1
    print(file_path)
    #path="C:\Users\dorlev\Emotion_recognition_system-master\check\\"
    im=cv2.imread(r"C:\Users\dorlev\Emotion_recognition_system-master\check\\" + file_path )
    mini = cv2.resize(im, (int(im.shape[1] / size), int(im.shape[0] / size)))
    # detect MultiScale / faces
    faces = classifier.detectMultiScale(mini)
    #pdb.set_trace()
    # Draw rectangles around each face
    if len(faces)==0:
        ans_arr_emotions.append("none")
    for f in faces:
        (x, y, w, h) = [v * size for v in f]  # Scale the shapesize backup
        sub_face = im[y:y + h, x:x + w]
        FaceFileName = "test.jpg"   # Saving the current image from the webcam for testing.
        cv2.imwrite(FaceFileName, sub_face)
        text = label_image.main(FaceFileName)  # Getting the Result from the label_image file, i.e., Classification Result.
        text = text.title()  # Title Case looks Stunning.
        font = cv2.FONT_HERSHEY_TRIPLEX
        ans_arr_emotions.append(text)
        if text == 'Angry':
            print('Angry')
        if text == 'Happy':
            print('Happy')
        if text == 'Fear':
            print('Fear')
        if text == 'Sad':
            print('Sad')
    # Show the image/
    cv2.imshow('Emotion recognition', im)
    key = cv2.waitKey(30)& 0xff
print(ans_arr_emotions)

dict_emotions = count_emotions(ans_arr_emotions)
print_precentage(dict_emotions)
