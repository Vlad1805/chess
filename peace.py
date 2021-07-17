from board import *

board = Board()

class Piece():
    def __init__(self, color, img, x, y):
        self.color = color
        self.img = img
        self.x = x
        self.y = y
    def coord(self):
        return (self.x * 90, self.y * 90)

class Pawn(Piece):
    def __init__(self, color, img, x, y, firstMove):
        super().__init__(color, img, x, y)
        self.firstMove = 1
    def longMove(self):
        if self.firstMove == 1:
            if self.color == 'white':
                self.y -= 2
                self.firstMove = 0
            else:
                self.y += 2
                self.firstMove = 0
    def move(self):
        if self.color == 'white':
            self.y -= 1
        else:
            self.y += 1
    def onClick(self):
        pass


class Bishop(Piece):
    pass

class Knight(Piece):
    pass

class Rook(Piece):
    pass

class Queen(Piece):
    pass

class King(Piece):
    pass