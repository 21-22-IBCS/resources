from graphics import*
import random
import time

class Bee():

    def __init__(self, win, p):
        self.p = p
        self.win = win
        self.im = Image(p, "bee.gif")
        self.im.draw(win)
        self.pollenCount = 0
        self.pollenThreshold = 10
        self.there = True

    def refresh(self):
        self.im.undraw()
        self.im.draw(self.win)

    def moveB(self):
        while True:
            randXdir = random.choice([1,-1])
            randYdir = random.choice([1,-1])
            randX = random.randint(7,25)
            randY = random.randint(7,25)
            x = self.p.getX() + randXdir*randX
            y = self.p.getY() + randYdir*randY
            if 110 < x < 610:
                if 110 < y < 460:
                    break
        self.p.move(randXdir*randX, randYdir*randY)
        self.im.move(randXdir*randX, randYdir*randY)

    def pollinate(self):
        self.pollenCount += 1
        self.flyAway()

    def checkPollinate(self, flowers):
        for i in range(len(flowers)):
            if flowers[i].isOpen():
                x = flowers[i].getPos().getX()
                y = flowers[i].getPos().getY()
                minX = x - 12
                maxX = x + 12
                minY = y - 12
                maxY = y + 12
            
                if maxX > self.p.getX() > minX:
                    if maxY > self.p.getY() > minY:
                        return i
        return len(flowers)

    def flyAway(self):
        if self.pollenCount > 4:
            for i in range(5, 100, 5):
                time.sleep(0.05)
                self.p.move(i, -i)
                self.im.move(i, -i)
            self.im.undraw()
            self.there = False
                

    
