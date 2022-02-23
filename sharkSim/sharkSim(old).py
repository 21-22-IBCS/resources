from graphics1 import *
from Button import *
from shark import *
from fish import *
import time
import random

def main():

#name the window and size it
    win = GraphWin("Shark Simulator", 800, 600)

 #draw the grid lines - separate loops for x and y
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

#all the buttons in one place
#one to move, one to quit, one to run the simulation and one to reset and reposition the
#shark and fish

    step = Button(win, "cyan", "Move", Point(620, 240), 40)
    quitB = Button(win, "red", "Quit", Point(620, 440), 40)
    run = Button(win, "grey", "Run", Point(620, 340), 40)
    goAgain = Button(win, "grey", "Reset", Point(620, 140), 40)

#this is so that the starting positions can be random
#positions is a list of all the possible 'coordinates'
#s, f, and f2 use shark and fish to generate the points and draw the images in the window
    positions = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    s = Shark(win, random.choice(positions), random.choice(positions))
    f = Fish(win, random.choice(positions), random.choice(positions))
    f2 = Fish(win, random.choice(positions), random.choice(positions))


    while True:
#make the buttons clickable!
        m1 = win.getMouse()

#when the quit button is clicked, it'll close and end the program
        if quitB.isClicked(m1):
            win.close()
            break

#when the reset button is clicked, it'll generate new points for the shark and fishes
        if goAgain.isClicked(m1):
            newSx = random.choice(positions)
            newSy = random.choice(positions)
            newFx = random.choice(positions)
            newFy = random.choice(positions)
            newF2x = random.choice(positions)
            newF2y = random.choice(positions)

#then it'll redraw the new images in their new positions
            s.redraw(newSx - s.pos[0], newSy - s.pos[1])
            f.draw(win, newFx, newFy)
            f2.draw(win, newF2x, newF2y)
            s.changePos(newSx, newSy)
            f.changePos(newFx, newFy)
            f2.changePos(newF2x, newF2y)

#when the run button is clicked, it'll start the program (moving in relation to each other)
#get eaten when they are in the same square
        if run.isClicked(m1):
            while True:
                s.move(f.pos)
                if s.pos == f.pos:
                    f.getEaten()
                    break
#continue moving and use time to slow it down until the shark and fish intersect
                else:
                    f.move(s.pos)
                    f2.move(s.pos)
                time.sleep(.25)

#when the move button is clicked, only move once, rather than continuously
        if step.isClicked(m1):
            s.move(f.pos)
            if s.pos == f.pos:
                f.getEaten()
            else:
                f.move(s.pos)
                f2.move(s.pos)

        
    

if __name__ == "__main__":
    main()
