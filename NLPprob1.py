import cv2
import numpy as np
import pytesseract
from PIL import Image

cap=cv2.VideoCapture(0)
# 0 means using the first camera means your laptop camera

#to check camera is open
if cap.isOpened():
    print("camera is working")
else:
    print("problem in opening camera")      

status,img=cap.read()  #it will take a picture

#now showing
cv2.imshow('liveshow',img)

#now writing and saving the image taken
cv2.imwrite('new.jpg',img)   #this saved image is used while calling get_string function

#wait for window to close
cv2.waitKey(1000)   #mili/micro seconds   ---- if given 0 then image wait for infinite time till we stop it

#to close camera
cap.release()

# Path of working folder on Disk
src_path="C:\\Users\\Akshat\\Desktop\\OpenCV\\"  #give the path where your image is to be stored

def get_string(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite(src_path + "noiseremoved.png", img)

    #  Apply threshold to get image with only black and white
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv to do some ...
    cv2.imwrite(src_path + "thresh.png", img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(src_path + "thresh.png"))

    return result


print ('--- Start recognize text from image ---')
print (get_string(src_path + "new.jpg"))

print ("------ Done -------")
