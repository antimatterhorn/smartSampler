from math import *
import numpy as np
import random
import matplotlib.pyplot as plt
import scipy.spatial as KDTree

def distance(thisTree,item,loc):
    a = thisTree.data[item]
    d = 0
    for i in range(2):
        d += (loc[i]-a[i])**2
    return sqrt(d)

xdim = 1.0
ydim = 1.0
ndims = 2.0

bign = 1000

xs = np.zeros(bign)
ys = np.zeros(bign)
for i in range(bign):
    xs[i] = random.random()*xdim
    ys[i] = random.random()*ydim

bigtree = KDTree.KDTree(zip(xs.ravel(),ys.ravel()))

new_x = []
new_y = []

new_x.append(xs[0])
new_y.append(ys[0])



js = []
for n in range(1,200):
    xx = np.asarray(new_x)
    yy = np.asarray(new_y)
    tree = KDTree.KDTree(zip(xx.ravel(),yy.ravel()))
    num = bign+1

    sn = n
    d = 0
    j = bign

    for i in range(1,bign):
        pos = [xs[i],ys[i]]
        dist = tree.query(np.asarray(pos))
        if dist > d:
            j = i
            d = dist
    if j==bign:
        print("something went wrong")
    else:
        js.append(j)
        new_x.append(xs[j])
        new_y.append(ys[j])

print(js)


#tree = KDTree.KDTree(zip(xs.ravel(),ys.ravel()))


#tree.query_ball_point([0.5,0.5],0.25)

#plt.plot(xs,ys,"k+")
plt.plot(new_x,new_y,"ro")
plt.show()