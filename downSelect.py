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