import pygame
from pygame.sprite import Sprite

from nlc_dino_runner.components import game
from nlc_dino_runner.components.obstaculos import obstacle
from nlc_dino_runner.components.obstaculos.cactus import Cactus
from nlc_dino_runner.components.obstaculos.obstacle import Obstacle
from nlc_dino_runner.utils.constants import HEART, SMALL_CACTUS


class Heart(Sprite):
    def __init__(self):
        self.image = HEART
        self.list_hearts = [self.image, self.image, self.image, self.image, self.image]
        self.rect.x = 20
        self.rect.y = 20

    def update(self):
        for heart in self.list_hearts:
            heart.update(game.game_speed, self.list_hearts)
            if game.player.dino_rect.colliderect[Obstacle]:
                if game.player_shield:
                    self.list_hearts.remowe(obstacle)
                else:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1

    def draw(self, screen):
        for heart in self.list_hearts:
            screen.blit(heart(self.rect.x, self.rect.y))
