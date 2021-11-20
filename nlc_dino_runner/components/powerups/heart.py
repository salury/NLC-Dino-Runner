import pygame
from pygame.sprite import Sprite
from nlc_dino_runner.components import game
from nlc_dino_runner.components.obstaculos import obstacle
from nlc_dino_runner.utils.constants import HEART, HEART_COUNT


class Heart(Sprite):
    def __init__(self, x_position, y_position):
        self.image = HEART
        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = y_position

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        obstacle.update(game.game_speed, self.obstacles)
        if game.player.dino_rect.colliderect(obstacle.rect):
            if not game.player.shield:
                game.player_heart_manager.reduce_heart()
                if game.player_heart_manager.heart_count > 0:
                    game.player.shield = True
                    game.player.show_text = False
                    star_time = pygame.time.get_ticks()
                    game.player.shield_time_up = star_time + 1000
                else:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count = 1
            else:
                self.obstacle.remove(obstacle)

class HeartManager:
    def __init__(self):
        self.heart_count = HEART_COUNT

    def reduce_heart(self):
        self.heart_count -= 1

    def draw(self, screen):
        x_position = 10
        y_position = 20
        for count in range(self.heart_count):
            heart = Heart(x_position, y_position)
            heart.draw(screen)
            x_position += 30

class PlayerHeartManager:
    def __init__(self):
        self.heart_count = HEART_COUNT

    def reduce_heart(self):
        self.heart_count -= 1

    def draw(self, screen):
        x_position = 10
        y_position = 20
        for counter in range(self.heart_count):
            heart = Heart(x_position, y_position)
            heart.draw(screen)
            x_position += 30

        def reset_hearts(self):
            self.heart_count = HEART_COUNT