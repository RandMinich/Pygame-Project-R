import pygame
import pygame_gui

import Load_image


def start_window(screen, button_sizes, clock):
    window_res = 800, 600
    gui_manager = pygame_gui.UIManager(window_resolution=window_res)
    start_button = pygame_gui.elements.UIButton(button_sizes[0], text='Start', manager=gui_manager)
    running = True
    new_game = False
    exit_button = pygame_gui.elements.UIButton(button_sizes[1], text='Exit', manager=gui_manager)
    while running:
        screen.fill((0, 0, 0))
        td = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == start_button:
                        new_game = True
                        running = False
                    if event.ui_element == exit_button:
                        running = False

            gui_manager.process_events(event)
            gui_manager.update(td)
        gui_manager.draw_ui(screen)
        pygame.display.flip()
    return new_game


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
