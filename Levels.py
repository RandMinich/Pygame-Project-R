import Load_image
import pygame


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
