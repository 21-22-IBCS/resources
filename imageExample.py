from graphics import*
from Button import*

def darken(cats):
    for i in range(500):
        for j in range(451):
            pix = cats.getPixel(i, j)
            r, g, b = pix[0] - 20, pix[1] - 20, pix[2] - 20
            if r < 0:
                r = 0
            if g < 0:
                g = 0
            if b < 0:
                b = 0
            cats.setPixel(i, j, color_rgb(r,g,b))

















def main():

    win = GraphWin("Image Editor", 800, 600)
    sh = Button(win, "white", "Show", Point(150, 40), 45)
    hi = Button(win, "white", "Hide", Point(300, 40), 45)
    close = Button(win, "grey", "Quit", Point(150, 560), 45)
    bright = Button(win, "white", "Brighten", Point(720, 50), 45)
    dark = Button(win, "white", "Darken", Point(720, 150), 45)
    blur = Button(win, "white", "Blur", Point(720, 250), 45)
    cont = Button(win, "white", "Contrast", Point(720, 350), 45)
    filt = Button(win, "white", "Filter", Point(720, 450), 45)

    cats = Image(Point(400,300), "Cats.png")

    m = win.getMouse()
    while True:
        if close.isClicked(m):
            break
        if sh.isClicked(m):
            cats.undraw()
            cats.draw(win)
        if hi.isClicked(m):
            cats.undraw()
        if dark.isClicked(m):
            darken(cats)
        m = win.getMouse()

    win.close()
    
if __name__ == "__main__":
    main()
