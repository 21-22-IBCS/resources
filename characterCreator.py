from graphics import*
from Button import*

def main():

    win = GraphWin("Character Creator", 800, 600)

    l = Line(Point(0,0),Point(400,300))
    l.draw(win)

    c = Circle(Point(200,400),120)
    c.draw(win)

    o = Oval(Point(550,400),Point(650,450))
    o.draw(win)

    r = Rectangle(Point(550,400),Point(650,450))
    r.draw(win)
    r.setFill("red")

    p = Polygon(Point(200,0),Point(250, 50), Point(150,120))
    p.draw(win)

    li = []
    for i in range(5):
        li.append(Point(300 + i*50, 200 - i*50))
                  
    p2 = Polygon(li)
    p2.draw(win)


if __name__ == "__main__":
    main()
