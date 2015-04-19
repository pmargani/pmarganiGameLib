import random
from math import pi

#from Shape import Shape
#from Circle import Circle
#from Ship import ShipBody
from RocketBody import RocketBody
from Explosion import Explosion
from BulletShape import BulletShape
from AsteroidShape import AsteroidShape
class GameState:

    def __init__(self):
        self.inPlay = False
        self.win = False

class AsteroidsGame:

    """
    This is the high level class for Asteroids.
    """

    def __init__(self, screenWidth = None, screenHeight = None):

        self.state = GameState()

        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        self.initObjects()

        self.verbose = True
 
    def initObjects(self):
        "Init all stuff drawn on the screen"

        self.initShip()
        self.initAsteroids()
        self.bullets = []
        self.explosions = []
        self.initStars()

    def initShip(self):
        "Start player's ship in center of screen"
        x0 = self.screenWidth // 2
        y0 = self.screenHeight // 2
        self.ship = RocketBody()
        self.ship.x = x0
        self.ship.y = y0

    def initStars(self):
        "Randomly placed stars make a cool background"

        self.numStars = random.randint(200,250)
        self.stars = []
        for i in range(self.numStars):
            x = random.randint(0, self.screenWidth)
            y = random.randint(0, self.screenHeight)
            self.stars.append((x,y))

    def initAsteroids(self):
        "Randomly place asteroids in screen"

        # create random asteroids
        # TBF: not too close to ship!
        self.numAsts = random.randint(3,10)
        self.asteroids = []
        for i in range(self.numAsts):
            x = random.randint(0, self.screenWidth)
            y = random.randint(0, self.screenHeight)
            theta = (2*pi/360.) * random.randint(0, 360)
            a = AsteroidShape('a%d' % i, x, y, theta)
            a.x = x
            a.y = y
            a.rotDir = random.randint(-1,1)
            self.asteroids.append(a)

    def update(self):
        "Handle obj interactions, and update each obj."

        if self.verbose: print "Game.update"

        wH = self.screenHeight
        wW = self.screenWidth

        # screen issues
        if self.ship.offScreen(wW, wH):
            self.ship.wrapAround(wW, wH)
        for a in self.asteroids:
            if a.offScreen(wW, wH):
                a.wrapAround(wW, wH)
        for i, b in enumerate(self.bullets):
            if b.offScreen(wW, wH):
                self.bullets.pop(i)

        # explosions done?
        for ei, e in enumerate(self.explosions):
            if e.isDone():
                print "explosion done"
                self.explosions.pop(ei)

        # collision detection
        for bi, b in enumerate(self.bullets):
            for ai, a in enumerate(self.asteroids):
                if b.collision(a):
                    print "collision: ", b, a
                    # replace both
                    self.asteroids.pop(ai)
                    self.bullets.pop(bi)
                    # with an explosion
                    self.explosions.append(Explosion(a.x, a.y))

        # did we just kill all asteroids?
        if len(self.asteroids) == 0:
            self.state.inPlay = False
            self.state.win = True
        # or did asteroids kill us?
        for a in self.asteroids:
            if self.ship.collision(a):
                print "collision with ship!"
                self.state.inPlay = False
                self.state.win = False
                self.explosions.append(Explosion(self.ship.x, self.ship.y))
    
        # pass on the call to update
        self.ship.update()
        for b in self.bullets:
            b.update()
        for a in self.asteroids:
            a.update()
        for e in self.explosions:
            e.update()


def main():

    g = Game(1000, 1000)
    for i in range(100):
        g.update()
            
if __name__ == '__main__':
    main()

        
