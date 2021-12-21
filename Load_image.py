import os
import sys
import pygame


def load_image(name, colorkey=None): # функция для правильной загрузки изображений
    fullname = os.path.join('data', name) # создаём путь к файлу с изображением
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден") # проверка на идиота
        sys.exit()
    image = pygame.image.load(fullname) # загрузка
    return image # отдаем
