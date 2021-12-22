import pygame

import Load_image


class Abstract_Object:
    def __init__(self, image, group):
        pygame.sprite.Sprite.__init__(group)
        self.image = Load_image.load_image(image)


class Abstract_Phisical_Object:
    def __init__(self, image, group, hp=100000):
        Abstract_Object.__init__(image, group)
        self.hp = hp


    def update(self, vertical_borders, horizontal_borders):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx
