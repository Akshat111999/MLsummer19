#importing cv2 module
import cv2 

img1=cv2.imread('480p1.jpg')  #reads the image provided here
img2=cv2.imread('480p2.jpg')  #provide the image which you have on your machine

print(img1.shape)
print(img2.shape)
img1[0:150,0:150]=img2[0:150,0:150]  #slicing the image1 and storing it in image2
cv2.imshow('crop1',img1)  #showing the image1 

img3=cv2.imread('480p1.jpg')  
img4=cv2.imread('480p2.jpg')

img4[0:150,0:150]=img3[0:150,0:150]
cv2.imshow('crop2', img4)

#replacing 10 rows and 20 columns of another image on an image
img5=cv2.imread('720p1.jpg')   ##provide the image which you have on your machine
img1[160:170,160:180]=img5[180:190,180:200]
cv2.imshow('10*20',img1)


#wait for window to close
cv2.waitKey(0) #mili/micro seconds   ---- if given 0 then image wait for infinite time till we stop it


