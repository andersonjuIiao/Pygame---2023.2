import pygame
pygame.init()


WIDTH, HEIGHT = 501, 392
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Insper Pong")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100

class Paddle:
    COLOR = WHITE
    VEL = 4

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

class Ball:
    MAX_VEL = 5
    COLOR = WHITE
    def __init__(self,x,y,radius):
        self.x = x
        self.y = y
        self.radius =radius
        self. x_vel = MAX_VEL
        self.y_vel = 0 
    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x , self.y), self.radius)






def draw(win, paddles):
    win.fill(BLACK)

    for paddle in paddles:
        paddle.draw(win)

    pygame.display.update()

def handle_paddle_movement(keys, Left_paddle, right_paddle):
    if keys[pygame.K_w] and Left_paddle.y - Left_paddle.VEL >= 0:
        Left_paddle.move(up=True)
    if keys[pygame.K_s] and Left_paddle.y + Left_paddle.VEL + Left_paddle.height <= HEIGHT:
        Left_paddle.move(up=False)

    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >= 0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height <= HEIGHT:
        right_paddle.move(up=False)


def main():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

    while run:
        clock.tick(FPS)
        draw(WIN, [left_paddle, right_paddle])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)
    
    pygame.quit

if __name__== '__main__':
    main()