from math import *
import numpy as np
import scipy.spatial as spatial

def down(points,numPoints):
    ndims = len(points[0])
    mins = np.zeros(ndims)
    maxs = np.zeros(ndims)
    for j in range(ndims):
        mins[j] = 1.0e30
        maxs[j] = -1.0e30
    for i in range(len(points)):
        ppi = points[i]
        for j in range(ndims):
            mins[j] = min(ppi[j],mins[j])
            maxs[j] = max(ppi[j],maxs[j])
    print("extrema for new inputs: ",mins,maxs)
    print("down sampling to %d best candidates"%numPoints)
    bign = len(points)
    bigtree = spatial.KDTree(points)

    new_points = []
    new_points.append(points[0])

    for n in range(1,numPoints):
        px = np.asarray(new_points)
        tree = spatial.KDTree(px)
        j = bign
        d = 0
        for i in range(1,bign):
            pos = points[i]
            dist = tree.query(pos)
            if dist > d:
                j = i
                d = dist
        if j==bign:
            print("something went wrong!")
        else:
            new_points.append(points[j])
    return np.asarray(new_points)

'''
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
'''