from Shapes.Circle import Circle
from math import cos, sin

class Bullet(Circle):

    def __init__(self, name, x, y, theta):
        Circle.__init__(self, name, 3, (0, 250, 0), x, y) 
        self.theta = theta
        self.speed = 100.
        self.vX = self.speed * cos(self.theta)
        self.vY = self.speed * sin(self.theta)
        self.theta = theta

