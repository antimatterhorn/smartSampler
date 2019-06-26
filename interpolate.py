from math import sqrt
import numpy as np
import kernel
from vectorMath import *

def interp(x,y,points):
    numPoints = len(points)
    xout = np.zeros(len(points[0].state))
    for i in range(numPoints):
        thisState = points[i].state
        thisPos = points[i].position
        thisCor = points[i].correction
        xx  = thisPos.x - x
        yy  = thisPos.y - y
        rij = vector2(xx,yy)
        rij = rij.magnitude()
        hi  = 200.*points[i].radius**-2
        for j in range(len(thisState)):
            xout[j] += thisState[j]*kernel.W(rij/hi,hi)*points[i].weight*thisCor
    return xout
