import pygame

from constants import WIDTH, HEIGHT, WHITE


class Visualizer:
    def __init__(self):
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))

    def draw(self, game):
        pygame.draw.rect(self.surface, WHITE, pygame.Rect(0, 0, WIDTH, HEIGHT))
        pygame.display.flip()
