import pygame
from load_image import load_image

class X(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_image("x.png")
