from graphics import*
from Beee import*
import time
from Flower import*

def main():

    win = GraphWin("simulation", 800, 600)
    b = Beee(win, Point(400,300))
    b2 = Beee(win, Point(450,200))
    b3 = Beee(win, Point(400,200))
    b4 = Beee(win, Point(400,300))
    f = Flower(win, Point(400,300))
    for i in range(200):
        time.sleep(.01)
        b.fly()
        b2.fly()
        b3.fly()
        b4.fly()
        #interaction checked here
        if b.checkFlower(f.getPos()):
            print("Found a flower!")
        if b2.checkFlower(f.getPos()):
            print("Found a flower!")
        if b3.checkFlower(f.getPos()):
            print("Found a flower!")
        if b4.checkFlower(f.getPos()):
            print("Found a flower!")
            
    

if __name__ == "__main__":
    main()
