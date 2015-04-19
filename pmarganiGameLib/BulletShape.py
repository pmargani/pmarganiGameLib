from Shapes.Polygon import Polygon
from math import cos, sin

class BulletShape(Polygon):

    def __init__(self, name, x, y, theta):

        pts = [(0,1),(1,0),(0,-1),(-1,0)]
        s = 3.
        pts = [(x*s,y*s) for x,y in pts]
        Polygon.__init__(self, name = 'RocektBody', x0 = x, y0 = y, points = pts)
        
        self.theta = theta
        self.speed = 200.
        self.vX = self.speed * cos(self.theta)
        self.vY = self.speed * sin(self.theta)
