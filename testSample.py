import numpy as np
import kernel
import matplotlib.pyplot as plt
import calculation
import interpolate
import random
from math import *
from vectorMath import *
from point import point

do_Corrections  = True
do_Map          = True
do_NewSample    = False

numPoints = 1000
nNeighbor = 20           
numInputs = 2
points = []

xmin = 1.e25
xmax = -1.e25
ymin = 1.e25
ymax = -1.e25

xs = np.zeros(numPoints)
ys = np.zeros(numPoints)
# populate initial sample
for i in range(numPoints):
    state = np.zeros(numInputs)
    for j in range(numInputs):
        state[j] = 1.0
    x = random.random()*10.0
    y = random.random()*10.0
    xs[i] = x
    ys[i] = y
    xmin = min(x,xmin)
    ymin = min(y,ymin)
    xmax = max(x,xmax)
    ymax = max(y,ymax)
    pos = vector2(x,y)
    points.append(point(i,pos,state))
# construct neighbor sets
for i in range(numPoints):
    thisPoint = points[i]
    thisPoint.updateNeighbors(points,nNeighbor)
    thisPoint.weight = thisPoint.volume
# calculate the 0th order corrections
if do_Corrections:
    for i in range(numPoints):
        thisPoint = points[i]
        thisPoint.calcCorrection(points)




if do_Map:
    sSize = 50
    iMap = np.zeros([sSize,sSize])
    xx = np.linspace(xmin,xmax,sSize)
    yy = np.linspace(ymin,ymax,sSize)

    for i in range(sSize):
        for j in range(sSize):
            x = (xmax-xmin)*j/sSize+xmin
            y = (ymax-ymin)*i/sSize+ymin
            val = interpolate.interp(x,y,points)
            iMap[i][j] = val[1]
            #print(x,y,val)
    plt.pcolor(xx,yy,iMap)
    plt.colorbar()


if do_NewSample:
    numNewSamples = 10
    numPoints = len(points)
    newPoints = []
    xs = np.zeros(numNewSamples)
    ys = np.zeros(numNewSamples)
    for i in range(numNewSamples):
        xn = random.random()*2+6.0
        yn = random.random()*2+6.0
        sn  = interpolate.interp(x,y,points)   
        x,y = calculation.func(sn)
        xs[i] = x
        ys[i] = y
        newPoints.append(point(i+numPoints,vector2(x,y),sn))
        print(xn,yn,sn,x,y)
    plt.plot(xs,ys,"ro")
plt.scatter(xs,ys,c='black',marker='+')
plt.xlim(xmin,xmax)
plt.ylim(ymin,ymax)
plt.show()