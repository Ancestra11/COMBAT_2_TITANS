import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite) :
    
    def __init__(self, game) :
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 2
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('../assets/images/sprites/player/rayman_idle1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 120
        self.rect.y = 370
        self.height = 90
        self.width = 90
        
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

    def update_health_bar(self, surface):

        # Dessiner la barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 9, self.rect.y - 10, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 9, self.rect.y - 10, self.health, 5])

    def damage(self, amount):
        if self.health - amount > amount :
            self.health -= amount
        else :
            self.game.game_over()
