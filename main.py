import pygame
import os
import random

pygame.init()

size = width, height = 500, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 20


class MySprite(pygame.sprite.Sprite):
    def __init__(self, *args):
        super().__init__(*args)

        file_bomb = os.path.join('data', 'bomb.png')
        image_bomb = pygame.image.load(file_bomb)
        image_bomb.convert_alpha()

        file_boom = os.path.join('data', 'boom.png')
        self.image_boom = pygame.image.load(file_boom)
        self.image_boom.convert_alpha()

        self.image = image_bomb
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - 60)
        self.rect.y = random.randrange(height - 57)

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(args[0].pos):
                self.image = self.image_boom


all_sprites = pygame.sprite.Group()

for i in range(20):
    MySprite(all_sprites)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            all_sprites.update(event)

    screen.fill('white')

    all_sprites.draw(screen)
    all_sprites.update()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
