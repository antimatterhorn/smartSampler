from math import *

class vector2:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def magnitude(self):
        return sqrt(self.x**2+self.y**2)
    def dot(self,w):
        return self.x*w.x+self.y*w.y 
    def __repr__(self):
        return "<%3.3f,%3.3f>" % (self.x,self.y)

class vector3:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def magnitude(self):
        return sqrt(self.x**2+self.y**2+self.z**2)
    def dot(self,w):
        return self.x*w.x+self.y*w.y+self.z*w.z
    def __repr__(self):
        return "<%3.3f,%3.3f,%3.3f>" % (self.x,self.y,self.z)