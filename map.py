import pygame
import json

class Map:
    def __init__(self,screen) -> None:
        self.tiles = []
        self.tile_size = 40
        self.tiles_pos = []
        self.screen = screen
        
    def draw(self):
        x,y = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        for tile in self.tiles:
            pygame.draw.rect(self.screen,"#00ff00",(tile["pos"][0],tile["pos"][1],self.tile_size,self.tile_size))
        if keys[pygame.K_LSHIFT]:
            pygame.draw.rect(self.screen,"#00ff00",(self.tile_size*(x//self.tile_size),self.tile_size*(y//self.tile_size),self.tile_size,self.tile_size))
    
    def create_tiles(self):
        width,height = self.screen.get_size()
        width = width//2
        for i in range(width//self.tile_size):
            self.tiles.append({"pos":(i*self.tile_size,0)})
            self.tiles.append({"pos":(i*self.tile_size,height-self.tile_size)})
            
            self.tiles_pos.append((i*self.tile_size,0))
            self.tiles_pos.append((i*self.tile_size,height-self.tile_size))
        for i in range(height//self.tile_size):
            self.tiles.append({"pos":(0,i*self.tile_size)})
            self.tiles.append({"pos":(width-self.tile_size,i*self.tile_size)})
            
            self.tiles_pos.append((0,i*self.tile_size))
            self.tiles_pos.append((width-self.tile_size,i*self.tile_size))
    
    def event_handler(self,event):
        keys = pygame.key.get_pressed()
        x,y = pygame.mouse.get_pos()
        l,_,r = pygame.mouse.get_pressed()
        if keys[pygame.K_LSHIFT] and l:
            self.tiles.append({"pos":(self.tile_size*(x//self.tile_size),self.tile_size*(y//self.tile_size))}) 
            self.tiles_pos.append((self.tile_size*(x//self.tile_size),self.tile_size*(y//self.tile_size))) 
        if keys[pygame.K_LSHIFT] and r:
            try:
                self.tiles.remove({"pos":(self.tile_size*(x//self.tile_size),self.tile_size*(y//self.tile_size))}) 
                self.tiles_pos.remove((self.tile_size*(x//self.tile_size),self.tile_size*(y//self.tile_size))) 
            except:
                pass
        if keys[pygame.K_ESCAPE]:
            with open("map.json","w") as f:
                json.dump(self.tiles,f)
    