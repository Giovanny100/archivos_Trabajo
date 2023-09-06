import pygame
from constants import *

WIDTH = 50
HEIGHT = 50

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()

        self.surf = pygame.Surface((WIDTH, HEIGHT))
        pygame.draw.rect(self.surf, (255,255,255), pygame.Re)