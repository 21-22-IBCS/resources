from graphics1 import *

class Shark():

    def __init__(self, win, x, y):

        self.x = x
        self.y = y
        self.pos = (x, y)
        self.start = Point(110 + x*20, 110 + y*20)
        self.image = Image(self.start, "sharkImage.gif")
        self.image.draw(win)

    def changePos(self, x, y):
        self.pos = (x, y)
    
    def redraw(self, cX, cY):
        self.image.move(cX*20, cY*20)
        
    #Rules for shark movement:
    #Can move diagonally and up to 2 squares
        
    def move(self, f1pos, f2pos, f3pos):
        
        x = self.pos[0]
        y = self.pos[1]

        f1X = f1pos[0]
        f1Y = f1pos[1]
        f2X = f2pos[0]
        f2Y = f2pos[1]
        f3X = f3pos[0]
        f3Y = f3pos[1]
        fList = []
        fList.append((f1X, f1Y))
        fList.append((f2X, f2Y))
        fList.append((f3X, f3Y))

        fDistances = []
        fDistances.append(abs(x - f1X) + abs(y - f1Y))
        fDistances.append(abs(x - f2X) + abs(y - f2Y))
        fDistances.append(abs(x - f3X) + abs(y - f3Y))

        minDist = 1000
        fX = 0
        fY = 0
        for i in range(3):
            if fDistances[i] < minDist:
                minDist = fDistances[i]
                fX = fList[i][0]
                fY = fList[i][1]
        
        #create a list to hold all of the potential movements
        potentialMove = []
        potentialMove.append((x, y - 1))
        potentialMove.append((x, y - 2))
        potentialMove.append((x, y + 1))
        potentialMove.append((x, y + 2))
        potentialMove.append((x, y))
        potentialMove.append((x + 1, y - 1))
        potentialMove.append((x + 1, y - 2))
        potentialMove.append((x + 1, y + 1))
        potentialMove.append((x + 1, y + 2))
        potentialMove.append((x + 1, y))
        potentialMove.append((x + 2, y - 1))
        potentialMove.append((x + 2, y + 1))
        potentialMove.append((x + 2, y))
        potentialMove.append((x - 1, y - 1))
        potentialMove.append((x - 1, y - 2))
        potentialMove.append((x - 1, y + 1))
        potentialMove.append((x - 1, y + 2))
        potentialMove.append((x - 1, y))
        potentialMove.append((x - 2, y - 1))
        potentialMove.append((x - 2, y + 1))
        potentialMove.append((x - 2, y))

        #check to see if any of the movements would go "off the grid"
        for m in potentialMove:
            if m[0] > 19 or m[0] < 0 or m[1] > 19 or m[1] < 0:
                potentialMove[potentialMove.index(m)] = (x, y)

        #create a list for all calculated distances
        distances = []

        #calculate all distances between potential movements and the fish position
        for m in potentialMove:
            diff = abs(fX - m[0]) + abs(fY - m[1])
            distances.append(diff)

        #evaluate which of the distances is the shortest
        minDist = 1000
        theMove = 0
        for dis in distances:
            if dis < minDist:
                minDist = dis
                theMove = distances.index(dis)

        #determine how far to move the shark image
        changeX = potentialMove[theMove][0] - x
        changeY = potentialMove[theMove][1] - y

        #change the position of the shark and the image
        self.pos = potentialMove[theMove]
        self.redraw(changeX, changeY)

        
        
                
        
        
    










