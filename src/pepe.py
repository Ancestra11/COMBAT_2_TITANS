import pygame
import random
import animation

class Pepe(animation.AnimateSprite) :

    def __init__(self, game) :
        super().__init__("pepe", "pepe_idle_gauche", 2)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        # TODO : Si la cible va vers la droite, tourner le sprite à droite avec uniquement du code
        self.image = pygame.image.load('../assets/images/sprites/pepe/pepe_idle_gauche.png')
        self.image = pygame.transform.scale(self.image, (60, 175))
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 300
        self.size = (60, 175)
        self.velocity = random.randint(1, 2)
        self.animationSpeed = 0.10

    def damage(self, amount):
        self.health -= amount
        # TODO : Mettre un autre son, plus agréable à écouter. Ou ne pas en mettre
        #self.game.sound_manager.play('damage_taken_sfx', False)

        # Fait respawn pépé ailleurs si ses PV sont <= à 0 (évite le surchargement de la mémoire)
        if self.health <= 0 :
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.max_health
            self.velocity = random.randint(1, 2)

    def update_animation(self):
        self.animate(self.size, self.animationSpeed)

    def update_health_bar(self, surface):
        # Code RGB vert de la barre de vie
        bar_color = (111, 210, 46)

        # Code RGB gris de l'arrière plan de la barre de vie
        back_bar_color = (60, 63, 60)

        # [x, y, largeur, hauteur]
        bar_position = [self.rect.x - 25, self.rect.y - 10, self.health, 5]
        back_bar_position = [self.rect.x - 25, self.rect.y - 10, self.max_health, 5]

        # Dessiner la barre de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)


    def forward(self):
        # Faire avancer pépé s'il n'y a pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players) :
            self.rect.x -= self.velocity
        else :
            # Baisser la vie du joueur s'il y a collision
            self.game.player.damage(self.attack)
