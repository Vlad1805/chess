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
    def move(self, pos, moves, board):
        p = [int(pos[0] / 90), int(pos[1] / 90)]
        if p in moves:
            if (p[0], p[1]) in board.keys():
                del board[(p[0], p[1])]
            board[(p[0], p[1])] = board.pop((self.x, self.y))
            self.x = p[0]
            self.y = p[1]
            if isinstance(self, Pawn):
                self.firstMove = 0
                if self.y == 0:
                    return True
                if self.y == 7:
                    return True
        return False

class Pawn(Piece):
    def __init__(self, color, img, x, y, firstMove):
        super().__init__(color, img, x, y)
        self.firstMove = firstMove
    def onClick(self, board):
        moves = []
        if self.color == 'white':
            if (self.x, self.y - 1) not in board:
                moves.append([self.x, self.y - 1])
                if self.firstMove == 1 and (self.x, self.y - 2) not in board:
                    moves.append([self.x, self.y - 2])    
            if (self.x - 1, self.y - 1) in board.keys() and board[(self.x-1,self.y-1)].color == 'black':
                moves.append([self.x - 1, self.y - 1])
            if (self.x + 1, self.y - 1) in board.keys() and board[(self.x+1,self.y-1)].color == 'black':
                moves.append([self.x + 1, self.y - 1])
        else:
            if (self.x, self.y + 1) not in board:
                moves.append([self.x, self.y + 1])
                if self.firstMove == 1 and (self.x, self.y + 2) not in board:
                    moves.append([self.x, self.y + 2])
            if (self.x - 1, self.y + 1) in board.keys() and board[(self.x-1,self.y+1)].color == 'white':
                moves.append([self.x - 1, self.y + 1])
            if (self.x + 1, self.y + 1) in board.keys() and board[(self.x+1,self.y+1)].color == 'white':
                moves.append([self.x + 1, self.y + 1])
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