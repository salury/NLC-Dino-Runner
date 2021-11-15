import pygame
from pygame.sprite import Sprite
from nlc_dino_runner.utils.constants import HEART

class Heart(Sprite, HEART):
    def __init__(self):
        self.image = HEART
        self.rect.x = 20
        self.rect.y = 20

    def update(self, ):
        self.list = []

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

