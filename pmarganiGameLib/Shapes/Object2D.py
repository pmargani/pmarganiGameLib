from math import cos, sin, sqrt, pi

class Object2D:

    def __init__(self, name = None, x0 = 0, y0 = 0):

        self.name = name

        self.x = x0
        self.y = y0

        self.vX = 0
        self.vY = 0

        self.aX = 0
        self.aY = 0

        self.dt = 0.1

        self.theta = 0.

    def __str__(self):
        return "%s : (%f, %f)" % (self.name, self.x, self.y)

    def update(self):
        self.updatePosition()

    def updatePosition(self):

        self.vX = self.vX + (self.aX * self.dt)
        self.x  = self.x + (self.vX * self.dt)

        self.vY = self.vY + (self.aY * self.dt)
        self.y  = self.y + (self.vY * self.dt)

    def applyAcceleration(self, accel, direction):

        self.aX = accel * cos(direction)
        self.aY = accel * sin(direction)


    def getDistanceFrom(self, obj2D):
        return sqrt((self.x - obj2D.x)**2 + (self.y -obj2D.y)**2)

if __name__ == '__main__':

    o = Object2D()
    
    print "object at rest: "
    for t in range(10):
        print "  ", t, o    
        o.updatePosition()

    print "projecticle"
    theta = pi/4.
    V = 10.0
    o.vX = V * cos(theta)
    o.vY = V * sin(theta)
    o.aY = -9.8
    for t in range(10):
        print "  ", t, o    
        o.updatePosition()

    print "changing acceleration: "
    o = Object2D()
    for t in range(10):
        a = 10 if t < 5 else 0
        o.applyAcceleration(a, 0)
        o.updatePosition()
        print "  ", t, a, o
           
    
