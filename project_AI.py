#Made my Khashbat Enkhbat. For the use of Crowd density application.
#First Part Of The program for image capture
import cv2
import time
import os
#Second part of the program for object counter
#Here are the libraries to use for the detecting objects
from cvlib.object_detection import draw_bbox
from numpy.lib.polynomial import poly
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cv

#Open any camera that is connected to the computer
cap = cv2.VideoCapture(0)
i = 0
 
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    #Save frame every 15 seconds for compehensive data analysis
    cv2.imwrite('image'+str(i)+'.jpg', frame)
    time.sleep(15)
    #We'll use the imshow function of the matplotlib package to display a picture.
    #Below is a display of the code.
    image = cv2.imread('image'+str(i)+'.jpg')
    image1 = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(10,10))
    plt.axis('off')
    plt.imshow(image1)
    plt.show()
    box, label, count = cv.detect_common_objects(image)
    output = draw_bbox(image, box, label, count)
    #We would use the imshow function once more to display the resulting image, 
    #and the output would be fairly accurate. 
    output = cv2.cvtColor(output,cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(9,9))
    plt.axis('off')
    plt.imshow(output)
    plt.show()
    i += 1
    print("Objects inside this train is " +str(len(label)))
    #Depending on how many objects there are in the train, we could do myriad of things
    #such as adjusting the temperatures, increasing airflow and notify the=
    #station masters about the density .
cap.release()
cv2.destroyAllWindows()










