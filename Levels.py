import pygame
import pygame_gui

import Load_image

window_res = 800, 600
gui_manager = pygame_gui.UIManager(window_resolution=window_res)


class Level:
    def __init__(self, gravity, background_image):
        self.bgi = Load_image.load_image(background_image)
        self.gravity = gravity
        self.objects = []
        self.running = False

    def append_object(self, object):
        self.objects.append(object)

    def run_level(self, screen, is_running_flag):
        self.running = is_running_flag
        while self.running:
            screen.blit(self.bgi, 0, 0)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            for group in self.objects:
                group.update()
                group.draw()


class Start_screen:
    def run(self, screen, start_pos, rect, ):
        start_button = pygame_gui.elements.UIButton(rect, text='Start', manager=gui_manager)
        running = True
        new_game = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == start_button:
                            new_game = True
                            running = False
            gui_manager.update(0.00001)
            gui_manager.draw_ui(screen)
