import pygame
from player import Player
from pepe import Pepe
from spiritomb import Spiritomb

class Game :
    
    def __init__(self) :

        # Définir si notre jeu a commencé ou non
        self.is_playing = False

        # Générer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)

        # Générer Spiritomb
        self.all_spiritombs = pygame.sprite.Group()
        self.spiritomb = Spiritomb()
        self.all_spiritombs.add(self.spiritomb)

        # Groupe de pépé
        self.all_pepes = pygame.sprite.Group()

        self.pressed = {}

    def start(self):
        self.is_playing = True
        #self.spawn_pepe()
        #self.spawn_pepe()

    def update(self, screen):
        # Appliquer l'image du joueur
        screen.blit(pygame.transform.scale(self.player.image, self.player.getSize()), self.player.rect)

        # Actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # Actualiser l'animation du joueur
        self.player.update_animation()

        # Récupérer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # Récupérer les pépés de notre jeu
        for pepe in self.all_pepes:
            pepe.forward()
            pepe.update_health_bar(screen)
            pepe.update_animation()

        for spiritomb in self.all_spiritombs :
            spiritomb.update_animation()

        self.all_spiritombs.draw(screen)

        # Appliquer l'ensemble des images de mon groupe de projectiles
        self.player.all_projectiles.draw(screen)

        # Appliquer l'ensemble des images de mon groupe de pépés
        self.all_pepes.draw(screen)

        # Vérifier si le joueur souhaite aller à gauche ou à droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width - 150 < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > -10:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_pepe(self):
        pepe = Pepe(self)
        self.all_pepes.add(pepe)

    def game_over(self):
        self.all_pepes = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
