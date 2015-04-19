from Circle import Circle
from math import cos, sin

class Asteroid(Circle):

    def __init__(self, name, x, y, radius, theta):
        Circle.__init__(self, name, radius, (250, 250, 0), x, y) 
        self.theta = theta
        self.speed = 20.
        self.vX = self.speed * cos(self.theta)
        self.vY = self.speed * sin(self.theta)
        self.theta = theta

