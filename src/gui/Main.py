import sys, pygame		# threading.Thread(target=texte1, args=( ,))
import Audio, Characters #, Events, Commands

from pygame import mixer
from pygame.locals import *

pygame.init()

# Objet de la musique de début de jeu (dans audio.py) :
s1 = Audio.Songs('../audio/Peacefulness.wav',-1)
s1.Starting_Song()

# Objet de la musique du combat (dans audio.py) :
# s2 = Audio.Songs('../audio/Epicness.wav', -1)
# s2.Fighting_Song()

# Objet musique de défaite :
#s3 = Audio.Songs('../audio/Sadness.wav', -1)
#s3.Defeat_Song()

# Générer fenêtre de jeu :

pygame.display.set_caption("GUERRE DE TERRITOIRE AU SOMMET DU TRÔNE.")  # display = affichage, set_caption = titre(s)
screensize = screenw, screenh = 1280, 520
screen = pygame.display.set_mode(screensize) # set_mode = affichage de la fenêtre (taille)

# Affiche = screen.blit(pygame.transform.scale())

background = pygame.image.load('../images/bg/bg_image.png').convert()

Img_Rayman = pygame.image.load('../images/player/Rayman.png') # déclaration image du perso
SCP = pygame.image.load('../images/bg/SCP087.png')

Img_Spiritomb = ('../images/bg/Spiritomb/Spiritomb0.png')
Spir = Characters.Entity(1035, 315, Img_Spiritomb)

x_Img_Rayman = 120
y_Img_Rayman = 370

Img_Pepe = ('../images/target/AttenteVGF.png')
Pepe = Characters.Fighters(850, 290, Img_Pepe, 5, 5, 15)
LoadPepe = pygame.image.load(Img_Pepe)

running = True # running = Nom de la boucle while ? While ne marche pas toute seule, booléen True = strict minimum

pygame.display.update()
pygame.key.set_repeat(2, 50) # ( Délai avant de continuer mouvement, temps entre chaque déplacement)

while running == True :

	# blit() = afficher image,         
	#(pygame.transform.scale(NomImage, (TailleImg, tailleImg)), (PositionImg += vers droite, PosImg += vers bas)

    screen.blit(background, (0,0))
    screen.blit(pygame.transform.scale(SCP, (30,30)), (34,200))
    screen.blit(pygame.transform.scale(Spir.loadImage(), (60,60)), (Spir.getX(), Spir.getY()))
    screen.blit(pygame.transform.scale(Img_Rayman, (90,90)), (x_Img_Rayman,y_Img_Rayman))
    # screen.blit(pygame.transform.scale(Rayman.getImage(), (90,90)),(Rayman.getX(), Rayman.getY()))

    screen.blit(pygame.transform.scale(LoadPepe, (67, 195)), (Pepe.getX(), Pepe.getY()))

    for event in pygame.event.get() :

        if event.type == KEYDOWN and event.key == K_RIGHT and x_Img_Rayman + 10 < 1210 :
            x_Img_Rayman = x_Img_Rayman + 15

        if event.type == KEYDOWN and event.key == K_LEFT and x_Img_Rayman - 10 > -15 :
            x_Img_Rayman = x_Img_Rayman - 15

        if event.type == KEYDOWN and event.key == K_UP and y_Img_Rayman - 10 > -10 :
            y_Img_Rayman = y_Img_Rayman - 15

        if event.type == pygame.QUIT :
            running = False

        pygame.display.update()
    
