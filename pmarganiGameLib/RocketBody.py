from Shapes.Polygon import Polygon
from Bullet import Bullet
from math import pi

class RocketBody(Polygon):

    def __init__(self):
        pts = [(10,0),(-2,-5),(0,0),(-2,5)]
        s = 5.
        pts = [(x*s,y*s) for x,y in pts]
        Polygon.__init__(self, name = 'RocektBody', points = pts)

        self.thrustAcceleration = 10
        self.rotationSpeed = pi / 16.

        # flags
        self.rotateLeft = False
        self.rotateRight = False
        self.thrust = False
        self.shoot = False


    def applyThrust(self):
        self.applyAcceleration(self.thrustAcceleration, self.rotTheta)

    def stopThrust(self):
        self.aX = 0
        self.aY = 0

    def rotateCW(self):
        self.rotTheta -= self.rotationSpeed
        
    def rotateCCW(self):
        self.rotTheta += self.rotationSpeed

    def fire(self):
        # TBF: start from tip of RocketBody
        return Bullet('bullet', self.x, self.y, self.rotTheta)

    #def collision(self, circle):
    #    d = self.getDistanceFrom(circle)
    #    return d < self.collisionRadius + circle.radius

    def update(self):

        if self.rotateRight:
            self.rotateCCW()
        if self.rotateLeft:
            self.rotateCW()
        if self.thrust:
            print "thrust!"
            self.applyThrust()
        else:
            self.stopThrust()

        #if fire:
        #    print "fire!"
        #    fire = 0
        #    b = BulletShape('b%d' % len(bullets), ship.x, ship.y, ship.rotTheta)
        #    b.x = ship.x
        #    b.y = ship.y
        
        Polygon.update(self)

            
