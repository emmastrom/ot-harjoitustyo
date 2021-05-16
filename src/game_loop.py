import pygame

class GameLoop:
    def __init__(self, game, renderer, event_queue, clock, cell_size, board):
        self._game = game
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self._cell_size = cell_size
        self.board = board

    def start(self):
        while True:
            if self._handle_events(self.board) == False:
                break

            current_time = self._clock.get_ticks()

            self._game.update(current_time)
            self._render()

            if self._game.is_completed():
                break

            self._clock.tick(60)


    def _handle_events(self, board):
        while True:
            for event in self._event_queue.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self._game.click(board)
                    if (self._game.winner or self._game.draw):
                        self._game.reset_game()
                elif event.type == pygame.QUIT:
                    return False

    def _render(self):
        self._renderer.render()
