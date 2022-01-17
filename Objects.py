import pygame

import Load_image
import main


class Abstract_Object(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = Load_image.load_image(image)


class Abstract_Phisical_Object(Abstract_Object):
    def __init__(self, image, hp=100000):
        Abstract_Object.__init__(self, image)
        self.hp = hp

    def get_damage(self, damage):
        self.hp -= damage


class Moving_object(Abstract_Phisical_Object):
    def __init__(self, image, hp, columns, rows, pos):
        Abstract_Phisical_Object.__init__(self, image, hp)
        self.frames = []
        self.cut_sheet(Load_image.load_image(image), columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(pos[0], pos[1])
        self.vx = 0
        self.is_jumping = False
        self.vy = 9
        self.choose = 0
        self.motion_const = 20
        self.onGround = False

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

    def check_collide(self, all_object_groups):
        for group in all_object_groups:
            if pygame.sprite.spritecollideany(self, group) and group.sprites().count(self) == 0:
                return True
        return False

    def motion(self, all_object_groups):
        if self.rect.bottom < 656 and self.vy // abs(self.vy) == 1:
            if not self.check_collide(all_object_groups):
                self.rect = self.rect.move(0, self.vy)
        if not self.check_collide(all_object_groups):
            self.rect.move(self.vx, 0)
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]

    def update(self, all_object_groups):
        self.onGround = False
        self.motion(all_object_groups)
        if not self.onGround:
            self.vy += 9

    def hit(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))


class Player(Moving_object):
    def check_collide(self, all_object_groups):
        for platforms in all_object_groups:
            platforms = platforms.sprites()
            if self not in platforms:
                for p in platforms:
                    if self.rect.bottom > 656:
                        self.rect.bottom = 656
                        self.vy = 0
                        self.onGround = True
                    if self.rect.left <= 0 and self.vx < 0:
                        self.vx = 0
                    if self.rect.left >= main.size[0] and self.vx > 0:
                        self.vx = 0
                    if pygame.sprite.collide_rect(self, p):  # если есть пересечение  с игроком
                        if type(p) == Enemy:
                            self.get_damage(1)
                            if self.vx > 0:
                                self.rect.right = p.rect.left - 30
                            if self.vx < 0:
                                self.rect.right = p.rect.right - 30
                            if self.vy > 0:
                                self.rect.bottom = p.rect.top - 25
                        else:
                            if self.vx > 0:  # если движется вправо
                                self.rect.right = p.rect.left  # то не движется вправо

                            if self.vx < 0:  # если движется влево
                                self.rect.left = p.rect.right  # то не движется влево

                            if self.vy > 0:  # если падает вниз
                                self.rect.bottom = p.rect.top  # то не падает вниз
                                self.onGround = True  # и становится на что-то твердое
                                self.vy = 0  # и энергия падения пропадает

                            if self.vy < 0:  # если движется вверх
                                self.rect.top = p.rect.bottom  # то не движется вверх
                                self.vy = 0  # и энергия прыжка пропадает

    def motion(self, all_object_groups):
        self.rect = self.rect.move(0, self.vy)
        self.check_collide(all_object_groups)
        self.rect = self.rect.move(self.vx, 0)
        self.check_collide(all_object_groups)


class Enemy(Moving_object):
    pass
