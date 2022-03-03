from graphics import*
import time

class Flower():

    def __init__(self, win, p):
        self.p = p
        self.win = win
        self.im = Image(p, "flower.gif")
        self.im2 = Image(p, "pollinated.png")
        self.im3 = Image(p, "bud.gif")
        self.im.draw(win)
        self.pollenCount = 2

    def getPos(self):
        return self.p

    def isOpen(self):
        if self.pollenCount > 0:
            return True
        else:
            return False

    def pollinated(self):
        self.im.undraw()
        self.im2.draw(self.win)
        time.sleep(0.35)
        self.im2.undraw()
        self.im.draw(self.win)
        
        self.pollenCount = self.pollenCount - 1
        if self.pollenCount == 0:
            self.finish()

    def finish(self):
        self.im.undraw()
        self.im3.draw(self.win)

    
