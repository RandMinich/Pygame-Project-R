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
    def __init__(self, image, group, hp, columns, rows, pos):
        Abstract_Phisical_Object.__init__(image, group, hp)
        self.frames = []
        self.cut_sheet(image, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(pos[0], pos[1])

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))


    def get_damage(self, damage):
        self.hp -= damage


    def update(self, all_object_groups):
        rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, all_object_groups):
            rect = self.rect
        self.rect = rect
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]

    def hit(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

