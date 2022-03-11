from graphics import*
#Button edited to create squares (to fit the board)
from Button import*
from Piece import*

class OthelloBoard():

    def __init__(self, win):
        self.win = win
        
        #matrix of buttons in (column, row) format
        self.cells = []
        for i in range(8):
            rows = []
            for j in range(8):
                rows.append(Button(win, "green", "", Point(i*50 + 100, j*50 + 100), 25))
            self.cells.append(rows)

        #determines black or white
        self.turnCount = 0

        #store all pieces on the board
        self.pieces = []

    #set up the board to start a game
    def initial(self):
        p0 = Piece(self.win, 3, 3)
        p1 = Piece(self.win, 4, 4)
        p2 = Piece(self.win, 3, 4)
        p3 = Piece(self.win, 4, 3)

        #two of the pieces are black
        p2.change()
        p3.change()
        self.pieces = [p0,p1,p2,p3]

    #play a piece on the board given space clicked on board
    #(c, r) = (column, row) of space / "button" clicked
    def play(self, c, r):

        #assume it is a fair place to put a piece
        valid = True
        for piece in self.pieces:
            #if space is already taken by another piece. it is not valid
            if piece.getPos() == [c, r]:
                valid = False

        #only create the new piece if it is valid
        if valid:
            p = Piece(self.win, c, r)
            #alternate placing black/white piece based on the turn count
            if self.turnCount%2 == 0:
                p.change()
                
            self.pieces.append(p)
            self.turnCount += 1
