import pygame

import Load_image
import game


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
        self.rect = self.rect.move(pos[0], pos[1])
        self.vx = 0
        self.vy = 8
        self.inventar = []
        self.choose = 0
        self.motion_const = 10

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

    def check_collide(self, all_object_groups, weapons_enemy, rect):
        if pygame.sprite.spritecollideany(self, all_object_groups):
            if pygame.sprite.spritecollideany(self, weapons_enemy):
                self.get_damage(weapons_enemy[0].damage)
                if self.hp <= 0:
                    pass
            rect = self.rect
        return rect

    def motion(self, all_object_groups, weapons_enemy):
        rect = self.rect.move(0, self.vy)
        self.rect = self.check_collide(all_object_groups, weapons_enemy, rect)
        rect = self.rect.move(self.vx, 0)
        self.rect = self.check_collide(all_object_groups, weapons_enemy, rect)
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]

    def update(self, all_object_groups, weapons_enemy):
        self.motion(all_object_groups, weapons_enemy)

    def hit(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))


class Player(Moving_object):
    def event(self, events):
        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == game.new_game.left:
                    self.vx = 0
                if event.key == game.new_game.right:
                    self.vx = 0
                if event.key == game.new_game.up:
                    self.vy = 0
                if event.key == game.new_game.left:
                    self.vy = 0
            if event.type == pygame.KEYDOWN:
                if event.key == game.new_game.left:
                    self.vx = self.motion_const
                if event.key == game.new_game.right:
                    self.vx = self.motion_const
                if event.key == game.new_game.up:
                    self.vy = 25
                if event.key == game.new_game.left:
                    self.vy = 25


class Weapon:
    def __init__(self, name, damage, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        self.frames = []
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))
        self.cur_farame = 0
        self.image = self.frames[self.cur_farame]
        self.damage = damage
        self.name = name


class Enemy(Moving_object):
    def update(self, all_object_groups, weapons_enemy, player_coords):
        vector = (player_coords[0] // abs(player_coords[0]), player_coords[1] // abs(player_coords[1]))
        self.vx = 5 * vector[0]
        self.vy = -9
        self.motion(all_object_groups, weapons_enemy)
