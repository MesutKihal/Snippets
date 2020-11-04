import pygame
import sys
import random


pygame.init()
window_width = 1024
window_height = 512
fps = 20

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('snake')
clock = pygame.time.Clock()
size_font = pygame.font.SysFont('rod', 24, bold=True)

x = 250
y = 100
w = 30
h = 30

left = False
right = True
up = False
down = False
size = 1
coor_x = [0 for _ in range(1, 20)]
coor_y = [0 for _ in range(1, 20)]
bate_x = random.randint(1, 1018)
bate_y = random.randint(1, 506)

def drawScreen():
    global coor_x,coor_y,size
    window.fill((255,255,255))
    
    coor_x.append(x)
    coor_x.pop(0)
    coor_y.append(y)
    coor_y.pop(0)
    if size >= 20:
        size = 20
    #else:
    #    mid = len(coor_x) // 2
    #    coor_x = coor_x[mid:]
    #    coor_y = coor_y[mid:]
    #    coor_x.append(x)
    #    coor_y.append(y)
    pygame.draw.rect(window, (255,0,0), (x,y,w,h))
    for i in range(1, size):
        pygame.draw.rect(window, (255,0,0), (coor_x[-i],coor_y[-i],w,h))
        if coor_x[-i] <= x <= coor_x[-i] + w and coor_y[-i] <= y + w <= coor_y[-i] + w:
            print('dead')
    pygame.draw.rect(window, (0,255,0), (bate_x,bate_y,10,10))
    window.blit(size_txt, (900, 20))
    pygame.display.update()

while True:
    clock.tick(fps)
    size_txt = size_font.render(f'{size}', True, (0,0,0))
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
        
    if left:
        x -= 30
    if right:
        x += 30
    if up:
        y -= 30
    if down:
        y += 30
    if (x <= bate_x <= x + w and y <= bate_y <= y + h) or (x <= bate_x + 10 <= x + w and y <= bate_y <= y + h):
        bate_x = random.randint(1, 1018)
        bate_y = random.randint(1, 506)
        size += 1
    
    #Borders
    if x + 30 < 0:
        x = 994
    if x + 30 > 1024:
        x = 0
    if y + 30 < 0:
        y = 482
    if y + 30 > 512:
        y = 0
    
    drawScreen()
