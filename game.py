import pygame

import Levels

pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


class game:  # это тело игры, в него заносятся уровни
    def __init__(self, size):
        self.dead_persons = -1
        self.Level_load_stack = []
        self.screen = pygame.display.set_mode(size)
        self.size = size

    def add_level(self, level):
        self.Level_load_stack.append(level)

    def run(self, size_of_buttons):
        flag = False
        flag = Levels.start_window(self.screen, size_of_buttons, clock, self.size)
        if flag:
            for level in self.Level_load_stack:
                level.run_level(screen, True, weapons=[])
            Levels.end_screen(self.screen, size_of_buttons, clock, self.dead_persons, self.size)
