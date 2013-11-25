import numpy
import ProcessMethods as pm

# Changeable variables
# Diectory to prepaired images
directory	= 'MagneticHoles/Set2/Prepaired/'
dirPath 	= '../../res/' + directory
# In the images there are a size difference from the video
# to the other images, so two sizes are used for one set of pictures
parSize1	= 143
parSize2	= 331.95
changeTime1	= 400	# The time (in seconds) the particle size changes

def process(imgName, cnt) :
	area = pm.getArea(imgName, cnt)
	timeString = imgName[0:-4]
	time = int(timeString)
	# Turn the area into number of particles
	if(time < changeTime1) :
		area = area/parSize1
	else :
		area = area/parSize2
	#print 'Total Particles: ', sum(area)
	# Save the data as a txt file with the same name
	numpy.savetxt(timeString+".txt",area)

# Run our defined method on all images
pm.itterateThroughFiles(dirPath,process)
