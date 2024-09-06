import pygame
from constants import *

class Scoreboard():
    def __init__(self):
        self.score = 0
        self.message = "Score: " + str(self.score)
        self.font = pygame.font.SysFont('ubuntu', 36)
        self.text_surface = self.font.render(self.message, True, (255, 255, 255))

    def update_score(self, score):
        self.score += score
        self.message = "Score " + str(self.score)
        self.text_surface = self.font.render(self.message, True, (255, 255, 255))

    def render(self, screen):
        screen.blit(self.text_surface, self.text_surface.get_rect(center = (SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 30)))
