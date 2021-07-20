import pygame
from peace import *
from pygame.locals import *
pygame.init()

dot = pygame.image.load('dot.png')
dot = pygame.transform.scale(dot, (90, 90))
dots = []
clicked_peace = None
PIECES = [None] * 12

def Transform(peace, board):
    if peace.color == 'black':
        board[(peace.x, peace.y)] = Queen('black', PIECES[7], peace.x, peace.y)
    else:
        board[(peace.x, peace.y)] = Queen('white', PIECES[1], peace.x, peace.y)


class Game():
    def __init__(self):
        
        board = {}

        #create pieces snipets
        SQW = 90
        SPRITE = pygame.transform.smoothscale(pygame.image.load('Chess_Pieces_Sprite.png'), (int(SQW*6), int(SQW*2)))
        global PIECES
        for i in range(2):
            for j in range(6):
                PIECES[j + i*6] = pygame.Surface.subsurface(SPRITE, (j*SQW, i*SQW, SQW, SQW))

        #create pieces
        pieces = [None] * 16
        for i in range(16):
            if i < 8:
                board[(i, 1)] = Pawn('black', PIECES[11], i, 1, 1)
            else:
                board[(i - 8, 6)] = Pawn('white', PIECES[5], i - 8, 6, 1)
        board[(2,0)] = Bishop('black', PIECES[8], 2, 0)
        board[(5,0)] = Bishop('black', PIECES[8], 5, 0)
        board[(2,7)] = Bishop('white', PIECES[2], 2, 7)
        board[(5,7)] = Bishop('black', PIECES[2], 5, 7)
        board[(1,0)] = Knight('black', PIECES[9], 1, 0)
        board[(6,0)] = Knight('black', PIECES[9], 6, 0)
        board[(1,7)] = Knight('white', PIECES[3], 1, 7)
        board[(6,7)] = Knight('white', PIECES[3], 6, 7)
        board[(0,0)] = Rook('black', PIECES[10], 0, 0)
        board[(7,0)] = Rook('black', PIECES[10], 7, 0)
        board[(0,7)] = Rook('white', PIECES[4], 0, 7)
        board[(7,7)] = Rook('white', PIECES[4], 7, 7)
        board[(4,0)] = Queen('black', PIECES[7], 4, 0)
        board[(4,7)] = Queen('white', PIECES[1], 4, 7)
        
        board[(3,0)] = King('black', PIECES[6], 3, 0)
        board[(3,7)] = King('white', PIECES[0], 3, 7)

        #create game window
        pygame.display.set_caption('chess')
        self.clock = pygame.time.get_ticks()
        self.screen_res = [750, 500]
        board_image = pygame.image.load('board.png')
        board_image = pygame.transform.scale(board_image, (720,720))
        background_colour = (255,255,255)
        (width, height) = (720, 720)
        self.screen = pygame.display.set_mode((width, height))
        self.screen.fill(background_colour)
        self.screen.blit(board_image, (0, 0))
        pygame.display.flip()

        clock = pygame.time.Clock()
        clock.tick(60)

        while 1:
            self.Loop(board,board_image)
  

    def Loop(self, board, board_image):
        # main game loop
        self.eventLoop(board)
        
        self.Tick()
        self.Draw(board, board_image)
        

    def Draw(self,board, board_image):
        #print(dots)
        background_colour = (255,255,255)
        #self.screen.fill(background_colour)
        self.screen.blit(board_image, (0, 0))
        for peace in board.values():
            self.screen.blit(peace.img, (peace.coord()))
        for d in dots:
            self.screen.blit(dot, [d[0] * 90, d[1] * 90])
        pygame.display.update()

    def eventLoop(self,board):
        global dots
        global clicked_peace
        moves = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for s in board.values():
                    if s.click(pos):
                        clicked_peace = s
                        dots = s.onClick(board)
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if clicked_peace is not None:
                    if clicked_peace.move(pos, dots, board):
                        Transform(clicked_peace, board)
                dots = []


    def Tick(self):
        pass


Game()