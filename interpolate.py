from math import sqrt
import numpy as np
import kernel

def interp(y1,y2,xarray,y1array,y2array,rarray,warray):
    numPoints = len(y1array)
    xout = np.zeros(len(xarray[0]))
    for i in range(numPoints):
        y1i = y1array[i]
        y2i = y2array[i]
        xx  = y1i - y1
        yy  = y2i - y2
        rij = sqrt(xx**2+yy**2)
        hi  = 2.0/rarray[i]**2
        for j in range(len(xarray[0])):
            xout[j] += xarray[i][j]*kernel.W(rij,hi)*warray[i]
    return xout
