import pygame, sys
from pygame.locals import *
BlackSquare = pygame.image.load("BBlank.png")
WhiteSquare = pygame.image.load("WBlank.png")
BlackPawn = pygame.image.load("BPawn.png")
BlackKnight = pygame.image.load("BKnight.png")
BlackBishop = pygame.image.load("BBishop.png")
BlackRook = pygame.image.load("BRook.png")
BlackQueen = pygame.image.load("BQueen.png")
BlackKing = pygame.image.load("BKing.png")
WhitePawn = pygame.image.load("WPawn.png")
WhiteKnight = pygame.image.load("WKnight.png")
WhiteBishop = pygame.image.load("WBishop.png")
WhiteRook = pygame.image.load("WRook.png")
WhiteQueen = pygame.image.load("WQueen.png")
WhiteKing = pygame.image.load("WKing.png")
MoveDot = pygame.image.load("MoveDot.png")
BlackPromote = pygame.image.load("BPromote.png")
WhitePromote = pygame.image.load("WPromote.png")
canvas = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Chess")
def GetPieceImage(img1, img2, color):
    if color == "w":
        return img1
    else:
        return img2
class Board:
    def __init__(self):
        self.board = []
        for x in range(8):
            self.board.append([])
            for y in range(8):
                if y == 0:
                    if x in [0, 7]:
                        self.board[-1].append(Rook("b"))
                    if x in [1, 6]:
                        self.board[-1].append(Knight("b"))
                    if x in [2, 5]:
                        self.board[-1].append(Bishop("b"))
                    if x == 3:
                        self.board[-1].append(Queen("b"))
                    if x == 4:
                        self.board[-1].append(King("b"))
                elif y == 1:
                    self.board[-1].append(Pawn("b"))
                elif y == 6:
                    self.board[-1].append(Pawn("w"))
                elif y == 7:
                    if x in [0, 7]:
                        self.board[-1].append(Rook("w"))
                    if x in [1, 6]:
                        self.board[-1].append(Knight("w"))
                    if x in [2, 5]:
                        self.board[-1].append(Bishop("w"))
                    if x == 3:
                        self.board[-1].append(Queen("w"))
                    if x == 4:
                        self.board[-1].append(King("w"))
                else:
                    self.board[-1].append(Empty())
    def displayBoard(self, view):
        for x in range(8):
            for y in range(8):
                if (x + y) % 2 == 1:
                    canvas.blit(BlackSquare, (x * 50, y * 50))
                else:
                    canvas.blit(WhiteSquare, (x * 50, y * 50))
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if view == "b":
                    readval = self.board[y][7 - x]
                else:
                    readval = self.board[y][x]
                if readval.identification != "#":
                    canvas.blit(readval.img, (y * 50, x * 50))
class Piece:
    def __init__(self):
        self.identification = "#"
        self.color = None
        self.img = None
    def click(self, board, pos):
        pass
class Empty(Piece):
    def __init__(self):
        super().__init__()
class PromoteSquare:
    def __init__(self, color):
        self.identification = "P"
        if color == "w":
            self.img = WhitePromote
        else:
            self.img = BlackPromote
        self.color = color
