import pygame 
import math

class Node:

    color = (255, 255, 255)

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 30, 30)
        self.is_start = False 
        self.is_end = False 
        self.g_cost = 0
        self.h_cost = 0 
        self.f_cost = self.g_cost + self.h_cost 

    def calculate_g_cost(self, start_node):
        self.g_cost = math.sqrt((self.rect.x - start_node.rect.x)**2 + (self.rect.y - start_node.rect.y)**2)

    def calculate_h_cost(self, end_node):
        pass 

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def collide(self, x, y):
        if self.rect.collidepoint(x, y):
            return True 
        else: 
            return False 

