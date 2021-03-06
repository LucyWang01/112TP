import pygame
import math
from gameObject import GameObject

# This is the Coins class that subclasses the GameObject class
# import coins and stars sprites and contain init and update methods
class Coins(GameObject):
    @staticmethod
    def init():
        # image taken from: https://webstockreview.net/images/coin-clipart-sprite-5.png
        Coins.sprite = [pygame.image.load("coins/coin1.png"),
                        pygame.image.load("coins/coin2.png"),
                        pygame.image.load("coins/coin3.png"),
                        pygame.image.load("coins/coin4.png"),
                        pygame.image.load("coins/coin5.png"),
                        pygame.image.load("coins/coin6.png")]
        # image taken from: https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/google/110/sparkles_2728.png
        Coins.starSprite = [pygame.transform.scale(pygame.image.load("stars.png"),
                                                   (20, 20)),
                            pygame.transform.scale(pygame.image.load("stars.png"),
                                                   (15, 15)),
                            pygame.transform.scale(pygame.image.load("stars.png"),
                                                   (10, 10))]
        
        for i in range(len(Coins.sprite)):
            Coins.sprite[i] = pygame.transform.scale(Coins.sprite[i], (15, 15))
        Coins.count = 0
        Coins.heart = [(0, 0), (15, 0), (30, 0), (45, 0), (10, -15), (35, -15), (15, 15), (30, 15), (22.5, 30)]
        Coins.lines = [(0, 0), (15, 0), (30, 0), (45, 0), (60, 0), (75, 0), (90, 0)]

    def __init__(self, x, y):
        self.image = Coins.sprite[0]
        width, height = self.image.get_size()
        self.scroll = 0
        self.scrollY = 0
        self.hit = False
        self.count = 0
        self.past = False
        self.isVisible = False
        
        super(Coins, self).__init__(x, y, self.image)

    def update(self, screenWidth, screenHeight, playerX, playerY, playerMode):
        if playerX - self.x - self.width / 2 > screenWidth / 2:
            self.kill()
        if abs(self.x - playerX) <= screenWidth / 2 - 170 and abs(self.y - playerY) <= screenHeight / 2 - 80:
            self.isVisible = True
        else:
            self.isVisible = False
        if self.hit:
            if self.count > 2:
                self.kill()
            self.image = Coins.starSprite[self.count % 3]
        else:
            self.image = Coins.sprite[self.count % 6]
        self.count += 1
        if playerMode == "magnet suit" and self.isVisible:
            self.x -= (self.x - playerX) // 5
            self.y -= (self.y - playerY) // 5
            self.scroll += (self.x - playerX) // 5
            self.scrollY += (self.y - playerY) // 5
        super(Coins, self).update(screenWidth, screenHeight, self.image)

