import pygame

pygame.init()

class Songs :

	def __init__(self, load, play) :

		self.load = load
		self.play = play

	def Starting_Song(self) : # Peacefulness.mp3

		pygame.mixer.music.load(self.load)
		pygame.mixer.music.play(self.play)

	def Fighting_Song(self) : # Epicness.mp3

		pygame.mixer.music.load(self.load)
		pygame.mixer.music.play(self.play)

	def Defeat_Song(self) : # Sadness.mp3

		pygame.mixer.music.load(self.load)
		pygame.mixer.music.play(self.play)

	def Victory_Song(self) :

		pygame.mixer.music.load(self.load)
		pygame.mixer.music.play(self.play)
		
#s1 = Songs('../audio/peacefulness.mp3',-1)
#s1.Starting_Song()
