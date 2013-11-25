import os
import glob
import ProcessMethods as pm


# Set 2 -r 0.5
#ffmpeg -i A007\ -\ 20131029_125646.wmv  -r 0.05 -f image2 image%3d.bmp

# Changeable variables
directory 	= 'IronParticles/Set3/'
dirPath 	= '../../res/' + directory
startTime 	= 0#13*60*60 + 21*60 +52
offset 		= 0#2*60 + 17 + 5085
imageIdentifier = 'img'

# Rename all image files to TIME.bmp (in seconds)
def rename(fileName, cnt):
	# This I used for some other files 
	sub  = fileName[-12:-4]
	hour = int(sub[0:2])
	min  = int(sub[3:5])
	sec  = int(sub[6:8])
	"""
	sub  = fileName[-10:-4]
	hour = int(sub[0:2])
	min  = int(sub[2:4])
	sec  = int(sub[4:6])
	"""
	# Timestamp in seconds
	time = hour*60*60+min*60+sec
	# Minus the start time and add a offset
	# (usually from image frames from a video)
	time = time - startTime + offset
	# Set the name of the file to the number of seconds
	newName = '%05d.bmp' %(time) 
	os.rename(fileName,newName)

pm.itterateThroughFiles(dirPath,rename,subString=imageIdentifier)

