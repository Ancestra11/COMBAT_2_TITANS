import pygame
import math
from game import Game

pygame.init()

pygame.display.set_caption("GUERRE DE TERRITOIRE AU SOMMET DU TRÔNE")
screen = pygame.display.set_mode((1280, 520))

background = pygame.image.load('../assets/images/background/game_background.png')
banner = pygame.image.load('../assets/images/ui/banner.png')
banner = pygame.transform.scale(banner, (1280, 520))
banner_rect = banner.get_rect()

play_button = pygame.image.load('../assets/images/ui/button_start.png')
play_button = pygame.transform.scale(play_button, (230, 80))
play_button_rect = play_button.get_rect()

# Pour placer l'image au milieu de l'écran
play_button_rect.x = math.ceil(screen.get_width() / 2.35)
play_button_rect.y = math.ceil(screen.get_height() / 2.2)

game = Game()
game.sound_manager.play('beginning_music')

running = True
while running :

    # Appliquer la fenêtre et la musique du jeu
    screen.blit(background, (0, 0))

    # Déclencher les instructions de la partie si notre jeu a commencé
    if game.is_playing :
        game.update(screen)
    else :
        screen.blit(banner, (0, 0))
        screen.blit(play_button, play_button_rect)

    # Mettre à jour l'écran
    pygame.display.flip()

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
            pygame.quit()
        
        elif event.type == pygame.KEYDOWN :
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE :
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP :
            game.pressed[event.key] = False

        # Lance le jeu si on clique sur le bouton start
        elif event.type == pygame.MOUSEBUTTONDOWN :
            if play_button_rect.collidepoint(event.pos) :
                game.start()
                game.sound_manager.play('damage_taken_sfx', False)
