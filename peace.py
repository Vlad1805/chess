#Copyright 2021 Stanciu Vlad

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
    def onBoard(self, newPos):
        if newPos[0] >= 0 and newPos[0] <= 7 and newPos[1] >= 0 and newPos[1] <= 7:
            return True
        return False
    def move(self, pos, moves, board):
        p = [int(pos[0] / 90), int(pos[1] / 90)]
        if p in moves:
            if isinstance(self, King) and self.firstMove:
                if p == [2, 7] and self.color == 'white':
                    board[2, 7] = board.pop((self.x, self.y))
                    self.x = 2
                    board[0, 7].x = 3
                    board[3, 7] = board.pop((0, 7))
                    self.firstMove = 0
                    return False
                if p == [6, 7] and self.color == 'white':
                    board[6, 7] = board.pop((self.x, self.y))
                    self.x = 6
                    board[7, 7].x = 5
                    board[5, 7] = board.pop((7, 7))
                    self.firstMove = 0
                    return False
                if p == [2, 0] and self.color == 'black':
                    board[2, 0] = board.pop((self.x, self.y))
                    self.x = 2
                    board[0, 0].x = 3
                    board[3, 0] = board.pop((0, 0))
                    self.firstMove = 0
                    return False
                if p == [6, 0] and self.color == 'black':
                    board[6, 0] = board.pop((self.x, self.y))
                    self.x = 6
                    board[7, 0].x = 5
                    board[5, 0] = board.pop((7, 0))
                    self.firstMove = 0
                    return False

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
            if isinstance(self, Rook) or isinstance(self, King):
                self.firstMove = 0
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
    def diagonal(self, board, moves, a, b):
        pos = [self.x, self.y]
        while self.onBoard([pos[0] + a, pos[1] + b]):
            pos[0] += a
            pos[1] += b
            if (pos[0], pos[1]) in board:
                if board[(pos[0], pos[1])].color != self.color:
                    moves.append(pos[:])
                break
            moves.append(pos[:])
    def onClick(self, board):
        moves = []
        self.diagonal(board, moves, 1, 1)
        self.diagonal(board, moves, 1, -1)
        self.diagonal(board, moves, -1, 1)
        self.diagonal(board, moves, -1, -1)
        return moves


class Knight(Piece):
    def jump(self, board, moves, a, b):
        if self.onBoard([self.x + a, self.y + b]):
            if (self.x + a, self.y + b) in board:
                if board[(self.x + a, self.y + b)].color != self.color:
                    moves.append([self.x + a, self.y + b])
            else:
                moves.append([self.x + a, self.y + b])
    def onClick(self, board):
        moves = []
        self.jump(board,moves,1,2)
        self.jump(board,moves,1,-2)
        self.jump(board,moves,-1,2)
        self.jump(board,moves,-1,-2)
        self.jump(board,moves,2,1)
        self.jump(board,moves,2,-1)
        self.jump(board,moves,-2,1)
        self.jump(board,moves,-2,-1)
        return moves

class Rook(Piece):
    def __init__(self, color, img, x, y, firstMove):
        super().__init__(color, img, x, y)
        self.firstMove = firstMove
    def line(self, board, moves, a, b):
        pos = [self.x, self.y]
        while self.onBoard([pos[0] + a, pos[1] + b]):
            pos[0] += a
            pos[1] += b
            if (pos[0], pos[1]) in board:
                if board[(pos[0], pos[1])].color != self.color:
                    moves.append(pos[:])
                break
            moves.append(pos[:])
    def onClick(self, board):
        moves = []
        self.line(board, moves, 1, 0)
        self.line(board, moves, -1, 0)
        self.line(board, moves, 0, 1)
        self.line(board, moves, 0, -1)
        return moves

class Queen(Piece):
    def movement(self, board, moves, a, b):
        pos = [self.x, self.y]
        while self.onBoard([pos[0] + a, pos[1] + b]):
            pos[0] += a
            pos[1] += b
            if (pos[0], pos[1]) in board:
                if board[(pos[0], pos[1])].color != self.color:
                    moves.append(pos[:])
                break
            moves.append(pos[:])
    def onClick(self, board):
        moves = []
        self.movement(board, moves, 1, 0)
        self.movement(board, moves, -1, 0)
        self.movement(board, moves, 0, 1)
        self.movement(board, moves, 0, -1)
        self.movement(board, moves, 1, 1)
        self.movement(board, moves, 1, -1)
        self.movement(board, moves, -1, 1)
        self.movement(board, moves, -1, -1)
        return moves

class King(Piece):
    def __init__(self, color, img, x, y, firstMove):
        super().__init__(color, img, x, y)
        self.firstMove = firstMove
    def movement(self, board, moves, a, b):
        if self.onBoard([self.x + a, self.y + b]):
            if (self.x + a, self.y + b) in board:
                if board[(self.x + a, self.y + b)].color != self.color:
                    moves.append([self.x + a, self.y + b])
            else:
                moves.append([self.x + a, self.y + b])
    def onClick(self, board):
        moves = []
        self.movement(board,moves, 1, 0)
        self.movement(board,moves, 1, -1)
        self.movement(board,moves, 1, 1)
        self.movement(board,moves, 0, 1)
        self.movement(board,moves, 0, -1)
        self.movement(board, moves, -1, 0)
        self.movement(board,moves, -1, 1)
        self.movement(board,moves, -1, -1)
        if self.firstMove == 1:
            if self.color == 'white':
                if (1,7) not in board and (2,7) not in board and (3,7) not in board:
                    if (0,7) in board and board[(0, 7)].color == 'white' and isinstance(board[(0, 7)], Rook) and board[0, 7].firstMove:
                        moves.append([2,7])
                if (5,7) not in board and (6,7) not in board:
                    if (7,7) in board and board[(7, 7)].color == 'white' and isinstance(board[(7, 7)], Rook) and board[7, 7].firstMove:
                        moves.append([6,7])
            if self.color == 'black':
                if (1,0) not in board and (2,0) not in board and (3,0) not in board:
                    if (0,0) in board and board[(0, 0)].color == 'black' and isinstance(board[(0, 0)], Rook) and board[0, 0].firstMove:
                        moves.append([2,0])
                if (5,0) not in board and (6,0) not in board:
                    if (7,0) in board and board[(7, 0)].color == 'black' and isinstance(board[(7, 0)], Rook) and board[7, 0].firstMove:
                        moves.append([6,0])
        return moves
