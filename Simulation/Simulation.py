from graphics import*
from Button import*
from flower import*
from Bee import*
import random
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

    '''sampleBee = Image(Point(700,400), "bee.gif") #photo from bamboozle.com
    sampleBee.draw(win)

    sampleFlower = Image(Point(400,300), "flower.gif") #photo from unsplash.com (user hsvrs)
    sampleFlower.draw(win)

    sampleBud = Image(Point(300,300), "bud.gif") #photo from subpng.com
    sampleBud.draw(win)'''

    flowers = []
    #pointList = generatePoints()
    for i in range(30):
        flowers.append(Flower(win, Point(random.randint(100,600),random.randint(100,400))))

    b1 = Bee(win, Point(300,450))
    b2 = Bee(win, Point(150,150))
    b3 = Bee(win, Point(300,150))
    bees = [b1, b2, b3]
    
    while True:
        m = win.getMouse()
        if quiB.isClicked(m):
            win.close()
            break

        if bloomB.isClicked(m):
            while True:
                for b in bees:
                    time.sleep(.05)
                    b.moveB()
                    flow = b.checkPollinate(flowers)
                    if flow < len(flowers):
                        flowers[flow].pollinated()
                        b.pollinate()

                done = True
                for b in bees:
                    if b.there:
                        done = False
                if done:
                    break



if __name__ == "__main__":
    main()
