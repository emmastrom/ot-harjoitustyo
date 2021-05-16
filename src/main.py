import pygame
from game import Game
from game_loop import GameLoop
from event_queue import EventQueue
from renderer import Renderer
from clock import Clock

turn = "x"
winner = None
draw = False

gameboard = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

CELL_SIZE = 120

def main():
    board = gameboard
    height = len(gameboard)
    width = len(gameboard)
    display_height = height * CELL_SIZE
    display_width = width * CELL_SIZE
    display = pygame.display.set_mode((display_width, display_height))

    pygame.display.set_caption("TicTacToe")

    game = Game(board, CELL_SIZE, turn)

    event_queue = EventQueue()
    renderer = Renderer(display, game)
    clock = Clock()
    game_loop = GameLoop(game, renderer, event_queue, clock, CELL_SIZE, board)

    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()
