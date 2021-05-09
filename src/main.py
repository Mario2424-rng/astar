#!/usr/local/bin/python3.9

import sys 
import pygame 
import display 

class App:

    def __init__(self):
        self.disp = display.Display(600, 600, 60)
        self.main()

    def main(self):
        while True: 
            self.disp.clear() 
            self.event_handler() 
            self.disp.update()

    def event_handler(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_x:
                sys.exit()
            
if __name__ == '__main__':
    App()
