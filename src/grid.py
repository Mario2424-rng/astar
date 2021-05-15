import pygame 
import node

class Grid: 

    def __init__(self): 
        self.nodes = []  
        self.already_has_start_node = False 
        self.already_has_end_node = False 
        for x in range(0, 601, 30):
            temp_list = []
            for y in range(0, 601, 30):
                temp_list.append(node.Node(x, y))
            self.nodes.append(temp_list) 

    def draw(self, screen):
        for row in self.nodes:
            for nd in row:
                nd.draw(screen) 
        for i in range(0, 601, 30):
            pygame.draw.line(screen, (0, 0, 0), (0, i), (600, i)) 
            pygame.draw.line(screen, (0, 0, 0), (i, 600), (i, 0)) 


