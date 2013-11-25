import os
import numpy
import cv2
import ProcessMethods as pm


# Changable variables
imgName 	= '00260.bmp'
contNum 	= 50  	# The contour number (from 0 to max)
findParSize 	= 1
parInCont 	= 45 	# The number of particles in the said contour 
directory     	= 'MagneticHoles/Set3/'
threshold	= pm.threshold3

dirPath = '../../res/' + directory

# Change the os directory to correct folder
os.chdir(dirPath)
img = cv2.imread(imgName, cv2.CV_LOAD_IMAGE_GRAYSCALE)
th  = threshold(imgName,0)
# Find the contours
cv2.namedWindow('CalibrationImage',cv2.WINDOW_NORMAL)
cv2.imshow('CalibrationImage',img)
cv2.waitKey(0)
con,hi = cv2.findContours(th,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

# Find the area
if(findParSize):
	area   = cv2.contourArea(con[contNum])
	parSize = area/parInCont
	# Print particle size so we can use it in ProcessImages.py
	print "Particle size is: ", parSize

# Count the aggregations
cnt = 0
i   = 0
while (i != -1):
	cnt += 1;
	# This is the hirerichal syntax which sets i to
	# the next contour on the same level
	i = hi[0][i][0]
print "Number of aggregations are : ", cnt

# Draw the contour on the original picture and show the 
# the original picture. All contours are highlighted in black
# and the contour we want to count particles on is highlighted in white
print "Drawing contours, black contour is cont nr. : ", contNum
cv2.drawContours(img,con,-1,(255,255,255),1)
cv2.drawContours(img,con,contNum,(0,0,0),1)
cv2.namedWindow('CalibrationImage',cv2.WINDOW_NORMAL)
cv2.imshow('CalibrationImage',img)
cv2.waitKey(0)
