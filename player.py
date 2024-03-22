import math
import pygame

class Player:
    def __init__(self,x,y,screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.angle = 0
        self.speed = 10
        self.no_of_rays = 600
        self.rays = []
        self.ray_lens = []
        self.size = 20
    
    def draw(self):
        for ray in [self.rays[0],self.rays[-1]]:
            pygame.draw.line(self.screen,"#ffffff",(self.x,self.y),ray)
        pygame.draw.circle(self.screen,"#ff0000",(self.x,self.y),self.size//2)
            
    def update(self,event = None):
        self.draw()

        
    def create_rays(self,tile_size,tiles):
        rays = []
        self.ray_lens = []
        dQ = 360/self.no_of_rays
        theta = self.angle - 30
        
        def calculate_distance_from_center(x,y):
            return math.sqrt((self.x-x)**2 + (self.y-y)**2) 
        
        while theta <= self.angle+30:
            x,y = self.x,self.y
            while (0<=x<self.screen.get_width() and 0<=y<self.screen.get_height()):
                x += math.sin(math.radians(theta))
                y -= math.cos(math.radians(theta))
                x0,y0 = tile_size*(x//tile_size) , tile_size*(y//tile_size)
                if (x0,y0) in tiles:
                    break
            rays.append((x,y))
            self.ray_lens.append((calculate_distance_from_center(x,y),theta))
            theta += dQ
        self.rays = rays

    def check_Collision(self,tile_size,tiles):
        x0,y0 = tile_size*(self.x//tile_size), tile_size*(self.y//tile_size)
        if (x0,y0) in tiles:
            return True
        return False

    def render(self):
        len_arr = self.ray_lens
        width,height = self.screen.get_size()
        width = width//2
        x = width
        scale = width/self.no_of_rays*6
        for i,angle in len_arr:
            color = 255 / (1 + i * i * 0.0001)
            i *= abs(math.cos(math.radians(self.angle - angle)))
            wall_height = 12000/(i+0.0001)
            rect = pygame.Rect(x,(height/2)-wall_height/2,scale,wall_height)
            pygame.draw.rect(self.screen,(color,color,color),rect)
            x += scale
    
    def event_handler(self,event,tile_size,tiles):
        keys = pygame.key.get_pressed()
        x0,y0 = self.x,self.y
        moved = False
        if keys[pygame.K_w]:
            self.x += self.speed*(math.cos(math.radians(90-self.angle)))
            self.y -= self.speed*(math.sin(math.radians(90-self.angle)))
            moved = True
        if keys[pygame.K_s]:
            self.x -= self.speed*(math.cos(math.radians(90-self.angle)))
            self.y += self.speed*(math.sin(math.radians(90-self.angle)))
            moved = True
        if keys[pygame.K_UP]:
            self.no_of_rays += 10
        if keys[pygame.K_DOWN]:
            self.no_of_rays -= 10
        if keys[pygame.K_a]:
            self.angle -= 5
            moved = True
        if keys[pygame.K_d]:
            self.angle += 5
            moved = True
        if moved:
            if self.check_Collision(tile_size,tiles):
                self.x,self.y = x0,y0
            self.create_rays(tile_size,tiles)
        