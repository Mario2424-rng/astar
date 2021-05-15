#!/usr/local/bin/python3.9

import sys 
import pygame 
import grid
import display 

class App:

    def __init__(self):
        self.disp = display.Display(600, 600, 60)
        self.grid = grid.Grid()
        self.main()
        
    def main(self):
        while True: 
            self.disp.clear() 
            self.event_handler() 
            self.grid.draw(self.disp.get_screen())
            self.disp.update()

    def event_handler(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_x:
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0): 
                    if self.grid.already_has_start_node:
                        pass
                    else:
                        mouse_pos = pygame.mouse.get_pos()
                        self.grid.already_has_start_node = True 
                        for row in self.grid.nodes:
                            for node in row:
                                if node.collide(*mouse_pos): 
                                    node.is_start_node = True 
                                    node.color = (0, 0, 255)
                                    for row in self.grid.nodes:
                                        for node in row:
                                            if node.is_start_node or node.is_end_node:
                                                pass
                                            else:
                                                node.calculate_g_cost(node)
                if pygame.mouse.get_pressed() == (0, 1, 0): 
                    pass 
                    
if __name__ == '__main__':
    App()
