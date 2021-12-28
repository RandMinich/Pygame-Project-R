import pygame

import Levels

pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


class game:  # это тело игры, в него заносятся уровни
    def __init__(self, size):
        self.Level_load_stack = []
        self.screen = pygame.display.set_mode(size)

    def add_level(self, level):
        self.Level_load_stack.append(level)

    def run(self, size_of_button):
        Levels.run(self.screen, size_of_button, clock)

        for level in self.Level_load_stack:
            level.run_level()

    def settings_of_button(self):
        self.up = pygame.K_w
        self.down = pygame.K_s
        self.right = pygame.K_a
        self.left = pygame.K_d

    def change_settings(self, name, key):
        if name == 'up':
            self.up = key
        if name == 'down':
            self.down = key
        if name == 'left':
            self.left = key
        if name == 'right':
            self.right = key
