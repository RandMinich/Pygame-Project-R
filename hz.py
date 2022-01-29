import pygame
import Levels
import Load_image
import Objects

pygame.init()
screen = pygame.display.set_mode((1024, 768))
pygame.display.set_caption('PyGame Project')
pygame.font.init()

background = Load_image.load_image('Level 2 (Background).png')
leveltext = Load_image.load_image('Level 2 (Text).png')
pumpkin = Load_image.load_image('Jack-o-lantern.png')
pumpkin = pygame.transform.scale(pumpkin, (80, 60))

screen.blit(background, (0, 0))
screen.blit(leveltext, (90, 130))
screen.blit(pumpkin, (652, 599))

boxes = pygame.sprite.Group()

leftbox = pygame.sprite.Sprite()
leftbox.image = Load_image.load_image('Box.png')
leftbox.rect = leftbox.image.get_rect()
boxes.add(leftbox)

leftbox.rect.x = 75
leftbox.rect.y = 607
boxes.draw(screen)

box = Objects.Moving_object('Box.png', hp=50, columns=1, rows=1, pos=(10, 10))
boxes.add(box)
rightbox = pygame.sprite.Sprite()
rightbox.image = Load_image.load_image('Box.png')
rightbox.rect = rightbox.image.get_rect()
boxes.add(rightbox)
rightbox.rect.x = 871
rightbox.rect.y = 607
boxes.draw(screen)

boxhp = 50
boxhp_font = pygame.font.SysFont('Leto Text Sans', 48)  # Font(None, 36)
boxhp_text = boxhp_font.render(str(boxhp), True,
                               (0, 128, 0))
screen.blit(boxhp_text, (leftbox.rect.x + 9, leftbox.rect.y - 40))
pygame.display.flip()


# screen.blit(background, (0, 0))
# screen.blit(pumpkin, (652, 599))
# boxes.draw(screen)
# screen.blit(boxhp_text, (leftbox.rect.x + 9, leftbox.rect.y - 40))
# pygame.display.flip()
# clock = pygame.time.Clock()
# while True:
#   screen.blit(background, (0, 0))
#  clock.tick(60)

# screen.blit(pumpkin, (652, 599))
# for event in pygame.event.get():
#   if event.type == pygame.QUIT:
#      pygame.quit()
# if event.type == pygame.KEYDOWN:
#    if event.key == pygame.K_LEFT:
# pygame.quit()
#       boxhp_font = pygame.font.SysFont('Leto Text Sans', 48)
#      boxhp= int(boxhp) - 1
#     boxhp_text = boxhp_font.render(str(boxhp), True,
#                                   (0, 128, 0))
#   screen.blit(boxhp_text, (leftbox.rect.x + 9, leftbox.rect.y - 40))

#                pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(100, 100, 100, 100))
#   boxes.update([boxes], [])
#  boxes.draw(screen)
# pygame.display.flip()


Level_2 = Levels.Level('Level 2 (Background).png')
Level_2.append_object(boxes)
Level_2.run_level(screen, True, weapons=[])
