import numpy
import ProcessMethods as pm
from matplotlib import pyplot as plt
from scipy 	import stats

# Changeable variables
directory = 'MagneticHoles/Set3/Prepaired/'
dirPath = '../../res/' + directory

# Initialize some lists we need
time 	     = []
aggregations = []
averageSize  = []
areaVec	     = []

def calculate(fileName,cnt) :
	area = numpy.loadtxt(fileName)
	area = numpy.around(area)
	area = area.astype(int)
	areaVec.append(area)
	time.append(int(fileName[0:-4]))

pm.itterateThroughFiles(dirPath,calculate,fileType='.txt')

particlesStart = sum(areaVec[0])
for area in areaVec:
	# Do a scaling to ensure the same number
	# of particles in each image 
	particlesCurrent = sum(area)
	area = area*(particlesStart/float(particlesCurrent))
	area = numpy.around(area)
	area = area.astype(int)

	# Get data for the plots
	aggregations.append(len(area))
	# Calculate weighted average
	maxSize = int(numpy.max(area))
	ns = range(maxSize+1)
	for size in area :
		ns[size] += 1;
	S1, S2 = 0,0
	for size in xrange(maxSize) :
		S1 += ns[size]*size*size
		S2 += ns[size]*size
	S = S1/float(S2)
	averageSize.append(S)


# Log2 plot
# Initialize the plot arrays we need
averageSizeLog2  = range(len(averageSize))
averageSizeLog   = range(len(averageSize)-1)
averageSizeRel   = range(len(averageSize))
aggregationsLog2 = range(len(aggregations))
aggregationsLog  = range(len(aggregations)-1)
aggregationsRel  = range(len(aggregations))
timeLog		 = range(len(time)-1)

minSize = float(numpy.min(averageSize))
maxSize = float(numpy.max(averageSize))
maxAggr = float(numpy.max(aggregations))
for i in xrange(len(time)) :
	averageSizeLog2[i] = numpy.log2(averageSize[i]/minSize)
	averageSizeRel [i] =            averageSize[i]/maxSize

	aggregationsLog2[i] = numpy.log2(aggregations[i]/maxAggr)
	aggregationsRel [i] =            aggregations[i]/maxAggr
	# Remove the first step as time = 0
	if (i == 0) : continue
	timeLog[i-1] 		= numpy.log(time[i])
	averageSizeLog[i-1]  	= numpy.log(averageSize[i])
	aggregationsLog[i-1]  	= numpy.log(aggregations[i])


# Indices used for the line regression
i1 = 1
i2 = len(time)-1

# log vs log plots
A1, b1, R1, p1, err1 = stats.linregress(timeLog[i1:i2],aggregationsLog[i1:i2])
A2, b2, R2, p2, err2 = stats.linregress(timeLog[i1:i2],averageSizeLog[i1:i2])
print 'Agg slope is : ', A1
print 'AggSize slope is : ', A2
print 'R1 = ', R1
print 'R2 = ', R2
x1 = numpy.linspace(time[i1+1],time[i2],1000)
y1 = numpy.exp(b1)*x1**(A1)
x2 = numpy.linspace(time[i1+1],time[i2],1000)
y2 = numpy.exp(b2)*x2**(A2)

xHalf1 = x1[i1]
yHalf1 = y1[i1]
xHalf2 = x2[i1]
yHalf2 = y2[i1]

ax = plt.subplot(211)
plt.plot(time, aggregations, 'bo')
plt.plot(x1, y1, 'r')
plt.title('Log vs Log')
plt.ylabel('Aggregations')
plt.text(xHalf1+10,yHalf1+50,'z = %f, R = %f'%(A1,R1))
ax.set_yscale('log')
ax.set_xscale('log')

ax = plt.subplot(212)
plt.plot(time, averageSize,'bo')
plt.plot(x2, y2, 'r')
plt.xlabel('Time (s)')
plt.ylabel('Particle Size')
plt.text(xHalf2+10,yHalf2,'z = %f, R = %f'%(A2,R2))
ax.set_yscale('log')
ax.set_xscale('log')
plt.savefig('LogVsLog.png')
plt.figure()

plt.plot(time, averageSize)
plt.title('Aggregation Size vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('Particle Size')
plt.savefig('AggregationSize.png')
plt.figure()

plt.plot(time, aggregations)
plt.title('Aggregations vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('Aggregations')
plt.savefig('Aggregations.png')
plt.figure()

plt.plot(time, averageSizeLog2)
plt.title('log2(Aggregation Size)  vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('log2( S(t) )')
plt.savefig('AggregationSizeLog.png')
plt.figure()

plt.plot(time, aggregationsLog2)
plt.title('log2(Aggregations)  vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('log2( N(t) )')
plt.savefig('AggregationsLog.png')
plt.figure()

plt.plot(time, averageSizeRel)
plt.title('Relative Cluster Size  vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('Cluster size / Min Cluster Size')
plt.savefig('AggregationSizeRel.png')
plt.figure()

plt.plot(time, aggregationsRel)
plt.title('Relative Cluster Number  vs. Time')
plt.xlabel('Time (s)')
plt.ylabel('Clusters / Max Clusters')
plt.savefig('AggregationsRel.png')
#plt.show()


