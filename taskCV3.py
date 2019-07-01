#importing cv2 module
import cv2 
import numpy as np

img1=cv2.imread('480p1.jpg')  #reads the image provided here
img2=cv2.imread('480p2.jpg')

#cv2.imshow('1',img1)  #displays the image -- 1st parameter passed is the window-name and 2nd is the image
#cv2.imshow('2',img2)

#find the difference b/w 2 images
diff=cv2.absdiff(img1,img2)   
cv2.imshow('diff',diff)

#adding 2 images
add12=cv2.add(img1,img2)
cv2.imshow('add',add12)

#Weighted addition of images
weighted_add=cv2.addWeighted(img1,0.55,img2,0.4,0)
cv2.imshow('Weighted Add',weighted_add)

#concatenating 2 images
concat= np.concatenate((img1,img2), axis=1) #if axis=1 then concatenate horizontally
                                            #if axis=0 then concatenate vertically
cv2.imshow('concat',concat)

#wait for window to close
cv2.waitKey(0)   #mili/micro seconds   ---- if given 0 then image wait for infinite time till we stop it
