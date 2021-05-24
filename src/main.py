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

    def check_mouse_collision(self, mouse_pos, start_or_end): 
        for row in self.grid.nodes:
            for node in row:
                if node.collide(*mouse_pos):
                    if start_or_end == "start":
                        node.is_start = True 
                        node.color = (0, 0, 255)
                    if start_or_end == "end":
                        node.is_end = True 
                        node.color = (255, 0, 0)
                    return True 
    
    def calculate_cells(self, const):
        for row in self.grid.nodes:
            for node in row:
                if node.is_start or node.is_end:
                    pass
                else:
                    if const == "g_cost":
                        node.calculate_g_cost(node)
                    if const == "h_cost":
                        node.calculate_h_cost(node)

    def event_handler(self):
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_x:
                    sys.exit()
                if e.key == pygame.K_s:
                    print("lol")
            if e.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0): 
                    if self.grid.already_has_start_node:
                        pass
                    else:
                        if self.check_mouse_collision(pygame.mouse.get_pos(), "start"): 
                            print("lololololollololololo")
                            self.grid.already_has_start_node = True 
                            self.calculate_cells("g_cost")
                if pygame.mouse.get_pressed() == (0, 1, 0): 
                    if self.grid.already_has_end_node:
                        pass
                    else:
                        if self.check_mouse_collision(pygame.mouse.get_pos(), "end"):
                            self.grid.already_has_end_node = True 
                            self.calculate_cells("h_cost")

if __name__ == '__main__':
    App()
