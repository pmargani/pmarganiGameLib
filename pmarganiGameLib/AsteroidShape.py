from Shapes.Polygon import Polygon
from math import cos, sin, pi

class AsteroidShape(Polygon):

    def __init__(self, name, x, y, theta):

        #pts = [(0,1),(1,0),(0,-1),(-1,0)]
        pts = [(0,1.25),(1,1),(1.25,0),(1,-1),(0,-0.5),(-1,-1),(-1.25,0),(-1,1)]
        s = 30.
        pts = [(x*s,y*s) for x,y in pts]
        Polygon.__init__(self, name = 'RocektBody', x0 = x, y0 = y, points = pts)
        
        self.theta = theta
        self.speed = 100.
        self.vX = self.speed * cos(self.theta)
        self.vY = self.speed * sin(self.theta)

        self.rotationSpeed = pi / 32.
        self.rotDir = 1

    def update(self):
        self.rotTheta += self.rotDir * self.rotationSpeed        
        Polygon.update(self)
