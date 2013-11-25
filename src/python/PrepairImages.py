import os
import numpy
import cv2
import ProcessMethods as pm
# This program is built to turn images of particles into black and white
# pictures using a threshold (and blurring if needed) to make it easier to 
# count the particles 

# Changeable variables 
directory       = 'MagneticHoles/Set3/' 
outFolder 	= 'Prepaired/'
dirPath 	= '../../res/' + directory
threshold 	= pm.threshold3

def prepair(imgName, cnt) :
	th = threshold(imgName,cnt)
	cv2.imwrite(outFolder+imgName,th)

os.mkdir(dirPath+outFolder)
# Go through the files an apply our prepair method
pm.itterateThroughFiles(dirPath,prepair)
