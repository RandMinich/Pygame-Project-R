import game
import pygame

buttons = [pygame.Rect(300, 300, 100, 50), pygame.Rect(300, 400, 100, 50), pygame.Rect(300, 800, 100, 100)]
if __name__ == '__main__':
    game = game.game((1000, 500))
    game.run(buttons)
