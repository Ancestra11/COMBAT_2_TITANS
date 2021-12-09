import sys, pygame      # threading.Thread(target=texte1, args=( ,))
from pygame.locals import *
import Audio, Characters #, Events, Commands
pygame.init()

# Objet de la musique de début de jeu (dans audio.py) :
s1 = Audio.Songs('../audio/Peacefulness.wav', -1)
s1.Starting_Song()

# Objet de la musique du combat (dans audio.py) :
# s2 = Audio.Songs('../audio/Epicness.wav', -1)
# s2.Fighting_Song()

# Objet musique de défaite :
#s3 = Audio.Songs('../audio/Sadness.wav', -1)
#s3.Defeat_Song()

pygame.display.set_caption("GUERRE DE TERRITOIRE AU SOMMET DU TRÔNE.")
screensize = screenw, screenh = 1280, 520
screen = pygame.display.set_mode(screensize)
clock = pygame.time.Clock()

# Importer images : 
Img_Spiritomb = '../images/bg/Spiritomb/Spiritomb0.png'
Spir = Characters.Entity(1035, 315, Img_Spiritomb)
LoadSpir = pygame.image.load(Img_Spiritomb)

Img_Pepe = '../images/target/AttenteVGF.png'
Pepe = Characters.Fighters(850, 290, Img_Pepe, 67, 195, 5, 5, 15)
LoadPepe = pygame.image.load(Img_Pepe)

background = pygame.image.load('../images/bg/bg_image.png').convert()

Img_Rayman = '../images/player/Rayman.png'
Rayman = Characters.Fighters(120, 370, Img_Rayman, 90, 90, 3, 5, 15)
LoadRayman = pygame.image.load(Img_Rayman)

Img_SCP = '../images/bg/SCP087.png'
SCP = Characters.Entity(34, 200, Img_SCP)
LoadSCP = pygame.image.load(Img_SCP)

running = True
pygame.key.set_repeat(2, 50) # ( Délai avant de continuer mouvement, temps entre chaque déplacement)

while running == True :

    # (pygame.transform.scale(NomImage, (LargeImg, HauteImg)), (PositionImg += vers droite, PosImg += vers bas)
    #Spir.anim('../images/bg/Spiritomb/', 'Spiritomb')

    screen.blit(background, (0, 0))
    screen.blit(pygame.transform.scale(LoadSCP, (30, 30)), SCP.getPos())
    screen.blit(pygame.transform.scale(LoadSpir, (60, 60)), Spir.getPos())
    screen.blit(pygame.transform.scale(LoadRayman, Rayman.getSize()), Rayman.getPos())
    screen.blit(pygame.transform.scale(LoadPepe, Pepe.getSize()), Pepe.getPos())

    #Spir.anim('../images/bg/Spiritomb/', 'Spiritomb')

    for event in pygame.event.get() :

        if event.type == KEYDOWN and event.key == K_RIGHT and Rayman.getPos()[0] + 10 < 1210 :
            Rayman.setX(Rayman.getPos()[0] + Rayman.getSpeed() )

        if event.type == KEYDOWN and event.key == K_LEFT and Rayman.getPos()[0] - 10 > -15 :
            Rayman.setX(Rayman.getPos()[0] - Rayman.getSpeed())

        if event.type == KEYDOWN and event.key == K_UP and Rayman.getY() - 10 > -10 :
            Rayman.setY(Rayman.getPos()[1] - Rayman.getSpeed())

        clock.tick(50)
        if event.type == pygame.QUIT :
            running = False

        pygame.display.update()
    
