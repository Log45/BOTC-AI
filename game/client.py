from network import Network
import pygame

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

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)


def read_pos(str):
    print("Str: ", str)
    string = str.strip().split(",")
    print("String: ", string)
    print(string[0], string[1])
    return int(string[0]), int(string[1])


def make_pos(tup):
    print("Tup: ", tup)
    print(str(tup[0]) + "," + str(tup[1]))
    return str(tup[0]) + "," + str(tup[1])


def redraw_window(window, player1, player2):
    window.fill((255, 255, 255))
    player1.draw(window)
    player2.draw(window)
    pygame.display.update()


def main():
    run = True
    n = Network()
    start_pos = read_pos(n.get_pos())
    print("Start_pos: ", start_pos)
    p1 = Character(start_pos[0], start_pos[1], 100, 100, "green")
    p2 = Character(0, 0, 100, 100, "red")
    clock = pygame.time.Clock()
    while run:

        clock.tick(60)
        print("Make pos: ", make_pos((p1.x, p1.y)))
        print("n.send: ", n.send(make_pos((p1.x, p1.y))))
        p2_pos = read_pos(n.send(make_pos((p1.x, p1.y))))
        p2.x = p2_pos[0]
        p2.x = p2_pos[1]
        print("P2_pos: " + p2_pos)
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p1.move()
        redraw_window(win, p1, p2)


if __name__ == "__main__":
    main()
