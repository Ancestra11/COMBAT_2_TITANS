import pygame
from projectile import Projectile
import animation

class Player(animation.AnimateSprite) :
    
    def __init__(self, game) :
        super().__init__('player', 'rayman_idle', 2)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 2
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 120
        self.rect.y = 350
        self.height = 150
        self.width = 77.5
        self.size = (self.height, self.width)
        self.animationSpeed = 0.10
        
    def move_right(self) :
        # Si le joueur n'est pas en collision avec pépé
        if not self.game.check_collision(self, self.game.all_pepes) :
            self.rect.x += self.velocity
        
    def move_left(self) :
        self.rect.x -= self.velocity
        
    def getSize(self) :
        return self.width, self.height

    def launch_projectile(self) :
        projectile = Projectile(self)
        self.all_projectiles.add(projectile)

        # Démarrer l'animation du lancer
        self.start_animation()

    def update_health_bar(self, surface):

        # Dessiner la barre de vie
        #pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 9, self.rect.y - 10, self.max_health, 5])
        #pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 9, self.rect.y - 10, self.health, 5])
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x - 5, self.rect.y - 10, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x - 5, self.rect.y - 10, self.health, 5])

    def damage(self, amount):
        if self.health - amount > amount :
            self.health -= amount
        else :
            self.game.game_over()

    def update_animation(self):
        self.animate(self.size, self.animationSpeed)
