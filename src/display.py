import pygame 

class Display:

    def __init__(self, width, height, fps):
        self.width = width 
        self.height = height 
        self.fps = fps 
        self.clock = pygame.time.Clock()   
        self.win = pygame.display.set_mode((width, height))

    def clear(self):
        self.win.fill((0,0,0))

    def update(self):
        pygame.display.update() 
        self.clock.tick(self.fps)

    def get_screen(self):
        return self.win