class Pawn(Piece):
    #Add en passant
    #And promotion
    def __init__(self, Color):
        self.identification = " "
        self.color = Color
        self.img = GetPieceImage(WhitePawn, BlackPawn, Color)
    def click(self, board, pos):
        possible_pos = []
        if self.color == "w":
            if pos[1] - 1 >= 0:
                if board[pos[0]][pos[1] - 1].identification == "#":
                    possible_pos.append([pos[0], pos[1] - 1])
                    if pos[1] == 6:
                        if board[pos[0]][pos[1] - 2].identification == "#":
                            possible_pos.append([pos[0], pos[1] - 2])
                if pos[0] - 1 >= 0:
                    if board[pos[0] - 1][pos[1] - 1].identification != "#":
                        if board[pos[0] - 1][pos[1] - 1].color != self.color:
                            possible_pos.append([pos[0] - 1, pos[1] - 1])
                if pos[0] + 1 <= 7:
                    if board[pos[0] + 1][pos[1] - 1].identification != "#":
                        if board[pos[0] + 1][pos[1] - 1].color != self.color:
                            possible_pos.append([pos[0] + 1, pos[1] - 1])
                    
        else:
            if pos[1] + 1 <= 7:
                if board[pos[0]][pos[1] + 1].identification == "#":
                    possible_pos.append([pos[0], pos[1] + 1])
                    if pos[1] == 1:
                        if board[pos[0]][pos[1] + 2].identification == "#":
                            possible_pos.append([pos[0], pos[1] + 2])
                if pos[0] - 1 >= 0:
                    if board[pos[0] - 1][pos[1] + 1].identification != "#":
                        if board[pos[0] - 1][pos[1] + 1].color != self.color:
                            possible_pos.append([pos[0] - 1, pos[1] + 1])
                if pos[0] + 1 <= 7:
                    if board[pos[0] + 1][pos[1] + 1].identification != "#":
                        if board[pos[0] + 1][pos[1] + 1].color != self.color:
                            possible_pos.append([pos[0] + 1, pos[1] + 1])
        return possible_pos
class Knight(Piece):
    def __init__(self, Color):
        self.identification = "N"
        self.color = Color
        self.img = GetPieceImage(WhiteKnight, BlackKnight, Color)
    def click(self, board, pos):
        possible_pos = []
        if pos[0] - 2 >= 0:
            if pos[1] - 1 >= 0:
                if board[pos[0] - 2][pos[1] - 1].color != self.color:
                    possible_pos.append([pos[0] - 2, pos[1] - 1])
            if pos[1] + 1 <= 7:
                if board[pos[0] - 2][pos[1] + 1].color != self.color:
                    possible_pos.append([pos[0] - 2, pos[1] + 1])
        if pos[0] + 2 <= 7:
            if pos[1] - 1 >= 0:
                if board[pos[0] + 2][pos[1] - 1].color != self.color:
                    possible_pos.append([pos[0] + 2, pos[1] - 1])
            if pos[1] + 1 <= 7:
                if board[pos[0] + 2][pos[1] + 1].color != self.color:
                    possible_pos.append([pos[0] + 2, pos[1] + 1])
        if pos[0] - 1 >= 0:
            if pos[1] - 2 >= 0:
                if board[pos[0] - 1][pos[1] - 2].color != self.color:
                    possible_pos.append([pos[0] - 1, pos[1] - 2])
            if pos[1] + 2 <= 7:
                if board[pos[0] - 1][pos[1] + 2].color != self.color:
                    possible_pos.append([pos[0] - 1, pos[1] + 2])
        if pos[0] + 1 <= 7:
            if pos[1] - 2 >= 0:
                if board[pos[0] + 1][pos[1] - 2].color != self.color:
                    possible_pos.append([pos[0] + 1, pos[1] - 2])
            if pos[1] + 2 <= 7:
                if board[pos[0] + 1][pos[1] + 2].color != self.color:
                    possible_pos.append([pos[0] + 1, pos[1] + 2])
        return possible_pos
