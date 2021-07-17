import pygame
from peace import *
from pygame.locals import *
pygame.init()

class Game():
    def __init__(self):
        
        #create pieces snipets
        SQW = 90
        SPRITE = pygame.transform.smoothscale(pygame.image.load('Chess_Pieces_Sprite.png'), (int(SQW*6), int(SQW*2)))
        PIECES = [None] * 12
        for i in range(2):
            for j in range(6):
                PIECES[j + i*6] = pygame.Surface.subsurface(SPRITE, (j*SQW, i*SQW, SQW, SQW))

        #create pieces
        pieces = [None] * 16
        for i in range(16):
            if i < 8:
                pieces[i] = Pawn('black', PIECES[11], i, 1, 1)
            else:
                pieces[i] = Pawn('white', PIECES[5], i - 8, 6, 1)
        pieces.append(Bishop('black', PIECES[8], 2, 0))
        pieces.append(Bishop('black', PIECES[8], 5, 0))
        pieces.append(Bishop('white', PIECES[2], 2, 7))
        pieces.append(Bishop('black', PIECES[2], 5, 7))
        pieces.append(Knight('black', PIECES[9], 1, 0))
        pieces.append(Knight('black', PIECES[9], 6, 0))
        pieces.append(Knight('white', PIECES[3], 1, 7))
        pieces.append(Knight('white', PIECES[3], 6, 7))
        pieces.append(Rook('black', PIECES[10], 0, 0))
        pieces.append(Rook('black', PIECES[10], 7, 0))
        pieces.append(Rook('white', PIECES[4], 0, 7))
        pieces.append(Rook('white', PIECES[4], 7, 7))
        pieces.append(Queen('black', PIECES[7], 4, 0))
        pieces.append(Queen('white', PIECES[1], 4, 7))
        pieces.append(King('black', PIECES[6], 3, 0))
        pieces.append(King('white', PIECES[0], 3, 7))

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

        while 1:
            self.Loop(pieces)
  

    def Loop(self, peaces):
        # main game loop
        self.eventLoop()
        
        self.Tick()
        self.Draw(peaces)
        pygame.display.update()

    def Draw(self,peaces):
        for peace in peaces:
            self.screen.blit(peace.img, (peace.coord()))

    def eventLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    def Tick(self):
        pass


Game()