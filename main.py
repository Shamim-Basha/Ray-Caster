import pygame

from player import Player
from map import Map

from utils import draw_bg

pygame.init()

WIDTH = 1200
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))

player = Player(300,300,screen)

map = Map(screen)
map.create_tiles()

player.create_rays(map.tile_size,map.tiles_pos)

running = True
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial",20,1)
while running:
    clock.tick(60)
    text = font.render("FPS: "+str(int(clock.get_fps())),1,"#ff0000")
    draw_bg(screen)
    map.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    player.update()
    map.event_handler(event)
    player.event_handler(event,map.tile_size,map.tiles_pos)
    player.render()
    screen.blit(text,((WIDTH/2)+10,10))
    # print(text)
    pygame.display.update()
pygame.quit()