from nlc_dino_runner.utils.constants import SMALL_CACTUS

from nlc_dino_runner.components.obstaculos.obstacle import Obstacle
import random


class Cactus(Obstacle):
    def __init__(self, image):
        self.index = random.randint(0,2)
        super().__init__(image, self.index)
        # El super es para usar algo de la clase padre
        self.rect.y = 310

