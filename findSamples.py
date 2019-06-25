import numpy as np
import kernel
import matplotlib.pyplot as plt
import calculation
import interpolate
import random
from math import *

#want to find xi that puts me in yi = 10+-5

def getHs(y1,y2,nNeighbor):
    n = len(y1)
    r = np.zeros(n)
    w = np.zeros(n)
    for i in range(n):
        yi1 = y1[i]
        yi2 = y2[i]
        rr  = np.zeros(n-1)
        k = 0
        for j in range(n):
            if i!=j:
                yj1 = ys1[j]
                yj2 = ys2[j]
                xij = yj1-yi1
                yij = yj2-yi2
                rij = sqrt(xij**2+yij**2)
                rr[k] = rij
                k+=1
        rr = np.sort(rr)
        ra = 0
        for j in range(nNeighbor):
            ra+=rr[j]/nNeighbor
        ra = rr[nNeighbor-1] # simply setting radius to distance to furthest neighbor
        r[i] = ra
        w[i] = ra**(-2)
    return r,w

def newSamples(N,y1,y2,xarray,yi1,yi2):
	return 0


numInputs = 2


numSamples = 100
nNeighbor  = 10

y1min = 1.e25
y1max = -1.e25
y2min = 1.e25
y2max = -1.e25
ys1 = np.zeros(numSamples)
ys2 = np.zeros(numSamples)
xs = np.zeros([numSamples,numInputs])
weights = np.zeros(numSamples)

for i in range(numSamples):
    for j in range(numInputs):
        xs[i][j] = random.random()*10.0
    y1,y2 = calculation.func(xs[i])
    ys1[i] = y1
    ys2[i] = y2
    y1min = min(y1,y1min)
    y1max = max(y1,y1max)
    y2min = min(y2,y2min)
    y2max = max(y2,y2max)



rs,weights = getHs(ys1,ys2,nNeighbor)
xs = np.asarray(xs)
ys1 = np.asarray(ys1)
ys2 = np.asarray(ys2)

plt.plot(ys1,ys2,"go")

for i in range(numSamples):
    print(xs[i],ys1[i],ys2[i],rs[i])


sSize = 50

iMap = np.zeros([sSize,sSize])
xx = np.linspace(y1min,y1max,sSize)
yy = np.linspace(y2min,y2max,sSize)

for i in range(sSize):
    for j in range(sSize):
        x = (y1max-y1min)*j/sSize+y1min
        y = (y2max-y2min)*i/sSize+y2min
        val = interpolate.interp(x,y,xs,ys1,ys2,rs,weights)
        iMap[i][j] = val[1]
plt.pcolor(xx,yy,iMap)


'''
numNewSamples = 10
ynew1 = np.zeros(numNewSamples)
ynew2 = np.zeros(numNewSamples)
xnews = np.zeros([numNewSamples,numInputs])
for i in range(numNewSamples):
    yn1 = random.random()+20.0
    yn2 = random.random()+200.0
    xn  = interpolate.interp(yn1,yn2,xs,ys1,ys2,rs)
    xnews[i] = xn
    ynew1[i],ynew2[i] = calculation.func(xn)
    print(yn1,yn2,xn,ynew1[i],ynew2[i])



plt.plot(ynew1,ynew2,"ro")


ys1 = np.append(ys1,ynew1)
ys2 = np.append(ys2,ynew2)
xs  = np.append(xs,xnews,axis=0)
print(xs)

rs = 0.5*getHs(ys1,ys2,nNeighbor)

numNewSamples = 5
ynew1 = np.zeros(numNewSamples)
ynew2 = np.zeros(numNewSamples)
xnews = np.zeros([numNewSamples,numInputs])
for i in range(numNewSamples):
    yn1 = random.random()*10.0-15.0
    yn2 = random.random()*6.0-8.0
    xn  = interpolate.interp(yn1,yn2,xs,ys1,ys2,rs)
    xnews[i] = xn
    ynew1[i],ynew2[i] = calculation.func(xn)
    print(xn,ynew1[i],ynew2[i])
plt.plot(ynew1,ynew2,"bo")
'''
plt.show()
