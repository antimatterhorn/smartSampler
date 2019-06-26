import numpy as np
import kernel
import matplotlib.pyplot as plt
import calculation
import interpolate
import random
from math import *
from vectorMath import *

class point:
    def __init__(self,id,position,state):
        self.id = id
        self.position = position
        self.state = state
        self.elements = len(state)
        self.neighbors = []
        self.weight = 0.0
        self.radius = 0.0
        self.correction = 0.0
    def updateNeighbors(self,points,nCount):
        n = len(points)
        myPos = self.position
        myId  = self.id
        others = []
        for i in range(n):
            pi = points[i]
            if pi.id != myId:
                xij = myPos.x - pi.position.x
                yij = myPos.y - pi.position.y
                rij = vector2(xij,yij).magnitude()
                others.append([rij,pi.id])
        others.sort()
        for i in range(nCount):
            self.neighbors.append(others[i][1])
        self.radius = others[nCount-1][0]
        self.weight = self.radius**2
    def calcCorrection(self,points):
        n = len(points)
        myId = self.id
        weights = 0.0
        for i in range(len(self.neighbors)):
            thisId = self.neighbors[i]
            thisWeight = points[thisId].weight
            weights += thisWeight
        self.correction = 1.0/weights

numPoints = 400
nNeighbor = 20           
numInputs = 2
points = []

xmin = 1.e25
xmax = -1.e25
ymin = 1.e25
ymax = -1.e25

xs = np.zeros(numPoints)
ys = np.zeros(numPoints)

for i in range(numPoints):
    state = np.zeros(numInputs)
    for j in range(numInputs):
        state[j] = random.random()*10.0
    x,y = calculation.func(state)
    xs[i] = x
    ys[i] = y
    xmin = min(x,xmin)
    ymin = min(y,ymin)
    xmax = max(x,xmax)
    ymax = max(y,ymax)
    pos = vector2(x,y)
    points.append(point(i,pos,state))
for i in range(numPoints):
    thisPoint = points[i]
    thisPoint.updateNeighbors(points,nNeighbor)
for i in range(numPoints):
    thisPoint = points[i]
    thisPoint.calcCorrection(points)

sSize = 50
iMap = np.zeros([sSize,sSize])
xx = np.linspace(xmin,xmax,sSize)
yy = np.linspace(ymin,ymax,sSize)

for i in range(sSize):
    for j in range(sSize):
        x = (xmax-xmin)*j/sSize+xmin
        y = (ymax-ymin)*i/sSize+ymin
        val = interpolate.interp(x,y,points)
        iMap[i][j] = val[0]
        print(x,y,val)

plt.plot(xs,ys,"g+")
plt.pcolor(xx,yy,iMap)
plt.colorbar()
plt.show()