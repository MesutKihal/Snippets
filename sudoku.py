import pygame
import sys
import random
from variables import *

pygame.init()
white = (255,255,255)
black = (0,0,0)
table = [
		[var1,var2,var3], [var10,var11,var12], [var19,var20,var21],
	    [var4,var5,var6], [var13,var14,var15], [var22,var23,var24],
	    [var7,var8,var9], [var16,var17,var18], [var25,var26,var27],
	  
	    [var28,var29,var30], [var37,var38,var39], [var46,var47,var48],
	    [var31,var32,var33], [var40,var41,var42], [var49,var50,var51],
	    [var34,var35,var36], [var43,var44,var45], [var52,var53,var54],
	
	    [var55,var56,var57], [var64,var65,var66], [var73,var74,var75],
	    [var58,var59,var60], [var67,var68,var69], [var76,var77,var78],
	    [var61,var62,var63], [var70,var71,var72], [var79,var80,var81],]

font = pygame.font.SysFont('verdana', 20)
screen_width = 600
screen_height = 370
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Sudoku")
clock = pygame.time.Clock()

while True:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	screen.fill(white)
	x = 1
	y = 1
	for sub in table:
		for var in sub:
			temp = font.render(str(var), True, black)
			if x*55 < 500:
				screen.blit(temp, (x*55,y*30))
				if x % 3 == 0 and not x == 9:
					pygame.draw.rect(screen,black,((x+1)*55-20,25,5,290))
			else:
				if y % 3 == 0:
					pygame.draw.rect(screen,black,(45,(y+1)*30-5,500,5))
				y += 1
				x = 1
				screen.blit(temp, (x*55,y*30))
			x += 1
	pygame.display.update()


#Check horizontally
'''
x = 2
i = 12
j = 0
while 12 <= i <= 12+2:
	while j < 3:
		if i != 14 and j != 2:
			if arr[i][j] == x:
				print((i, j))
		j += 1
	j = 0
	i += 1
'''
'''Check vertically'''
#i = 0
#while i <= 24:
#	print(arr[i][1])
#	i += 3
