#from board import *

#board = Board([])

class Piece():
    def __init__(self, color, img, x, y):
        self.color = color
        self.img = img
        self.x = x
        self.y = y
    def coord(self):
        return (self.x * 90, self.y * 90)
    def click(self, pos):
        coord = self.coord()
        if coord[0] < pos[0] and coord[0] + 90 > pos[0]:
            if coord[1] < pos[1] and coord[1] + 90 > pos[1]:
                return True
        return False

class Pawn(Piece):
    def __init__(self, color, img, x, y, firstMove):
        super().__init__(color, img, x, y)
        self.firstMove = firstMove
    def longMove(self):
        if self.firstMove == 1:
            if self.color == 'white':
                self.y -= 2
                self.firstMove = 0
            else:
                self.y += 2
                self.firstMove = 0
    def move(self, pos, moves):
        p = [int(pos[0] / 90), int(pos[1] / 90)]
        if p in moves:
            self.x = p[0]
            self.y = p[1]
            self.firstMove = 0
        print(p)
        print(moves)
    def onClick(self):
        moves = []
        if self.color == 'white':
            moves.append([self.x, self.y - 1])
            if self.firstMove == 1:
                moves.append([self.x, self.y - 2])
        else:
            moves.append([self.x, self.y + 1])
            if self.firstMove == 1:
                moves.append([self.x, self.y + 2])
        return moves


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