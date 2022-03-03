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

def generatePoints(num, spacing):
    points = []
    space = [[0,0,0,0]]
    sf = spacing
    while True:
        x = random.randint(120,600)
        y = random.randint(120,450)

        valid = True
        for s in space:
            if (s[0] < x) and (s[1] > x):
                if (s[2] < y) and (s[3] > y):
                    valid = False
        if valid:
            points.append(Point(x,y))
            space.append([x - sf, x + sf, y - sf, y + sf])

        if len(points) == num:
            break

    return points

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
    pointList = generatePoints(40,35)
    for i in range(len(pointList)):
        flowers.append(Flower(win, pointList[i]))

    b1 = Bee(win, Point(300,420))
    b2 = Bee(win, Point(150,150))
    b3 = Bee(win, Point(300,150))
    b4 = Bee(win, Point(450,230))
    b5 = Bee(win, Point(400,400))
    bees = [b1, b2, b3, b4, b5]
    
    while True:
        m = win.getMouse()
        if quiB.isClicked(m):
            win.close()
            break

        if bloomB.isClicked(m):
            while True:
                for b in bees:
                    time.sleep(.025)
                    if b.there:
                        b.moveB()
                        flow = b.checkPollinate(flowers)
                        if flow < len(flowers):
                            flowers[flow].pollinated()
                            b.pollinate()
                        b.refresh()

                done = True
                for b in bees:
                    if b.there:
                        done = False
                if done:
                    break



if __name__ == "__main__":
    main()
