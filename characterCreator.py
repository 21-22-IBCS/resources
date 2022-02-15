from graphics import*
from Button import*


def main():

    win = GraphWin("Character Creator", 600, 600)

    face = Oval(Point(200,100), Point(400,450))
    face.draw(win)

    nose = Polygon([Point(300, 200), Point(350, 280), Point(250, 280)])
    #nose.draw(win)
    nose2 = Circle(Point(300,250),20)
    nose2.setFill('red')

    noseButton = Button(win, 'cyan', 'Large Nose', Point(200, 500), 70)

    nose2Button = Button(win, 'yellow', 'Button Nose', Point(100, 500),60)
    
    quitButton = Button(win, 'red', "Quit", Point(500, 520), 60)

    while True:

        m1 = win.getMouse()
        
    
        if quitButton.isClicked(m1):
            break

        if noseButton.isClicked(m1):
            nose2.undraw()
            nose.undraw()
            nose.draw(win)

        if nose2Button.isClicked(m1):
            nose.undraw()
            nose2.undraw()
            nose2.draw(win)

    win.close()

if __name__ == "__main__":
    main()




