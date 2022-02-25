from graphics import*
from Button import*
from flower import*
import math
import time

'''This spring simulation is designed to show how plants, like
the Rhododendron are pollinated. Each plant will have flower buds which will
randomly bloom. Once pollinated by bees, the flower with close.'''

def main():

    win = GraphWin("Spring Simulation 2022", 1000, 600)
    quiB = Button(win, "grey", "Quit", Point(920,200), 50)
    bloomB = Button(win, "cyan", "Bloom", Point(920,100),50)

    background = Image(Point(400,350), "rhodo.gif") #photo from plantopedia.com
    background.draw(win)

    sampleBee = Image(Point(700,400), "bee.gif") #photo from bamboozle.com
    sampleBee.draw(win)

    '''sampleFlower = Image(Point(400,300), "flower.gif") #photo from unsplash.com (user hsvrs)
    sampleFlower.draw(win)

    sampleBud = Image(Point(300,300), "bud.gif") #photo from subpng.com
    sampleBud.draw(win)'''

    f1 = Flower(win, Point(300,350))
    f2 = Flower(win, Point(200,250))
    f3 = Flower(win, Point(400,550))
    
    while True:
        m = win.getMouse()
        if quiB.isClicked(m):
            win.close()
            break

        if bloomB.isClicked(m):
            f1.bloom()
            f2.bloom()
            f3.bloom()
        



if __name__ == "__main__":
    main()
