import pygame
import pygame_gui

import Load_image
import Objects


def start_window(screen, button_sizes, clock):
    window_res = 800, 600
    gui_manager = pygame_gui.UIManager(window_resolution=window_res)
    start_button = pygame_gui.elements.UIButton(button_sizes[0], text='Start', manager=gui_manager)
    running = True

    bcg_group = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    background = pygame.sprite.Sprite()
    background.image = Load_image.load_image('file.png')
    test_sprite = Objects.Moving_object('test.png', rows=8, columns=9, hp=100, pos=(50, 50))
    enemies.add(test_sprite)
    background.rect = pygame.Rect(-1, -1, 2000, 20000)
    bcg_group.add(background)
    new_game = False
    exit_button = pygame_gui.elements.UIButton(button_sizes[1], text='Exit', manager=gui_manager)
    while running:
        bcg_group.draw(screen)
        enemies.draw(screen)
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
        self.objects.append(object)  # здесь должны быть группы спрайтов в качестве объектов

    def run_level(self, screen, is_running_flag):
        self.running = is_running_flag

        while self.running:
            screen.blit(self.bgi, 0, 0)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.pause()
            for group in self.objects:
                group.update()
                group.draw()
            pygame.display.flip()

    def pause(self, screen):
        non_break = True
        buttons = [pygame.Rect(300, 300, 100, 50), pygame.Rect(300, 400, 100, 50), pygame.Rect(300, 800, 100, 100)]
        gui_manager = pygame_gui.UIManager(window_resolution=(1000, 500))
        start_button = pygame_gui.elements.UIButton(buttons[0], text='Continue', manager=gui_manager)
        exit_button = pygame_gui.elements.UIButton(buttons[0], text='Exit', manager=gui_manager)
        while non_break:
            td = clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        non_break = False
                    if event.type == pygame.USEREVENT:
                        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                            if event.ui_element == start_button:
                                non_break = False
                            if event.ui_element == exit_button:
                                non_break = False
                                self.running = False

                    gui_manager.process_events(event)
                    gui_manager.update(td)
                gui_manager.draw_ui(screen)
                pygame.display.flip()

