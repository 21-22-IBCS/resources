from graphics import*
import time

class Flower():

    def __init__(self, win, p):
        self.p = p
        self.win = win
        self.im = Image(p, "flower.gif")
        self.im.draw(win)

    def getPos(self):
        return self.p
