import pygame
import random
import animation

class Spiritomb(animation.AnimateSprite) :
    def __init__(self) :
        super().__init__("spiritomb", "spiritomb", 112)
        #self.image = pygame.image.load('../assets/images/sprites/pepe/pepe_idle_gauche.png')
        #self.image = pygame.transform.scale(self.image, (60, 175))
        self.rect = self.image.get_rect()
        self.rect.x = 1035
        self.rect.y = 315
        self.size = (60, 60)

    def update_animation(self):
        self.animate(self.size)