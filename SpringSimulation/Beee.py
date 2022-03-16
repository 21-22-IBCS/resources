from graphics import*
import random

class Beee():

    
    def __init__(self, win, p):
        #image taken from bamboozle.com
        self.im = Image(p,"Bee.gif")
        self.im.draw(win)
        self.pos = p

    def fly(self):

        xDir = random.choice([-1,0,1])
        yDir = random.choice([-1,0,1])

        self.pos.move(20*xDir, 20*yDir)
        self.im.move(20*xDir, 20*yDir)

    def checkFlower(self, fpoint):
        x = self.pos.getX()
        y = self.pos.getY()
        xMin = fpoint.getX() - 10
        yMin = fpoint.getY() - 10
        xMax = fpoint.getX() + 10
        yMax = fpoint.getY() + 10
        if x > xMin:
            if y > yMin:
                if x < xMax:
                    if y < yMax:
                        #we found the flower!
                        self.disappear()
                        return True
        return False

    def disappear(self):
        self.im.undraw()
        self.pos = Point(-1000, -1000)








        
        

