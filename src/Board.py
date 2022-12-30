import pygame

from Pieces import *
from Def import *

BG = (0,0,0)
FG = (255,255,255)
GRAY = (188, 188, 188)
P1_COLOR = (231,14,43,255)
P0_COLOR = (14,231,43, 255)
PLAYER0 = 0
PLAYER1 = 1

class Board:
    def __init__(self):
        self.pieces = []
        self.turn = PLAYER0 

        bishop  =  pygame.transform.scale(pygame.image.load("../assets/black_bishop.png"),(120, 120))
        rook    =  pygame.transform.scale(pygame.image.load("../assets/black_rook.png")  ,(120, 120))
        knight  =  pygame.transform.scale(pygame.image.load("../assets/black_knight.png"),(120, 120))
        pawn    =  pygame.transform.scale(pygame.image.load("../assets/black_pawn.png")  ,(120, 120))
        queen   =  pygame.transform.scale(pygame.image.load("../assets/black_queen.png") ,(120, 120))
        king    =  pygame.transform.scale(pygame.image.load("../assets/black_king.png")  ,(120, 120))

        self.pieces.append(Pieces(0, 0, ROOK,rook,P1_COLOR,1))
        self.pieces.append(Pieces(1, 0, KNIGHT,knight,P1_COLOR,1))
        self.pieces.append(Pieces(2, 0, BISHOP,bishop,P1_COLOR,1))
        self.pieces.append(Pieces(3, 0, QUEEN,queen,P1_COLOR,1))
        self.pieces.append(Pieces(4, 0, KING,king,P1_COLOR,1))
        self.pieces.append(Pieces(5, 0, BISHOP,bishop,P1_COLOR,1))
        self.pieces.append(Pieces(6, 0, KNIGHT,knight,P1_COLOR,1))
        self.pieces.append(Pieces(7, 0, ROOK,rook,P1_COLOR,1))
        self.pieces.append(Pieces(0, 1, PAWN,pawn,P1_COLOR,1))
        self.pieces.append(Pieces(1, 1, PAWN,pawn,P1_COLOR,1))
        self.pieces.append(Pieces(2, 1, PAWN,pawn,P1_COLOR,1))
        self.pieces.append(Pieces(3, 1, PAWN,pawn,P1_COLOR,1))
        self.pieces.append(Pieces(4, 1, PAWN,pawn,P1_COLOR,1))
        self.pieces.append(Pieces(5, 1, PAWN,pawn,P1_COLOR,1))
        self.pieces.append(Pieces(6, 1, PAWN,pawn,P1_COLOR,1))
        self.pieces.append(Pieces(7, 1, PAWN,pawn,P1_COLOR,1))

        self.pieces.append(Pieces(0, 7, ROOK,rook,P0_COLOR,0))
        self.pieces.append(Pieces(1, 7, KNIGHT,knight,P0_COLOR,0))
        self.pieces.append(Pieces(2, 7, BISHOP,bishop,P0_COLOR,0))
        self.pieces.append(Pieces(3, 7, QUEEN,queen,P0_COLOR,0))
        self.pieces.append(Pieces(4, 7, KING,king,P0_COLOR,0))
        self.pieces.append(Pieces(5, 7, BISHOP,bishop,P0_COLOR,0))
        self.pieces.append(Pieces(6, 7, KNIGHT,knight,P0_COLOR,0))
        self.pieces.append(Pieces(7, 7, ROOK,rook,P0_COLOR,0))
        self.pieces.append(Pieces(0, 6, PAWN,pawn,P0_COLOR,0))
        self.pieces.append(Pieces(1, 6, PAWN,pawn,P0_COLOR,0))
        self.pieces.append(Pieces(2, 6, PAWN,pawn,P0_COLOR,0))
        self.pieces.append(Pieces(3, 6, PAWN,pawn,P0_COLOR,0))
        self.pieces.append(Pieces(4, 6, PAWN,pawn,P0_COLOR,0))
        self.pieces.append(Pieces(5, 6, PAWN,pawn,P0_COLOR,0))
        self.pieces.append(Pieces(6, 6, PAWN,pawn,P0_COLOR,0))
        self.pieces.append(Pieces(7, 6, PAWN,pawn,P0_COLOR,0))

        self.clicked_pos = None
        self.grabbed_piece = None

    def show(self, canvas):
        canvas.fill(BG)
        for x in range(8):
            for y in range(8):
                if self.clicked_pos != None and self.clicked_pos[0] == x and self.clicked_pos[1] == y and self.grabbed_piece != None:
                    pygame.draw.rect(canvas, GRAY, (x*120, y*120, 120, 120))
                    continue

                if ((x + y) % 2) == 0 :
                    pygame.draw.rect(canvas, FG, (x*120, y*120, 120, 120))
        for p in self.pieces:
            w,h = p.sprite.get_size()
            r, g, b, _ = p.color
            for x in range(w):
                for y in range(h):
                    a = p.sprite.get_at((x,y))[3]
                    p.sprite.set_at((x,y), pygame.Color(r, g, b, a))
            canvas.blit(p.sprite, (120*p.x, 120*p.y))
        pygame.display.update()

    def handle_click(self, pos):
        x,y = pos
        self.clicked_pos = [x//120,y//120]
        if self.grabbed_piece == None:
            for p in self.pieces:
                if (p.x == self.clicked_pos[0] and p.y == self.clicked_pos[1] and p.player == self.turn) : self.grabbed_piece = p
        else:
            if self.grabbed_piece.move_to(self.clicked_pos[0], self.clicked_pos[1], self.pieces):
                if self.turn == PLAYER1: self.turn = PLAYER0
                else: self.turn = PLAYER1
            self.grabbed_piece = None
