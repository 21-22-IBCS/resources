from graphics import*

class Flower():

    def __init__(self, win, p):
        self.p = p
        self.win = win
        self.im = Image(p, "bud.gif")
        self.im.draw(win)

    def bloom(self):
        self.im.undraw()
        self.im = Image(self.p, "flower.gif")
        self.im.draw(self.win)

    
