import pygame
import math
from gameObject import GameObject
from Hitboxes import Hitboxes

class Obstacles(GameObject):
    @staticmethod
    def init():
        #image = pygame.image.load("purpleClouds.jpg").convert_alpha()
        pass

    def __init__(self, x, y):
        self.image = pygame.transform.scale(pygame.image.load("lightning ball2.png").convert_alpha(),
                                            (150, 150))
        width, height = self.image.get_size()
        self.hitbox = Hitboxes(x, y, width, height)
        super(Obstacles, self).__init__(x, y, self.image)

    def update(self, screenWidth, screenHeight):
        super(Obstacles, self).update(screenWidth, screenHeight, self.image)