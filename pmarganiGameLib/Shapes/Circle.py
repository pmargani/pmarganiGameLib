from Object2D import Object2D
from math import cos, sin

class Circle(Object2D):

    def __init__(self, name, radius, color, xpos = None, ypos = None):
        Object2D.__init__(self, name = name, x0 = xpos, y0 = ypos)
        self.radius = radius
        self.color = color
        
        #self.speed = 5 # pixels / frame
        #self.theta = 0 # angle w/ x-axis; radians

    def __str__(self):
        return "%s: (%d, %d) r: %d" % (self.name, self.x, self.y, self.radius)

    def offScreen(self, width, height):
        maxExt = self.radius
        x = self.x
        y = self.y

        if x - maxExt > width or \
           x + maxExt < 0 or \
           y - maxExt > height or \
           y + maxExt < 0:
           return True
        else:
           return False

    def wrapAroundSide(self, maxLen, pos):
        newpos = pos
        if pos > maxLen:
            newpos = 0
        if pos < 0:
            newpos = maxLen
        return newpos

    def wrapAround(self, screenWidth, screenHeight):
        self.x = self.wrapAroundSide(screenWidth, self.x)
        self.y = self.wrapAroundSide(screenHeight, self.y)

    def collision(self, circle):
        d = self.getDistanceFrom(circle)
        return d < (self.radius + circle.radius)

if __name__ == '__main__':
    c = Circle('a', 3, (0,0,0), 0, 0)
    print c.x, c.y
    c.update()
    print c.x, c.y
    c.theta = 3.147 / 2.
    c.update()
    print c.x, c.y
    c.wrapAround(200,200)

