import pygame

# Poing de Rayman envoyé pour infliger des dégâts
class Projectile(pygame.sprite.Sprite) :

    def __init__(self, player):
        super().__init__()
        self.velocity = 2
        self.player = player
        self.image = pygame.image.load('../assets/images/sprites/player/projectile.png')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 80
        self.rect.y = player.rect.y + 30

    def move(self):
        # TODO : Si le joueur regarde à gauche, ça tire vers la gauche et inversement
        self.rect.x += self.velocity

        # Supprimer le projectile s'il entre en collision avec pépé et infliger les dégâts
        for pepe in self.player.game.check_collision(self, self.player.game.all_pepes) :
            self.remove()
            pepe.damage(self.player.attack)

        # Vérifier si notre projectile n'est plus présent sur l'écran
        if self.rect.x > 1280 :
            self.remove()

    def remove(self):
        self.player.all_projectiles.remove(self)
