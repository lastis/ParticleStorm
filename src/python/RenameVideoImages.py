import os
import glob
import ProcessMethods as pm

# Set 2 -r 0.5
#ffmpeg -i A007\ -\ 20131029_125646.wmv  -r 0.05 -f image2 image%3d.bmp

# Rename all image files to TIME.bmp (in seconds)
# Changeable variables
directory 	= 'IronParticles/Set3/'
dirPath 	= '../../res/' + directory
startTime 	= 0	# In seconds
timeStep 	= 20	# In seconds
imageIdentifier = 'image'	# Substring the identifies the 
				# image files

def rename(fileName,cnt):
	time = cnt*timeStep
	newName = '%05d.bmp' %time
	os.rename(fileName,newName)

#rename AXXX_TIMESTAMP.bmp files
pm.itterateThroughFiles(dirPath,rename,subString=imageIdentifier)

