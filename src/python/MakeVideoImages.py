import os

# This doesn't seem to work

# Set 2 -r 0.5
#ffmpeg -i A007\ -\ 20131029_125646.wmv  -r 0.05 -f image2 image%3d.bmp

# Rename all img files to seconds 
# Changeable variables
directory 	= 'FirstMeasure/Set1/'
dirPath 	= '../../res/' + directory
cmd1 		= 'ffmpeg -i ' 
videoName 	= 'A008_133441.wmv'
cmd2 		= ' -r 0.5 -f image2 image%3d.bmp'
cmd 		= cmd1 + videoName + cmd2

# Change the os directory to picture folder
os.chdir(dirPath)
os.system(cmd1 + videoName + cmd2)

