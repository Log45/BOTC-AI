import pygame
from BOTC import *

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

client_number = 0

class Character():
    def __init__(self, x, y, width, height, color) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 2
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.vel

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.vel

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.vel

        self.rect = (self.x, self.y, self.width, self.height)

def redraw_window(window, player):
    win.fill((255, 255, 255))
    player.draw(win)
    pygame.display.update()

def main():
    run = True

    p = Character(50, 50, 100, 100, "green")

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redraw_window(win, p)

if __name__ == "__main__":
    main()