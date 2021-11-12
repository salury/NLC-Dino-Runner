import pygame
from nlc_dino_runner.components.obstaculos.cactus import Cactus
from nlc_dino_runner.utils.constants import SMALL_CACTUS


class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player_shield:
                    self.obstacles.remowe(obstacle)
                else:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
