#!/usr/local/bin/python3.9

import sys 
import pygame 
import field
import display 

class App:

    def __init__(self):
        self.disp = display.Display(600, 600, 60)
        self.field = field.Field()
        self.main()
        
    def main(self):
        while True: 
            self.disp.clear() 
            self.event_handler() 
            self.field.draw(self.disp.get_screen())
            self.disp.update()

    def event_handler(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_x:
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0): 
                    mouse_pos = pygame.mouse.get_pos()
                    for row in self.field.cells:
                        for cell in row:
                            if cell.collide(*mouse_pos): 
                                cell.is_start_node = True 
                                cell.color = (0, 0, 255)
                    for row in self.field.cells:
                        for cell in row:
                            if cell.is_start_node:
                                pass
                            else:
                                cell.calculate_g_cost(self.field.grid)
                if pygame,mouse.get_pressed() == (0, 1, 0): 
                    pass 
                    
if __name__ == '__main__':
    App()
