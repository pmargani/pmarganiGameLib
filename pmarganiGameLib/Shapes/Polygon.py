from math import cos, sin, pi

from Object2D import Object2D

class Polygon(Object2D):

    def __init__(self, name = None, x0 = 0, y0 = 0, points = []):

        Object2D.__init__(self, name, x0, y0)

        # describe polygon around origin
        # these change with rotation
        self.points = points

        # these don't change
        self.originalPnts = points

        # the angel from the x-axis we rotate our points
        self.rotTheta = 0

        pts = []
        for x, y in points:
            pts.append(x)
            pts.append(y)
        self.radius = max(pts)

    def update(self):
        Object2D.update(self)
        self.rotate(self.rotTheta)

    def rotatePoint(self, pt, theta):
        x, y = pt
        xx = x * cos(theta) - y * sin(theta)
        yy = y * cos(theta) + x * sin(theta)
        return (xx, yy)

    def rotate(self, theta):
        self.points = [self.rotatePoint(p, theta) for p in self.originalPnts]

    def getOffsetPnts(self):
        return [(self.x + xx, self.y + yy) for xx, yy in self.points]

    def pointInsideRect(self, pt, rect):
        x, y = pt
        x0, y0, w, h = rect
        x1 = x0 + w
        y1 = y0 + h

        return (x >= x0 and x <= x1) and \
               (y >= y0 and y <= y1)

    def allInsideRect(self, rect):
        for pt in self.getOffsetPnts(): 
            if not self.pointInsideRect(pt, rect):
                return False
        return True

    def allOutsideRect(self, rect):
        for pt in self.getOffsetPnts(): 
            if self.pointInsideRect(pt, rect):
                return False
        return True

    def offScreen(self, screenWidth, screenHeight):
        return self.allOutsideRect((0,0,screenWidth, screenHeight))

    def posInScreen(self, screen, pos):
        return pos >= 0 and pos <= screen

    def shipInY(self, screenHeight):
        return self.posInScreen(screenHeight, self.y)

    def shipInX(self, screenWidth):
        return self.posInScreen(screenWidth, self.x)

    def wrapAroundY(self, screenHeight):
        if not self.shipInY(screenHeight):
            if self.y < 0:
                self.y = screenHeight
            if self.y > screenHeight:
                self.y = 0
 
    def wrapAroundX(self, screenWidth):
        if not self.shipInX(screenWidth):
            if self.x < 0:
                self.x = screenWidth
            if self.x > screenWidth:
                self.x = 0
 
    def wrapAround(self, screenWidth, screenHeight):
        self.wrapAroundY(screenHeight)
        self.wrapAroundX(screenWidth)

    def collision(self, polygon):
        d = self.getDistanceFrom(polygon)
        return d < (self.radius + polygon.radius)
    
if __name__ == '__main__':
    
    pts = [(-1,1),(1,1),(1,-1),(-1,-1)]
    s = 10.
    pts = [(x*s, y*s) for x, y in pts]
    p = Polygon(points = pts)

    print "original: "
    p.update()
    print p, p.points

    print "rotate 45 degrees"
    p.rotTheta = pi / 4.0
    p.update()
    print p, p.points
        
    print "in rect?"
    p.rotTheta = 0
    p.update()
    rect = (400,400,10,10)
    print p.allInsideRect(rect), p.allOutsideRect(rect)

    rect = (-20,-20,40,40)
    print p.allInsideRect(rect), p.allOutsideRect(rect)
        
    # move it
    p.vX = 50
    p.update()

    print "should have moved in x direction: "
    print p, p.getOffsetPnts()
