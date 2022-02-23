from graphics1 import *
from Button import *
from shark import *
from fish import *
import time
import random

def main():

    win = GraphWin("Shark Simulator", 800, 600)
 
    for i in range(21):
    
        p1 = Point(100 + i*20, 100)
        p2 = Point(100 + i*20, 500)
        l = Line(p1, p2)
        l.draw(win)

    for i in range(21):
        
        p1 = Point(100, 100 + i*20)
        p2 = Point(500, 100 + i*20)
        l = Line(p1, p2)
        l.draw(win)

    step = Button(win, "cyan", "Move", Point(620, 240), 40)
    quitB = Button(win, "red", "Quit", Point(620, 440), 40)
    run = Button(win, "grey", "Run", Point(620, 340), 40)
    goAgain = Button(win, "grey", "Reset", Point(620, 140), 40)

    positions = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    s = Shark(win, random.choice(positions), random.choice(positions))
    f = Fish(win, random.choice(positions), random.choice(positions))
    f2 = Fish(win, random.choice(positions), random.choice(positions))
    f3 = Fish(win, random.choice(positions), random.choice(positions))
    
    while True:
        m1 = win.getMouse()

        if quitB.isClicked(m1):
            win.close()
            break

        if goAgain.isClicked(m1):
            newSx = random.choice(positions)
            newSy = random.choice(positions)
            newFx = random.choice(positions)
            newFy = random.choice(positions)
            newF2x = random.choice(positions)
            newF2y = random.choice(positions)
            newF3x = random.choice(positions)
            newF3y = random.choice(positions)

            s.redraw(newSx - s.pos[0], newSy - s.pos[1])
            f.draw(win, newFx, newFy)
            f2.draw(win, newF2x, newF2y)
            f3.draw(win, newF3x, newF3y)
            
            s.changePos(newSx, newSy)
            f.changePos(newFx, newFy)
            f2.changePos(newF2x, newF2y)
            f3.changePos(newF3x, newF3y)
            f.isEaten = False
            f2.isEaten = False
            f3.isEaten = False
        
        if run.isClicked(m1):
            while True:

                s.move(f.pos, f2.pos, f3.pos)
                if s.pos == f.pos:
                    f.getEaten()
                if s.pos == f2.pos:
                    f2.getEaten()
                if s.pos == f3.pos:
                    f3.getEaten()
                else:
                    f.move(s.pos)
                    f2.move(s.pos)
                    f3.move(s.pos)

                if f.isEaten and f2.isEaten and f3.isEaten:
                    break
                time.sleep(.25)
            
        if step.isClicked(m1):
            s.move(f.pos, f2.pos, f3.pos)
            if s.pos == f.pos:
                f.getEaten()
            if s.pos == f2.pos:
                f2.getEaten()
            if s.pos == f3.pos:
                f3.getEaten()
            else:
                f.move(s.pos)
                f2.move(s.pos)
                f3.move(s.pos)

        
    

if __name__ == "__main__":
    main()