class Bishop(Piece):
    def __init__(self, Color):
        self.identification = "B"
        self.color = Color
        self.img = GetPieceImage(WhiteBishop, BlackBishop, Color)
    def click(self, board, pos):
        possible_pos = []
        current_pos = [pos[0], pos[1]]
        while True:
            if current_pos[0] - 1 >= 0:
                if current_pos[1] - 1 >= 0:
                    if board[current_pos[0] - 1][current_pos[1] - 1].color != self.color:
                        possible_pos.append([current_pos[0] - 1, current_pos[1] - 1])
                        if board[current_pos[0] - 1][current_pos[1] - 1].color != None:
                            break
                    else:
                        break
                else:
                    break
            else:
                break
            current_pos[0] -= 1
            current_pos[1] -= 1
        current_pos = [pos[0], pos[1]]
        while True:
            if current_pos[0] - 1 >= 0:
                if current_pos[1] + 1 <= 7:
                    if board[current_pos[0] - 1][current_pos[1] + 1].color != self.color:
                        possible_pos.append([current_pos[0] - 1, current_pos[1] + 1])
                        if board[current_pos[0] - 1][current_pos[1] + 1].color != None:
                            break
                    else:
                        break
                else:
                    break
            else:
                    break
            current_pos[0] -= 1
            current_pos[1] += 1
        current_pos = [pos[0], pos[1]]
        while True:
            if current_pos[0] + 1 <= 7:
                if current_pos[1] - 1 >= 0:
                    if board[current_pos[0] + 1][current_pos[1] - 1].color != self.color:
                        possible_pos.append([current_pos[0] + 1, current_pos[1] - 1])
                        if board[current_pos[0] + 1][current_pos[1] - 1].color != None:
                            break
                    else:
                        break
                else:
                    break
            else:
                break
            current_pos[0] += 1
            current_pos[1] -= 1
        current_pos = [pos[0], pos[1]]
        while True:
            if current_pos[0] + 1 <= 7:
                if current_pos[1] + 1 <= 7:
                    if board[current_pos[0] + 1][current_pos[1] + 1].color != self.color:
                        possible_pos.append([current_pos[0] + 1, current_pos[1] + 1])
                        if board[current_pos[0] + 1][current_pos[1] + 1].color != None:
                            break
                    else:
                        break
                else:
                    break
            else:
                break
            current_pos[0] += 1
            current_pos[1] += 1
        return possible_pos
class Rook(Piece):
    def __init__(self, Color):
        self.identification = "R"
        self.color = Color
        self.img = GetPieceImage(WhiteRook, BlackRook, Color)
    def click(self, board, pos):
        possible_pos = []
        current_pos = [pos[0], pos[1]]
        while True:
            if current_pos[0] + 1 <= 7:
                if board[current_pos[0] + 1][current_pos[1]].color != self.color:
                    possible_pos.append([current_pos[0] + 1, current_pos[1]])
                    if board[current_pos[0] + 1][current_pos[1]].color != None:
                        break
                else:
                    break
            else:
                break
            current_pos[0] += 1
        current_pos = [pos[0], pos[1]]
        while True:
            if current_pos[0] - 1 >= 0:
                if board[current_pos[0] - 1][current_pos[1]].color != self.color:
                    possible_pos.append([current_pos[0] - 1, current_pos[1]])
                    if board[current_pos[0] - 1][current_pos[1]].color != None:
                        break
                else:
                    break
            else:
                break
            current_pos[0] -= 1
        current_pos = [pos[0], pos[1]]
        while True:
            if current_pos[1] + 1 <= 7:
                if board[current_pos[0]][current_pos[1] + 1].color != self.color:
                    possible_pos.append([current_pos[0], current_pos[1] + 1])
                    if board[current_pos[0]][current_pos[1] + 1].color != None:
                        break
                else:
                    break
            else:
                break
            current_pos[1] += 1
        current_pos = [pos[0], pos[1]]
        while True:
            if current_pos[1] - 1 >= 0:
                if board[current_pos[0]][current_pos[1] - 1].color != self.color:
                    possible_pos.append([current_pos[0], current_pos[1] - 1])
                    if board[current_pos[0]][current_pos[1] - 1].color != None:
                        break
                else:
                    break
            else:
                break
            current_pos[1] -= 1
        return possible_pos
