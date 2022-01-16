import sqlite3

import pygame
import pygame_gui

import Load_image
import main


def start_window(screen, button_sizes, clock, size):
    window_res = size
    gui_manager = pygame_gui.UIManager(window_resolution=window_res)
    start_button = pygame_gui.elements.UIButton(button_sizes[0], text='Start', manager=gui_manager)
    running = True
    font = pygame.font.Font('C:/Users/yuryk/PycharmProjects/Pygame-Project-R/data/BreakPassword.otf', 100)
    bcg_group = pygame.sprite.Group()
    background = pygame.sprite.Sprite()
    background.image = Load_image.load_image('file.png')
    background.rect = pygame.Rect(-1, -1, 2000, 20000)
    bcg_group.add(background)
    new_game = False
    exit_button = pygame_gui.elements.UIButton(button_sizes[1], text='Exit', manager=gui_manager)
    Game_Name = font.render('Rabbit Knight', True, (0, 0, 0))
    while running:
        bcg_group.draw(screen)
        screen.blit(Game_Name, (100, 150))
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


def end_screen(screen, button_sizes, clock, dead_persons, size):
    screen.fill((0,0,0))
    window_res = size
    gui_manager = pygame_gui.UIManager(window_resolution=window_res)
    running = True
    bcg_group = pygame.sprite.Group()
    background = pygame.sprite.Sprite()
    background.image = Load_image.load_image('file.png')
    background.rect = pygame.Rect(-1, -1, 2000, 20000)
    bcg_group.add(background)
    exit_button = pygame_gui.elements.UIButton(button_sizes[1], text='Exit', manager=gui_manager)
    text = ''

    font = pygame.font.Font('C:/Users/yuryk/PycharmProjects/Pygame-Project-R/data/BreakPassword.otf', 50)
    con = sqlite3.connect("winners.db")
    cur = con.cursor()
    results = cur.execute("""SELECT Name FROM winners ORDER BY Result""").fetchall()[-1:-6:-1]

    while running:
        bcg_group.draw(screen)
        td = clock.tick(60) / 1000.0
        for i in range(len(results)):
            screen.blit(font.render(results[i][0], True, (0, 0, 0)), (250, 50 * (i + 2)))
        screen.blit(font.render(text, True, (0, 0, 0)), (300, 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if text == '':
                        pass
                    else:
                        text = text[:-1]
                if event.key == 13:
                    cur.execute("""INSERT INTO winners(Name, Result) VALUES(?, ?) """, (text, dead_persons))
                    con.commit()
                    running = False
                if event.unicode in main.symbols:
                    text += event.unicode
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == exit_button:
                        running = False
            gui_manager.process_events(event)
            gui_manager.update(td)
        gui_manager.draw_ui(screen)
        pygame.display.flip()


class Level:
    def __init__(self, background_image, player_group):
        self.bgi = Load_image.load_image(background_image)
        self.objects = []
        self.running = False
        self.clock = pygame.time.Clock()
        self.player_group = player_group

    def append_object(self, object):
        self.objects.append(object)  # здесь должны быть группы спрайтов в качестве объектов

    def run_level(self, screen, is_running_flag, weapons):
        self.running = is_running_flag
        self.clock.tick(60)
        while self.running:
            screen.blit(self.bgi, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.pause(screen)
                    if event.key == pygame.K_a:
                        self.player_group.sprites()[0].vx = -1 * self.player_group.sprites()[0].motion_const
                    if event.key == pygame.K_d:
                        self.player_group.sprites()[0].vx = self.player_group.sprites()[0].motion_const
                    if event.key == pygame.K_w and not self.player_group.sprites()[0].is_jumping:
                        self.player_group.sprites()[0].vy = -25
                        self.player_group.sprites()[0].is_jumping = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.player_group.sprites()[0].vx = 0
                    if event.key == pygame.K_d:
                        self.player_group.sprites()[0].vx = 0
            for group in self.objects:
                group.update(self.objects, weapons)
                group.draw(screen)
            pygame.display.flip()

    def pause(self, screen):
        non_break = True
        buttons = [pygame.Rect(300, 300, 100, 50), pygame.Rect(300, 400, 100, 50), pygame.Rect(300, 800, 100, 100)]
        gui_manager = pygame_gui.UIManager(window_resolution=(1000, 500))
        start_button = pygame_gui.elements.UIButton(buttons[0], text='Continue', manager=gui_manager)
        restart_button = pygame_gui.elements.UIButton(buttons[2], text='Restart', manager=gui_manager)
        exit_button = pygame_gui.elements.UIButton(buttons[1], text='Exit', manager=gui_manager)
        while non_break:
            td = self.clock.tick(60) / 1000.0
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
                        if event.ui_element == restart_button:
                            self.run_level(screen, is_running_flag=True, weapons=[])
                gui_manager.process_events(event)
                gui_manager.update(td)
                gui_manager.draw_ui(screen)
                pygame.display.flip()
