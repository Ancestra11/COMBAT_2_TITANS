import pygame
import os, time
screensize = screenw, screenh = 1280, 520
screen = pygame.display.set_mode(screensize)

class Entity(pygame.sprite.Sprite) :

	def __init__(self, posx, posy, image) :

		pygame.sprite.Sprite.__init__(self)
		self.posx = posx
		self.posy = posy
		self.image = image
		self.all_images = []

	def getImage(self) :
		return self.image

	def getPos(self) :
		return [self.posx, self.posy]

	def getY(self) :
		return self.posy

	def setX(self, posx) :
		self.posx = posx

	def setY(self, posy) :
		self.posy = posy

	def anim(self, path, name) :
		self.path = path
		self.name = name

		for i in range(0, 222, 2) :
			img = pygame.image.load(os.path.join(self.path, self.name + str(i) + '.png')).convert()
			img.convert_alpha()  # optimise alpha
			self.all_images.append(img)
			self.image = self.all_images[0]
			self.rect = self.image.get_rect()
			screen.blit(pygame.transform.scale(self.image, (60, 60)), (self.posx, self.posy))
			self.image = int(self.all_images[0])
			pygame.display.update()
			print(i)
			i += 0.2

class Fighters(Entity) :

	def __init__(self, posx, posy, image,  width, height, health, max_health, speed) :

		super().__init__(posx, posy, image)
		self.width = width
		self.height = height
		self.health = health
		self.max_health = max_health
		self.speed = speed

	def getSize(self) :
		return self.width, self.height

	def getSpeed(self) :
		return self.speed
