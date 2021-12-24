import pygame

import Load_image


class Abstract_Object:
    def __init__(self, image, group):
        pygame.sprite.Sprite.__init__(group)
        self.image = Load_image.load_image(image)


class Abstract_Phisical_Object:
    def __init__(self, image, group, hp=100000):
        Abstract_Object.__init__(self, image, group)
        self.hp = hp

    def get_damage(self, damage):
        self.hp -= damage


class Moving_object(Abstract_Phisical_Object):
    def get_damage(self, damage):
        self.hp -= damage

    def update(self, all_object_groups):
        rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, all_object_groups):
            rect = self.rect
        self.rect = rect
