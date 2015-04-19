from Shapes.Object2D import Object2D
from math import cos, sin, pi
import random

class Explosion:

    def __init__(self, x, y):

        self.x = x
        self.y = y
        
        self.lifetime = 100 # frames
        self.age = 0

        self.initPoints()

    def initPoints(self):

        self.pnts = []
        self.numPnts = random.randint(20,25)
        for i in range(self.numPnts):
            pnt = Object2D(x0 = self.x, y0 = self.y)
            pnt.theta = (2*pi/360.) * random.randint(0,360);
            v = random.randint(30,60)
            pnt.vX = v*cos(pnt.theta)
            pnt.vY = v*sin(pnt.theta)
            self.pnts.append(pnt)
            
    def update(self):
        self.age += 1            
        for pnt in self.pnts:
            pnt.update()

    def isDone(self):
        self.age > self.lifetime
