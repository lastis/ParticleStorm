import os
import numpy
import cv2
from matplotlib import pyplot as plt

# Read picture in a grayscale 
im = cv2.imread('A002.bmp',cv2.CV_LOAD_IMAGE_GRAYSCALE)

#Show image and wait for key press
#cv2.imshow('image',im)
#cv2.waitKey(0)

# Try blurring the images to reduce noise
im1 = cv2.GaussianBlur(im,(5,5),0)
im2 = cv2.GaussianBlur(im,(11,11),0)
im3 = cv2.GaussianBlur(im,(25,25),0)

# Test with Otsu's thresholding
ret, th1 = cv2.threshold(im1,0,255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret, th2 = cv2.threshold(im2,0,255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret, th3 = cv2.threshold(im3,0,255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret, th4 = cv2.threshold(im,0,255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',th1)
cv2.waitKey(0)
cv2.imshow('image',th2)
cv2.waitKey(0)
cv2.imshow('image',th3)
cv2.waitKey(0)
cv2.imshow('image',th4)
cv2.waitKey(0)
"""
images = [[im1, im2, im3],
	  [th1, th2, th3]]

for i in xrange(3):
	plt.subplot(3,3,3*i+1), plt.xticks([]), plt.yticks([])
	plt.imshow(images[0][i],'gray')
	plt.subplot(3,3,3*i+2), plt.xticks([]), plt.yticks([])
	plt.hist(  images[0][i].ravel(),256)
	plt.subplot(3,3,3*i+3), plt.xticks([]), plt.yticks([])
	plt.imshow(images[1][i],'gray')
plt.show()

"""



# test
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',th3)
cv2.waitKey(0)


con,hi = cv2.findContours(th3,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
# Count the aggregations
cnt = 0
i   = 0
while (i != -1):
	cnt += 1;
	# This is the hirerichal syntax which sets i to
	# the next contour on the same level
	i = hi[0][i][0];

#Calculate som spesific values on contor number 10 (index 9)
parInCon9 = 17 
area = cv2.contourArea(con[9])
parSize = area/19;
# Draw the contour 
cv2.drawContours(im, con,9,(0,0,0),2)
#Show image and wait for key press
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',im)
cv2.waitKey(0)


# Lets test the area of a new contour
cv2.drawContours(im, con,6,(255,255,255),2)
area = cv2.contourArea(con[6])/parSize
print 'Area is ',area
#Show image and wait for key press
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',im)
cv2.waitKey(0)



# Lets test the area of a new contour
cv2.drawContours(im, con,8,(255,255,255),2)
area = cv2.contourArea(con[8])/parSize
print 'Area is ',area
#Show image and wait for key press
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',im)
cv2.waitKey(0)

#Show images and wait for key press
cv2.destroyAllWindows()
