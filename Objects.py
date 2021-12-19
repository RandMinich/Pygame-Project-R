import pygame

import Load_image


class Abstract_Object:
    def __init__(self, image, pos_l, group):
        pygame.sprite.Sprite.__init__(group)
        self.image = Load_image.load_image(image)
