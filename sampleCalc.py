from graphics import*
from Button import*
from math import*

def calcy(f, num):
    if "sqrt(x)" in f:
        return sqrt(num)
    elif "x^2" in f:
        return num**2
    elif "sin(x)" in f:
        return sin(num)
    elif "e^x" in f:
        return e**num
    elif "cos(x)" in f:
        return cos(num)
    else:
        return num

def main():

    win = GraphWin("calc",800,800)
    title = Text(Point(400,50), "Welcome to the Graphing Calculator")
    title.setSize(32)
    title2 = Text(Point(400,110), "Enter a function you would like to graph")
    title2.setSize(20)
    title.draw(win)
    title2.draw(win)

    yAxis = Line(Point(150,200), Point(150,650))
    yAxis.draw(win)
    xAxis = Line(Point(150,500), Point(650,500))
    xAxis.draw(win)

    funText = Text(Point(200,650), "Y  =  ")
    funText.setSize(24)
    funText.draw(win)

    fun = Entry(Point(340,650),30)
    fun.draw(win)

    graph = Button(win, 'white', "GRAPH", Point(550,650), 75)
    quitB = Button(win, 'red', "QUIT", Point(400,720), 50)

    while True:
        m1 = win.getMouse()
        if graph.isClicked(m1):
            f = fun.getText()

            scale = 50

            points = []
            for i in range(500):
                x = i + 150
                y = 500 - scale*calcy(f,i/scale)
                points.append(Point(x,y))

            for p in points:
                p.draw(win)

        if quitB.isClicked(m1):
            win.close()
            break
                
    

if __name__ == "__main__":
    main()