class Queen(Piece):
    def __init__(self, Color):
        self.identification = "Q"
        self.color = Color
        self.img = GetPieceImage(WhiteQueen, BlackQueen, Color)
    def click(self, board, pos):
        possible_pos = []
        current_pos = [pos[0], pos[1]]
        while True:
            if current_pos[0] + 1 <= 7:
                if board[current_pos[0] + 1][current_pos[1]].color != self.color:
                    possible_pos.append([current_pos[0] + 1, current_pos[1]])
                    if board[current_pos[0] + 1][current_pos[1]].color != None:
                        break
                else:
                    break
            else:
                break
            current_pos[0] += 1
        current_pos = [pos[0], pos[1]]
        while True:
            if current_pos[0] - 1 >= 0:
                if board[current_pos[0] - 1][current_pos[1]].color != self.color:
                    possible_pos.append([current_pos[0] - 1, current_pos[1]])
                    if board[current_pos[0] - 1][current_pos[1]].color != None:
                        break
                else:
                    break
            else:
                break
            current_pos[0] -= 1
        current_pos = [pos[0], pos[1]]
        while True:
            if current_pos[1] + 1 <= 7:
                if board[current_pos[0]][current_pos[1] + 1].color != self.color:
                    possible_pos.append([current_pos[0], current_pos[1] + 1])
                    if board[current_pos[0]][current_pos[1] + 1].color != None:
                        break
                else:
                    break
            else:
                break
            current_pos[1] += 1
        current_pos = [pos[0], pos[1]]
        while True:
            if current_pos[1] - 1 >= 0:
                if board[current_pos[0]][current_pos[1] - 1].color != self.color:
                    possible_pos.append([current_pos[0], current_pos[1] - 1])
                    if board[current_pos[0]][current_pos[1] - 1].color != None:
                        break
                else:
                    break
            else:
                break
            current_pos[1] -= 1
        current_pos = [pos[0], pos[1]]
        while True:
            if current_pos[0] - 1 >= 0:
                if current_pos[1] - 1 >= 0:
                    if board[current_pos[0] - 1][current_pos[1] - 1].color != self.color:
                        possible_pos.append([current_pos[0] - 1, current_pos[1] - 1])
                        if board[current_pos[0] - 1][current_pos[1] - 1].color != None:
                            break
                    else:
                        break
                else:
                    break
            else:
                break
            current_pos[0] -= 1
            current_pos[1] -= 1
        current_pos = [pos[0], pos[1]]
        while True:
            if current_pos[0] - 1 >= 0:
                if current_pos[1] + 1 <= 7:
                    if board[current_pos[0] - 1][current_pos[1] + 1].color != self.color:
                        possible_pos.append([current_pos[0] - 1, current_pos[1] + 1])
                        if board[current_pos[0] - 1][current_pos[1] + 1].color != None:
                            break
                    else:
                        break
                else:
                    break
            else:
                    break
            current_pos[0] -= 1
            current_pos[1] += 1
        current_pos = [pos[0], pos[1]]
        while True:
            if current_pos[0] + 1 <= 7:
                if current_pos[1] - 1 >= 0:
                    if board[current_pos[0] + 1][current_pos[1] - 1].color != self.color:
                        possible_pos.append([current_pos[0] + 1, current_pos[1] - 1])
                        if board[current_pos[0] + 1][current_pos[1] - 1].color != None:
                            break
                    else:
                        break
                else:
                    break
            else:
                break
            current_pos[0] += 1
            current_pos[1] -= 1
        current_pos = [pos[0], pos[1]]
        while True:
            if current_pos[0] + 1 <= 7:
                if current_pos[1] + 1 <= 7:
                    if board[current_pos[0] + 1][current_pos[1] + 1].color != self.color:
                        possible_pos.append([current_pos[0] + 1, current_pos[1] + 1])
                        if board[current_pos[0] + 1][current_pos[1] + 1].color != None:
                            break
                    else:
                        break
                else:
                    break
            else:
                break
            current_pos[0] += 1
            current_pos[1] += 1
       
        return possible_pos
