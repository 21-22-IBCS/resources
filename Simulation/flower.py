from graphics import*

class Flower():

    def __init__(self, win, p):
        self.p = p
        self.win = win
        self.im = Image(p, "flower.gif")
        self.im.draw(win)
        self.pollenCount = 1

    def getPos(self):
        return self.p

    def isOpen(self):
        if self.pollenCount > 0:
            return True
        else:
            return False

    def pollinated(self):
        self.pollenCount = self.pollenCount - 1
        if self.pollenCount == 0:
            self.finish()

    def finish(self):
        self.im.undraw()
        self.im = Image(self.p, "bud.gif")
        self.im.draw(self.win)

    
