import pygame
from sprites.x import X
from sprites.o import O
from sprites.bg import Background

class Game:
    def __init__(self, gameboard, cell_size, turn):
        self.cell_size = cell_size
        self.xs = pygame.sprite.Group()
        self.os = pygame.sprite.Group()
        self.bgs = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.winner = None
        self._draw_board(gameboard)
        self.draw = False

    def draw_end(self):
        if self.winner is None:
            pass
        else:
            pass
            #tilastoihin lisätään x / o voitto
        if self.draw:
            #tilastoihin lisätään tasapeli
            pass

    def check_win(self, gameboard):
        for row in range(0, 3):
            if ((gameboard[row][0] == gameboard[row][1] == gameboard[row][2]) and (gameboard[row][0] != 0)):
                self.winner = gameboard[row][0]
                break

        for column in range(0, 3):
            if (gameboard[0][column] == gameboard[1][column] == gameboard[2][column]) and (gameboard[0][column] != 0):
                self.winner = gameboard[0][column]
                break

        if (gameboard[0][0] == gameboard[1][1] == gameboard[2][2]) and (gameboard[0][0] != 0):
            self.winner = gameboard[0][0]

        if (gameboard[0][2] == gameboard[1][1] == gameboard[2][0]) and (gameboard[0][2] != 0):
            self.winner = gameboard[0][2]

        if (all([all(row) for row in gameboard]) and self.winner is None):
            self.draw = True
        draw_end()

    def drawOX(row, column, gameboard, turn):
        width = len(gameboard[0])
        height = len(gameboard)

        if row == 1:
            posx = 30
        if row == 2:
            posx = width/3 + 30
        if row == 3:
            posx = width/3*2 + 30

        if column == 1:
            posy = 30
        if column == 2:
            posy = height/3 +30
        if column == 3:
            posy = height/3*2 + 30

        if turn == "o":
            gameboard[row-1][column-1] = "o"
            turn == "x"
        else:
            gameboard[row-1][column-1] = "x"
            turn == "o"
        self._draw_board(gameboard)

    def click(self, gameboard):
        width = len(gameboard[0])
        height = len(gameboard)
        x,y = pygame.mouse.get_pos()

        if (x < width/3):
            column = 1
        elif (x < width/3*2):
            column = 2
        elif (x < width):
            column = 3
        else:
            column = None

        if (y < height/3):
            row = 1
        elif (y < height/3*2):
            row = 2
        elif (y < height):
            row = 3
        else:
            row = None

        if (row and column and gameboard[row-1][column-1] == 0):
            drawOX(row, col, gameboard, turn)
            check_win()

    def _draw_board(self, gameboard):
        height = len(gameboard)
        width = len(gameboard[0])
        for y in range(height):
            for x in range(width):
                cell = gameboard[y][x]
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                if cell == 0:
                   self.bgs.add(Background(normalized_x, normalized_y))
                if cell == "x":
                   self.xs.add(X(normalized_x, normalized_y))
                if cell == "o":
                   self.os.add(O(normalized_x, normalized_y))

        self.all_sprites.add(
            self.bgs,
            self.xs,
            self.os
        )

    def reset_game(self, gameboard, turn):
        self.winner = None
        self.draw = False
        turn = "x"
        gameboard = [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]
