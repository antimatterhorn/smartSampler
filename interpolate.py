from math import sqrt
import numpy as np
import kernel
from vectorMath import *

def interp(x,y,points):
    numPoints = len(points)
    xout = np.zeros(len(points[0].state))
    for i in range(numPoints):
        thisPoint   = points[i]
        thisState   = thisPoint.state
        thisPos     = thisPoint.position
        thisCor     = thisPoint.correction
        thisWeight  = thisPoint.weight
        xx  = thisPos.x - x
        yy  = thisPos.y - y
        rij = vector2(xx,yy).magnitude()
        hi  = points[i].radius*0.5
        for j in range(len(thisState)):
            xout[j] += kernel.W(rij/hi,hi)*thisWeight*thisCor*thisState[j]
    return xout
