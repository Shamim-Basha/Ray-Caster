def draw_bg(screen):
    screen.fill("#000000")
    screen.fill("#00ee00",(screen.get_width()//2,0,screen.get_width()//2,screen.get_height()))
    screen.fill("#aa0000",(screen.get_width()//2,screen.get_height()//2-10,screen.get_width()//2,screen.get_height()//2+10))
    