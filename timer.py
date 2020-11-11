import pygame
import time
import datetime
import sys


pygame.init()

screen = pygame.display.set_mode((450,300))
fps = 60
clock = pygame.time.Clock()
font = pygame.font.SysFont('tunga', 40, bold=True)

class Entry:
    def __init__(self, x, y, width,  height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont("couriernew", 32)
        self.solution = "0"
        self.txt = self.font.render(self.solution, True,(0,0,0))
        self.color = (200,200,200)
        self.On = False
        
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x,self.y,self.width,self.height))
        window.blit(self.txt,(self.x+10, self.y+5))
        
entry1 = Entry(50,70,50,50)
def Draw():
    screen.fill((255,255,255))
    screen.blit(text, (100, 100))
    entry1.draw(screen)
    pygame.display.update()

later = datetime.datetime.now() + datetime.timedelta(minutes=1)

def timer():
    seconds =  (later - datetime.datetime.now()).seconds
    minutes = seconds // 60
    seconds %= 60
    return "%02d:%02d" % (minutes, seconds)

def convert(seconds):
        seconds = seconds % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        return "%d:%02d:%02d" % (hour, minutes, seconds)

while True:
    text = font.render(timer(), True, (0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if entry1.x < mouse[0] < entry1.x + entry1.width and entry1.y < mouse[1] < entry1.y + entry1.height:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_KP0]: entry1.solution += "0"
        if keys[pygame.K_KP1]: entry1.solution += "1"
        if keys[pygame.K_KP2]: entry1.solution += "2"
        if keys[pygame.K_KP3]: entry1.solution += "3"
        if keys[pygame.K_KP4]: entry1.solution += "4"
        if keys[pygame.K_KP5]: entry1.solution += "5"
        if keys[pygame.K_KP6]: entry1.solution += "6"
        if keys[pygame.K_KP7]: entry1.solution += "7"
        if keys[pygame.K_KP8]: entry1.solution += "8"
        if keys[pygame.K_KP9]: entry1.solution += "9"

    Draw()