class King(Piece):
    def __init__(self, Color):
        self.identification = "K"
        self.color = Color
        self.img = GetPieceImage(WhiteKing, BlackKing, Color)
    def click(self, board, pos):
        possible_pos = []
        if pos[0] + 1 <= 7:
            if board[pos[0] + 1][pos[1]].color != self.color:
                possible_pos.append([pos[0] + 1, pos[1]])
        if pos[0] - 1 >= 0:
            if board[pos[0] - 1][pos[1]].color != self.color:
                possible_pos.append([pos[0] - 1, pos[1]])
        if pos[1] + 1 <= 7:
            if board[pos[0]][pos[1] + 1].color != self.color:
                possible_pos.append([pos[0], pos[1] + 1])
        if pos[1] - 1 >= 0:
            if board[pos[0]][pos[1] - 1].color != self.color:
                possible_pos.append([pos[0], pos[1] - 1])
        if pos[0] + 1 <= 7:
            if pos[1] + 1 <= 7:
                if board[pos[0] + 1][pos[1] + 1].color != self.color:
                    possible_pos.append([pos[0] + 1, pos[1] + 1])
        if pos[0] + 1 <= 7:
            if pos[1] - 1  >= 0:
                if board[pos[0] + 1][pos[1] - 1].color != self.color:
                    possible_pos.append([pos[0] + 1, pos[1] - 1])
        if pos[0] - 1 >= 0:
            if pos[1] + 1 <= 7:
                if board[pos[0] - 1][pos[1] + 1].color != self.color:
                    possible_pos.append([pos[0] - 1, pos[1] + 1])
        if pos[0] - 1 >= 0:
            if pos[1] - 1 <= 7:
                if board[pos[0] - 1][pos[1] - 1].color != self.color:
                    possible_pos.append([pos[0] - 1, pos[1] - 1])
        return possible_pos
board = Board()
clicked = Empty()
clicked_pos = None
move_options = []
promotion_query = False
promotion_x = None
while True:
    board.displayBoard("w")
    for x in move_options:
        canvas.blit(MoveDot, (x[0] * 50, x[1] * 50))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            mpos = pygame.mouse.get_pos()
            bpos = [int(mpos[0] / 50), int(mpos[1] / 50)]
            if board.board[bpos[0]][bpos[1]].identification == "P":
                PromotePiece = board.board[bpos[0]][bpos[1]]
                if mpos[0] - bpos[0] * 50 <= 25:
                    if mpos[1] - bpos[1] * 50 <= 25:
                        board.board[bpos[0]][bpos[1]] = Queen(PromotePiece.color)
                        move_options = []
                    else:
                        board.board[bpos[0]][bpos[1]] = Knight(PromotePiece.color)
                        move_options = []
                else:
                    if mpos[1] - bpos[1] * 50 <= 25:
                        board.board[bpos[0]][bpos[1]] = Rook(PromotePiece.color)
                        move_options = []
                    else:
                        board.board[bpos[0]][bpos[1]] = Bishop(PromotePiece.color)
                        move_options = []
            elif bpos in move_options:
                if clicked.identification == " ":
                    if clicked.color == "w":
                        if bpos[1] == 0:
                            board.board[clicked_pos[0]][clicked_pos[1]] = Empty()
                            board.board[bpos[0]][bpos[1]] = PromoteSquare("w")
                            promotion_x = bpos[0]
                            promotion_query = True
                        else:
                            board.board[bpos[0]][bpos[1]] = clicked
                            board.board[clicked_pos[0]][clicked_pos[1]] = Empty()
                            clicked = None
                            clicked_pos = None
                            move_options = []
                    elif clicked.color == "b":
                        if bpos[1] == 7:
                            board.board[clicked_pos[0]][clicked_pos[1]] = Empty()
                            board.board[bpos[0]][bpos[1]] = PromoteSquare("b")
                            promotion_x = bpos[0]
                            promotion_query = True
                        else:
                            board.board[bpos[0]][bpos[1]] = clicked
                            board.board[clicked_pos[0]][clicked_pos[1]] = Empty()
                            clicked = None
                            clicked_pos = None
                            move_options = []
                    else:
                        board.board[bpos[0]][bpos[1]] = clicked
                        board.board[clicked_pos[0]][clicked_pos[1]] = Empty()
                        clicked = None
                        clicked_pos = None
                        move_options = []
                else:
                    board.board[bpos[0]][bpos[1]] = clicked
                    board.board[clicked_pos[0]][clicked_pos[1]] = Empty()
                    clicked = None
                    clicked_pos = None
                    move_options = []
            elif board.board[bpos[0]][bpos[1]].identification != "#":
                clicked = board.board[bpos[0]][bpos[1]]
                clicked_pos = bpos
                move_options = board.board[bpos[0]][bpos[1]].click(board.board, bpos)
                for x in move_options:
                    canvas.blit(MoveDot, (x[0] * 50, x[1] * 50))
    pygame.display.update()
