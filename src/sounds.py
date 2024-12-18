import pygame

'''
pygame.mixer.music.load() pour des fichiers audio longs, permet une gestion de la musique
pygame.mixer.Sound() pour des effets sonores courts qu'on peut jouer de manière rapide et répétée
'''
class SoundManager:

    def __init__(self):
        self.sounds = {
            'beginning_music': "../assets/sounds/beginning_music.mp3",
            'fighting_music': "../assets/sounds/fighting_music.mp3",
            'game_over_music':"../assets/sounds/game_over_music.mp3",
            'damage_taken_sfx': "../assets/sounds/damage_taken_sfx.wav",
            "rayman_punch_sfx": "../assets/sounds/rayman_punch_sfx.wav"

        }

    def play(self, name, is_music=True):

        if is_music :
            pygame.mixer.music.load(self.sounds[name])
            pygame.mixer.music.play(-1)
        else :
            sfx = pygame.mixer.Sound(self.sounds[name])
            sfx.set_volume(0.2)
            sfx.play()
