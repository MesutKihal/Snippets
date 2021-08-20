import pygame
import sys
import random
import concurrent.futures

class Snake:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 30
        self.h = 30
        self.color = (255,255,0)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))

class Bate:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 10
        self.h = 10
        self.color = (255,0,0)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h))


def Play():
    white = (255,255,255)
    black = (0,0,0)
    
    pygame.init()
    window_width = 768
    window_height = 512
    fps = 20

    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('snake')
    clock = pygame.time.Clock()
    score_font = pygame.font.SysFont('rod', 24, bold=True)

    left = False
    right = True
    up = False
    down = False
    score = 1
    size = 1
    
    head = Snake(250, 100)
    b = Bate(random.randint(1, 700), random.randint(1, 506))

    snake_parts = [head]

    coor_x = [head.x]
    coor_y = [head.y]

    def drawScreen():
        i = 0
        window.fill(black)
        for part in snake_parts:
            if part is not snake_parts[0]:
                part.x = coor_x[-i]
                part.y = coor_y[-i]
                part.draw(window)
            else:
                part.draw(window)
            i += 1
            
        b.draw(window)
        window.blit(score_txt, (700, 20))
        pygame.display.update()

    while True:
        clock.tick(fps)
        score_txt = score_font.render(f'{score}', True, (255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if not right:
                left = True
                right = False
                up = False
                down = False
        if keys[pygame.K_RIGHT]:
            if not left:
                left = False
                right = True
                up = False
                down = False
        if keys[pygame.K_UP]:
            if not down:
                up = True
                down = False
                left = False
                right = False
        if keys[pygame.K_DOWN]:
            if not up:
                up = False
                down = True
                left = False
                right = False

        #Snake motion 
        if left:
            head.x -= 15
        if right:
            head.x += 15
        if up:
            head.y -= 15
        if down:
            head.y += 15
            
        if (head.x <= b.x <= head.x + head.w and head.y <= b.y <= head.y + head.h) or (head.x <= b.x + b.w <= head.x + head.w and head.y <= b.y + b.h <= head.y + head.h):
            b.x = random.randint(1, 700)
            b.y = random.randint(1, 506)
            snake_parts.append(Snake(coor_x[len(coor_x)-1], coor_y[len(coor_y)-1]))
            score += 1
            size += 1
      
        #Borders
        if head.x + head.w < 0:
            head.x = window_width - head.w
        if head.x + head.w > window_width:
            head.x = 0
        if head.y + head.h < 0:
            head.y = window_height - head.h
        if head.y + head.h > window_height:
            head.y = 0
            
        if len(coor_x) < size:
            coor_x.append(head.x)
        else:
            coor_x = coor_x[1:]
        if len(coor_y) < size:
            coor_y.append(head.y)
        else:
            coor_y = coor_y[1:]
            
        drawScreen()
Play()
