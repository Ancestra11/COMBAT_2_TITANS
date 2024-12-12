import pygame

class AnimateSprite(pygame.sprite.Sprite) :

	def __init__(self, dir_name, sprite_name, image_sum) :
		super().__init__()
		self.image = pygame.image.load(f'../assets/images/sprites/{dir_name}/{sprite_name}1.png')
		self.current_image = 0

		self.images = animations.get(dir_name)

	def animate(self, size) :
		self.current_image += 0.15

		# Si on a atteint la fin de l'animation
		if self.current_image >= len(self.images) :
			self.current_image = 0

		self.image = self.images[int(self.current_image)]
		self.image = pygame.transform.scale(self.image, size)

# Boucle sur chaque image d'un dossier pour animer les sprites
def load_animation_images(dir_name, sprite_name, image_sum) :
	images = []
	path = f"../assets/images/sprites/{dir_name}/{sprite_name}"

	for image_number in range(1, image_sum + 1) :
		image_path = path + str(image_number) + '.png'
		images.append(pygame.image.load(image_path))
	return images

animations = {
	'pepe': load_animation_images('pepe', 'pepe_idle_gauche', 2),
	'spiritomb': load_animation_images('spiritomb', 'spiritomb', 112),
	#'player': load_animation_images('player', 'rayman_shoot', 0)
}