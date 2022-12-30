from Def import *

def sign(x):
    return (x > 0) - (x < 0)

class Pieces:
    def __init__(self, x, y, piece_type, sprite, color, player):
        self.x = x
        self.y = y
        self.player = player
        self.color = color
        self.first_move = True
        self.piece = piece_type
        self.sprite = sprite


    def valid_move(self, next_x, next_y, pieces_list):
        if next_x < 0 or next_x > 7: return False
        if next_y < 0 or next_y > 7: return False
        if self.x == next_x and self.y == next_y: return False

        if self.piece == ROOK:
            if next_x == self.x:
                if next_y > self.y:
                    for p in pieces_list:
                        if p.x == next_x and (p.y < next_y and p.y > self.y) and p != self: return False
                else:
                    for p in pieces_list:
                        if p.x == next_x and (p.y > next_y and p.y < self.y) and p != self: return False
            elif(next_y == self.y):
                if next_x > self.x:
                    for p in pieces_list:
                        if p.y == next_y and (p.x < next_x and p.x > self.x) and p != self: return False
                else:
                    for p in pieces_list:
                        if p.y == next_y and (p.x > next_x and p.x < self.x) and p != self: return False
            else: return False

        elif self.piece == KNIGHT:
            # we got our knight!!!
            if abs(self.x - next_x) == 1:
                if abs(self.y - next_y) == 2:
                    return True
                else: return False
            elif abs(self.y - next_y) == 1:
                if abs(self.x - next_x) == 2:
                    return True
                else: return False
            else: return False

        elif self.piece == BISHOP:
            # It's compicated
            # I need to figure out an efficient solution to validate the next move of bishop.
            diff_x = next_x - self.x
            diff_y = next_y - self.y
            dist = (diff_x**2 + diff_y**2)
            if abs(diff_x) == abs(diff_y):
                for p in pieces_list:
                    ndiff_x = p.x - self.x
                    ndiff_y = p.y - self.y
                    if abs(ndiff_x) == abs(ndiff_y):
                        if sign(diff_x) == sign(ndiff_x) and sign(diff_y) == sign(ndiff_y):
                            if dist > (ndiff_x**2 + ndiff_y**2): return False
                return True
            else: return False

        elif self.piece == QUEEN:
            if next_x == self.x:
                if next_y > self.y:
                    for p in pieces_list:
                        if p.x == next_x and (p.y < next_y and p.y > self.y) and p != self: return False
                else:
                    for p in pieces_list:
                        if p.x == next_x and (p.y > next_y and p.y < self.y) and p != self: return False
                return True
            elif(next_y == self.y):
                if next_x > self.x:
                    for p in pieces_list:
                        if p.y == next_y and (p.x < next_x and p.x > self.x) and p != self: return False
                else:
                    for p in pieces_list:
                        if p.y == next_y and (p.x > next_x and p.x < self.x) and p != self: return False
                return True

            diff_x = next_x - self.x
            diff_y = next_y - self.y
            dist = (diff_x**2 + diff_y**2)
            if abs(diff_x) == abs(diff_y):
                for p in pieces_list:
                    ndiff_x = p.x - self.x
                    ndiff_y = p.y - self.y
                    if abs(ndiff_x) == abs(ndiff_y):
                        if sign(diff_x) == sign(ndiff_x) and sign(diff_y) == sign(ndiff_y):
                            if dist > (ndiff_x**2 + ndiff_y**2): return False
                return True
            else: return False
        
        elif self.piece == KING:
            if abs(self.x - next_x) > 1 or abs(self.y - next_y) > 1: return False
            else: return True

        elif self.piece == PAWN:
            if self.player == 0:
                if self.first_move:
                    if (self.x != next_x) or ((self.y - next_y) != 2 and (self.y - next_y) != 1): return False
                    else: return True
                else:
                    if (self.x != next_x) or (self.y - next_y) != 1: return False
                    else: return True

            elif self.player == 1:
                if self.first_move:
                    if (self.x != next_x) or (-self.y + next_y != 2 and -self.y + next_y != 1): return False
                    else: return True
                else:
                    if (self.x != next_x) or -self.y + next_y != 1: return False
                    else: return True
            else:
                assert "UNKNOWN PLAYER"

        return True

    def move_to(self, next_x, next_y, pieces_list):

        if self.valid_move(next_x, next_y, pieces_list):
            # Cheking if we can kill the opponents piece
            for p in pieces_list:
                if p.x == next_x and p.y == next_y:
                    if self.player != p.player:
                        pieces_list.remove(p)
                        self.x = next_x
                        self.y = next_y
                        self.first_move = False
                        return True
                    else: return False
            self.x = next_x
            self.y = next_y
            self.first_move = False
            return True
        else: return False

