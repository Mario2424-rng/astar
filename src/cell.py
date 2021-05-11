import pygame 

class Cell:

    color = (255, 255, 255)

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 30, 30)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def __str__(self):
        return f"{self.x} {self.y}"

    def __repr__(self):
        return f"{self.rect.x} {self.rect.y}"
