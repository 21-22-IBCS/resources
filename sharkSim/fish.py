from graphics1 import *
import random

class Fish():

    def __init__(self, win, x, y):

        self.x = x
        self.y = y
        self.pos = (x, y)
        self.isEaten = False
        self.start = Point(110 + x*20, 110 + y*20)
        self.image = Image(self.start, "bitFish.gif")
        self.image.draw(win)

    def changePos(self, x, y):
        self.pos = (x, y)

    def draw(self, win, x, y):
        self.image.undraw()
        self.image = Image(Point(110 + x*20, 110 + y*20), "bitFish.gif")
        self.image.draw(win)
    
    def redraw(self, cX, cY):
        self.image.move(cX*20, cY*20)

    def getEaten(self):
        self.redraw(10000,10000)
        self.pos = (10000,10000)
        self.isEaten = True

    def moveLR(self, x, y):
        potentialMove = []
        potentialMove.append((x + 1, y))
        potentialMove.append((x - 1, y))
        potentialMove.append((x, y + 1))
        potentialMove.append((x, y - 1))
        
        for m in potentialMove:
            if m[0] > 19 or m[0] < 0 or m[1] > 19 or m[1] < 0:
                potentialMove[potentialMove.index(m)] = (x, y)
                
        self.pos = random.choice(potentialMove)
        newX = self.pos[0]
        newY = self.pos[1]
        self.redraw(newX - x, newY - y)
        

    def move(self, spos):

        potentialMove = []
        
        x = self.pos[0]
        y = self.pos[1]
        sX = spos[0]
        sY = spos[1]
        
        if abs(x - sX) + abs(y-sY) > 9:
            self.moveLR(x, y)
        else:    
            potentialMove.append((x, y - 1))
            potentialMove.append((x, y + 1))
            potentialMove.append((x, y))
            potentialMove.append((x + 1, y - 1))
            potentialMove.append((x + 1, y + 1))
            potentialMove.append((x + 1, y))
            potentialMove.append((x - 1, y - 1))
            potentialMove.append((x - 1, y + 1))
            potentialMove.append((x - 1, y))

            for m in potentialMove:
                if m[0] > 19 or m[0] < 0 or m[1] > 19 or m[1] < 0:
                    potentialMove[potentialMove.index(m)] = (x, y)

            distances = []
            
            for m in potentialMove:
                diff = abs(sX - m[0]) + abs(sY - m[1])
                distances.append(diff)

            maxDist = 0
            theMove = 0
            for dis in distances:
                if dis > maxDist:
                    maxDist = dis
                    theMove = distances.index(dis)

            changeX = potentialMove[theMove][0] - x
            changeY = potentialMove[theMove][1] - y
            self.pos = potentialMove[theMove]
            self.redraw(changeX, changeY)

