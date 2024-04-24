import pygame as pg


pg.init()
screen = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
all_sprites = pg.sprite.Group()


game = True
while game:
    all_sprites.draw(screen)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False
            break
    pg.display.update()
    clock.tick(60)