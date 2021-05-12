import pygame 
import cell 

class Field: 

    def __init__(self): 
        self.cells = []  
        for x in range(0, 601, 30):
            temp_list = []
            for y in range(0, 601, 30):
                temp_list.append(cell.Cell(x, y))
            self.cells.append(temp_list) 
        print(self.cells)

    def draw(self, screen):
        for row in self.cells:
            for cl in row:
                cl.draw(screen) 
        for i in range(0, 601, 30):
            pygame.draw.line(screen, (0, 0, 0), (0, i), (600, i)) 
            pygame.draw.line(screen, (0, 0, 0), (i, 600), (i, 0)) 


