from vectorMath import *
import numpy as np
import kernel

class point:
    def __init__(self,id,position,state):
        self.id = id
        self.position = position
        self.state = state
        self.elements = len(state)
        self.neighbors = []
        self.weight = 0.0
        self.radius = 0.0
        self.correction = 1.0
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
        self.h      = self.radius
        self.mass   = 1.0
        self.volume = np.pi*self.radius**2
    def calcCorrection(self,points):
        n = len(points)
        myId = self.id
        weights = 0.0
        for i in range(len(self.neighbors)):
            thisId = self.neighbors[i]
            thisWeight = points[thisId].weight
            thisPos    = points[thisId].position
            xij = self.position.x - thisPos.x
            yij = self.position.y - thisPos.y
            rij = vector2(xij,yij).magnitude()
            thisKern   = kernel.W(rij/self.h,self.h)
            weights += thisWeight*thisKern
        self.correction = 1.0/weights