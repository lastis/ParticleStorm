import os
import glob
import numpy
import cv2

def itterateThroughFiles(dir, func, fileType = '.bmp', subString = ""):
	# Change the os directory to picture folder
	os.chdir(dir)
	# Get all the images in a directory and make output folder
	files = glob.glob('*')
	files.sort()
	# Itterate through all the files and check if it 
	# matches the correct filetype and substring
	cnt = 0;
	for fileName in files:
		# If the file is not found, continue
		if (fileName.find(fileType)  == -1) :
			continue
		if (fileName.find(subString) == -1):
			continue
		func(fileName,cnt)
		print fileName
		cnt += 1
	if (cnt == 0) :
		print 'No files with given parameters found'


# These methods are different ways of applying a threshold to get good images
def threshold1(imgName,cnt) :
	# This is used for magnetic holes set 1
	img = cv2.imread(imgName, cv2.CV_LOAD_IMAGE_GRAYSCALE)
	out = cv2.GaussianBlur(img,(15,15),0)
	out = cv2.adaptiveThreshold(out, 255, 
			cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,-1)
	out = cv2.GaussianBlur(out,(15,15),0)
	ret,out = cv2.threshold(out,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	return out

def threshold2(imgName,cnt) :
	# This is used for magnetic holes set 2
	img = cv2.imread(imgName, cv2.CV_LOAD_IMAGE_GRAYSCALE)
	out = cv2.GaussianBlur(img,(15,15),0)
	out = cv2.adaptiveThreshold(out, 255, 
			cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,-1)
	ret,out = cv2.threshold(out,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	out = cv2.GaussianBlur(out,(27,27),0)
	ret,out = cv2.threshold(out,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	return out

def threshold3(imgName,cnt) :
	# This is used for magnetic holes but where we have a 
	# highlighted area in the center, set 3
	img = cv2.imread(imgName, cv2.CV_LOAD_IMAGE_GRAYSCALE)
	out = cv2.GaussianBlur(img,(11,11),0)
	out = cv2.adaptiveThreshold(out, 255, 
			cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,-2)
	out = cv2.GaussianBlur(out,(21,21),0)
	ret,out = cv2.threshold(out,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	return out

def threshold4(imgName,cnt) :
	# This is used for the iron particles
	img = cv2.imread(imgName, cv2.CV_LOAD_IMAGE_GRAYSCALE)
	ret, th = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	return th

# Find the area of all the contours and return them as an array
# Need prepaired images for this to work
def getArea(imgName,cnt) :
	img 	= cv2.imread(imgName, cv2.CV_LOAD_IMAGE_GRAYSCALE)
	con,hi 	= cv2.findContours(img,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
	# Count the aggregations with the hierchy given
	# by the find contours method
	cnt = 0
	i   = 0
	while (i != -1):
		# This is the hirerichal syntax which sets i to
		# the next contour on the same level
		i = hi[0][i][0]
		cnt += 1;
	# Create an array with areas
	area = numpy.zeros(cnt)
	i    = 0
	cnt  = 0
	while (i != -1):
		i = hi[0][i][0]
		area[cnt] = cv2.contourArea(con[i])
		# Set j to the child cont. of i
		j = hi[0][i][2]
		# itterate through the child cont. and remove
		# the area in them
		while (j != -1):
			j = hi[0][j][0]
			area[cnt] -= cv2.contourArea(con[j])
		cnt += 1
	return area
