import numpy as np
import kernel
import matplotlib.pyplot as plt
import calculation
import random
from math import *

#want to find xi that puts me in yi = 10+-5

def getHs(y1,y2):
	n = len(y1)
	r = np.zeros(n)
	for i in range(n):
		yi1 = y1[i]
		yi2 = y2[i]
		ri  = sqrt(yi1**2+yi2**2)
		rij = 1.0e25
		for j in range(n):
			if i!=j:
				yj1 = ys1[j]
				yj2 = ys2[j]
				rj  = sqrt(yj1**2+yj2**2)
				if abs(ri-rj)<rij:
					rij = abs(ri-rj)
		r[i] = rij
	return r

def interp(y1,y2,xarray,y1array,y2array,rarray):
	numPoints = len(y1array)
	r = sqrt(y1**2+y2**2)
	xout = np.zeros(4)
	for i in range(numPoints):
		y1i = y1array[i]
		y2i = y2array[i]
		ri  = sqrt(y1i**2+y2i**2)
		rij = abs(ri-r)
		hi  = 2.0/rarray[i]**2
		for j in range(4):
			xout[j] += xarray[i][j]*kernel.W(rij,hi)
	return xout

def newSamples(N,y1,y2,xarray,yi1,yi2):
	return 0

ys1 = []
ys2 = []
xs = []
numSamples = 200
for i in range(numSamples):
	x1 = random.random()*10.0
	x2 = random.random()*10.0
	x3 = random.random()*10.0
	x4 = random.random()*10.0
	xs.append([x1,x2,x3,x4])
	y1,y2 = calculation.func([x1,x2,x3,x4])
	ys1.append(y1)
	ys2.append(y2)


rs = 0.5*getHs(ys1,ys2)
xs = np.asarray(xs)
for i in range(numSamples):
	print(xs[i],rs[i])
#print(xs)

plt.plot(ys1,ys2,"+")

numNewSamples = 10
ynew1 = np.zeros(numNewSamples)
ynew2 = np.zeros(numNewSamples)
xnews = np.zeros([numNewSamples,4])
for i in range(numNewSamples):
	yn1 = random.random()*10.0-15.0
	yn2 = random.random()*6.0-8.0
	xn  = interp(yn1,yn2,xs,ys1,ys2,rs)
	xnews[i] = xn
	ynew1[i],ynew2[i] = calculation.func(xn)
	print(xn,ynew1[i],ynew2[i])



plt.plot(ynew1,ynew2,"ro")


ys1 = np.append(ys1,ynew1)
ys2 = np.append(ys2,ynew2)
xs  = np.append(xs,xnews,axis=0)
print(xs)

numSamples = len(ys1)
print(numSamples)
rs = [] # this can def. be done better
for i in range(numSamples):
	yi1 = ys1[i]
	yi2 = ys2[i]
	ri  = sqrt(yi1**2+yi2**2)
	rij = 1.0e25
	for j in range(numSamples):
		if i!=j:
			yj1 = ys1[j]
			yj2 = ys2[j]
			rj  = sqrt(yj1**2+yj2**2)
			if abs(ri-rj)<rij:
				rij = abs(ri-rj)
	rs.append(rij)
rs = 0.5*np.asarray(rs)

numNewSamples = 10
ynew1 = np.zeros(numNewSamples)
ynew2 = np.zeros(numNewSamples)
xnews = np.zeros([numNewSamples,4])
for i in range(numNewSamples):
	yn1 = random.random()*10.0-15.0
	yn2 = random.random()*6.0-8.0
	xn  = interp(yn1,yn2,xs,ys1,ys2,rs)
	xnews[i] = xn
	ynew1[i],ynew2[i] = calculation.func(xn)
	print(xn,ynew1[i],ynew2[i])
plt.plot(ynew1,ynew2,"bo")

plt.show()