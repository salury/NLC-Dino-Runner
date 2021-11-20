from pygame.sprite import Sprite

from nlc_dino_runner.components.powerups.power_up import PowerUp
from nlc_dino_runner.utils.constants import HAMMER, SCREEN_WIDTH, HAMMER_TYPE


class Hammer(Sprite):
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = HAMMER
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = 15

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.x += self.speedy
        if self.rect.left < SCREEN_WIDTH:
            self.kill()


class HammerPowerUp(PowerUp):
    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        super(HammerPowerUp, self).__init__(self.image, self.type)
