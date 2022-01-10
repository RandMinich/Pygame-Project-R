import game
import pygame

buttons = [pygame.Rect(100, 100, 100, 100), pygame.Rect(100, 250, 100, 100), pygame.Rect(100, 300, 100, 100)]
if __name__ == '__main__':
    game = game.game((1000, 500 ))
    game.run(buttons)
