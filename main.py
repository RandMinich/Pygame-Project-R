import pygame
import Objects
import Levels
import game

size = (1024, 768)
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6',
           '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a',
           'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
           'x', 'y', 'z', '{', '|', '}', '~']
buttons = [pygame.Rect(300, 300, 100, 50), pygame.Rect(300, 400, 100, 50), pygame.Rect(470, 500, 100, 50)]
if __name__ == '__main__':
    game = game.game(size)
    player = Objects.Player('Box.png', hp=10, columns=1, rows=1, pos=(100, 100))
    player_g = pygame.sprite.Group()
    player_g.add(player)
    hole1 = Objects.Moving_object('Hole.png', columns=1, rows=1, hp=1, pos=(200, 200))

    hole1_group = pygame.sprite.Group()
    hole1_group.add(hole1)
    Level_2 = Levels.Level('Level 2 (Background).png', player_g,hole1_group)
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption('PyGame Project')

    # Загрузка изображений и их масштабирование
    # leveltext = pygame.image.load('Level 2 (Background).png')
    # pumpkin = pygame.image.load('Jack-o-lantern.png')
    # pumpkin = pygame.transform.scale(pumpkin, (80, 60))
    # hole = pygame.image.load('Hole.png')
    # arrow = pygame.image.load('Arrow.png')
    # hole_object = Objects.Abstract_Object('Hole.png')
    # arrow_object = Objects.Abstract_Object('Arrow.png')

    # screen.blit(background, (0, 0))
    # screen.blit(leveltext, (90, 130))
    # screen.blit(pumpkin, (652, 599))
    # screen.blit(hole, (950, 645))
    # screen.blit(arrow, (930, 430))

    leftbox_group = pygame.sprite.Group()

    leftbox = Objects.Moving_object('Box.png', hp=50, columns=1, rows=1, pos=(75, 607))
    # leftbox.image = ('Box.png')
    # leftbox.rect = leftbox.image.get_rect()
    leftbox_group.add(leftbox)
    # leftbox.rect.x = 75
    # leftbox.rect.y = 607

    rightbox_group = pygame.sprite.Group()

    rightbox = Objects.Moving_object('Box.png', hp=50, columns=1, rows=1, pos=(871, 607))
    # rightbox.image = pygame.image.load('Box.png')
    # rightbox.rect = rightbox.image.get_rect()
    rightbox_group.add(rightbox)
    # rightbox.rect.x = 871
    # rightbox.rect.y = 607

    topleftbox_group = pygame.sprite.Group()

    topleftbox = Objects.Moving_object('Box.png', hp=50, columns=1, rows=1, pos=(340, 408))
    # topleftbox.image = pygame.image.load('Box.png')
    # topleftbox.rect = topleftbox.image.get_rect()
    topleftbox_group.add(topleftbox)
    # topleftbox.rect.x = 340
    # topleftbox.rect.y = 408

    topleftbox1_group = pygame.sprite.Group()

    topleftbox1 = Objects.Moving_object('Box.png', hp=50, columns=1, rows=1, pos=(340, 458))
    # topleftbox1.image = pygame.image.load('Box.png')
    # topleftbox1.rect = topleftbox1.image.get_rect()
    topleftbox1_group.add(topleftbox1)
    # topleftbox1.rect.x = 340
    # topleftbox1.rect.y = 458

    topleftbox2_group = pygame.sprite.Group()

    topleftbox2 = Objects.Moving_object('Box.png', hp=50, columns=1, rows=1, pos=(340, 508))
    # topleftbox2.image = pygame.image.load('Box.png')
    # topleftbox2.rect = topleftbox2.image.get_rect()
    topleftbox2_group.add(topleftbox2)
    # topleftbox2.rect.x = 340
    # topleftbox2.rect.y = 508

    topleftbox3_group = pygame.sprite.Group()

    topleftbox3 = Objects.Moving_object('Box.png', hp=50, columns=1, rows=1, pos=(340, 558))
    # topleftbox3.image = pygame.image.load('Box.png')
    # topleftbox3.rect = topleftbox3.image.get_rect()
    topleftbox3_group.add(topleftbox3)
    # topleftbox3.rect.x = 340
    # topleftbox3.rect.y = 558

    topleftbox4_group = pygame.sprite.Group()

    topleftbox4 = Objects.Moving_object('Box.png', hp=50, columns=1, rows=1, pos=(340, 608))
    # topleftbox4.image = pygame.image.load('Box.png')
    # topleftbox4.rect = topleftbox4.image.get_rect()
    topleftbox4_group.add(topleftbox4)
    # topleftbox4.rect.x = 340
    # topleftbox4.rect.y = 608


    toprightbox_group = pygame.sprite.Group()

    toprightbox = Objects.Moving_object('Box.png', hp=50, columns=1, rows=1, pos=(530, 358))
    # toprightbox.image = pygame.image.load('Box.png')
    # toprightbox.rect = toprightbox.image.get_rect()
    toprightbox_group.add(toprightbox)
    # toprightbox.rect.x = 530
    # toprightbox.rect.y = 358

    toprightbox1_group = pygame.sprite.Group()

    toprightbox1 = Objects.Moving_object('Box.png', hp=50, columns=1, rows=1, pos=(530, 408))
    # toprightbox1.image = pygame.image.load('Box.png')
    # toprightbox1.rect = toprightbox1.image.get_rect()
    toprightbox1_group.add(toprightbox1)
    # toprightbox1.rect.x = 530
    # toprightbox1.rect.y = 408

    toprightbox2_group = pygame.sprite.Group()

    toprightbox2 = Objects.Moving_object('Box.png', hp=50, columns=1, rows=1, pos=(530, 458))
    # toprightbox2.image = pygame.image.load('Box.png')
    # toprightbox2.rect = toprightbox2.image.get_rect()
    toprightbox2_group.add(toprightbox2)
    # toprightbox2.rect.x = 530
    # toprightbox2.rect.y = 458

    toprightbox3_group = pygame.sprite.Group()

    toprightbox3 = Objects.Moving_object('Box.png', hp=50, columns=1, rows=1, pos=(530, 508))
    # toprightbox3.image = pygame.image.load('Box.png')
    # toprightbox3.rect = toprightbox3.image.get_rect()
    toprightbox3_group.add(toprightbox3)
    # toprightbox3.rect.x = 530
    # toprightbox3.rect.y = 508

    toprightbox4_group = pygame.sprite.Group()

    toprightbox4 = Objects.Moving_object('Box.png', hp=50, columns=1, rows=1, pos=(530, 558))
    # toprightbox4.image = pygame.image.load('Box.png')
    # toprightbox4.rect = toprightbox4.image.get_rect()
    toprightbox4_group.add(toprightbox4)
    # toprightbox4.rect.x = 530
    # toprightbox4.rect.y = 558

    toprightbox5_group = pygame.sprite.Group()

    toprightbox5 = Objects.Moving_object('Box.png', hp=50, columns=1, rows=1, pos=(530, 608))
    # toprightbox5.image = pygame.image.load('Box.png')
    # toprightbox5.rect = toprightbox5.image.get_rect()
    toprightbox5_group.add(toprightbox5)
    # toprightbox5.rect.x = 530
    # toprightbox5.rect.y = 608

    Level_2.append_object(leftbox_group)
    Level_2.append_object(rightbox_group)

    Level_2.append_object(topleftbox_group)
    Level_2.append_object(topleftbox1_group)
    Level_2.append_object(topleftbox2_group)
    Level_2.append_object(topleftbox3_group)
    Level_2.append_object(topleftbox4_group)

    Level_2.append_object(toprightbox_group)
    Level_2.append_object(toprightbox1_group)
    Level_2.append_object(toprightbox2_group)
    Level_2.append_object(toprightbox3_group)
    Level_2.append_object(toprightbox4_group)
    Level_2.append_object(toprightbox5_group)
    Level_2.append_object(player_g)

    game.add_level(Level_2)
    game.run(buttons)
