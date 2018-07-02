#*****************************************************GRAPHICS INTERFACE FOR SUDOKU GAME**********************************************
import sudoku
import pygame,sys
from pygame.locals import*
import time

#*********************************************************INITIALIZE ALL THE REQUIRED VARIABLES***************************************

FPS = 30
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
L_BLUE = (135,206,250)
YELLOW = (255,255,0)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SUDOKU = [[0 for i in range(9)] for j in range (9)]
MATRIX = [[0 for i in range(9)] for j in range (9)]

#********************************************************GAME STARTS HERE ************************************************

pygame.init()
fpsClock = pygame.time.Clock()
DISPLAY = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Sudoku')
bg = pygame.image.load("bg.jpg")

#def main_menu () :

class Button :
	def __init__(self,x,y,h,w,c,target):
		self.button = pygame.Rect(x,y,w,h)
		self.c = c
		self.x = x
		self.y = y
		self.level = target
	def display_button(self,mouse) :
		pygame.draw.rect(DISPLAY,self.c,self.button)
		message_display(self.level,30,self.x+75,self.y+30)
		if self.button.collidepoint(mouse) :
			pygame.draw.rect(DISPLAY,(0,255,0),self.button)
			message_display(self.level,30,self.x+75,self.y+30)
			return True
		return False
	def on_click(self) :
		global SUDOKU,filled
		SUDOKU,filled = sudoku.generate_sudoku_problem(self.level)
		#game_loop()



def text_objects(text, font , color) :
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_display(text,font_size,x,y,color = BLACK) :
    largeText = pygame.font.Font('freesansbold.ttf',font_size)
    TextSurf, TextRect = text_objects(text, largeText,color)
    TextRect.center = (x,y)                              #200 307
    DISPLAY.blit(TextSurf, TextRect)

#*********************IN Construction************************
def main_menu () :
	DISPLAY.blit(bg,(0,0))
	message_display('SUDOKU',90,300,150)
	message_display('GUI By Bhavya Saraf',15,300,580)
	button_easy = Button(230,200,60,150,RED,'Easy')
	button_medium = Button(230,280,60,150,RED,'Medium')
	button_hard = Button(230,360,60,150,RED,'Hard')
	while True :
		mouse = pygame.mouse.get_pos()
		
		x = button_easy.display_button(mouse)
		y = button_medium.display_button(mouse)
		z = button_hard.display_button(mouse)

		for event in pygame.event.get() :
			if event.type == pygame.QUIT :
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN :
				if event.button == 1 : 
					if x :
						button_easy.on_click()
						return 0
					if y :
						button_medium.on_click()
						return 1
					if z :
						button_hard.on_click()
						return 2

		pygame.display.update()
		fpsClock.tick(20)

#********************************************************DISPLAY SUDOKU GRID AND BOXES****************************************
def display_grid () :
	global SUDOKU,MATRIX
	for i in range (10,495,60):
		for j in range (10,495,60):																	#10,70,130,190 
			a = (i-10)//60
			b = (j-10)//60
			
			MATRIX[a][b] = pygame.Rect(i,j,50,50)
			if (a,b) not in filled:
				pygame.draw.rect(DISPLAY,YELLOW,MATRIX[a][b])
				message_display(str(SUDOKU[a][b]),15,i+25,j+25)
			else :
				pygame.draw.rect(DISPLAY,L_BLUE,MATRIX[a][b])
			#if SUDOKU[a][b] != 0 :
				#message_display(str(SUDOKU[a][b]),15,i+25,j+25)
				
	pygame.draw.line(DISPLAY,BLACK,(185,10),(185,540),4)
	pygame.draw.line(DISPLAY,BLACK,(365,10),(365,540),4)
	pygame.draw.line(DISPLAY,BLACK,(10,185),(540,185),4)
	pygame.draw.line(DISPLAY,BLACK,(10,365),(540,365),4)

#********************************************************DISPLAY SUDOKU NUMBERS************************************************
def display_number (SUDOKU) :
	count = 0
	for i in filled :
			if SUDOKU[i[0]][i[1]] != 0 :
				message_display(str(SUDOKU[i[0]][i[1]]),15,i[0]*60+35,i[1]*60+35)
				count = count + 1

	if count == 81 :
		return True
	return False		


def change_color_on_hover (mouse,arr) :
	count = 0
	for i in arr :
		if MATRIX[i[0]][i[1]].collidepoint(mouse) :
			pygame.draw.rect(DISPLAY,WHITE,MATRIX[i[0]][i[1]])
			if SUDOKU[i[0]][i[1]] != 0 :
				message_display(str(SUDOKU[i[0]][i[1]]),15,i[0]*60+35,i[1]*60+35)
				count = count + 1
			return i[0],i[1],count
		else :
			pygame.draw.rect(DISPLAY,L_BLUE,MATRIX[i[0]][i[1]])

		if SUDOKU[i[0]][i[1]] != 0 :
				message_display(str(SUDOKU[i[0]][i[1]]),15,i[0]*60+35,i[1]*60+35)
				count = count + 1
	return -1,-1,count

def high_score():
	f = open('time_best.txt','r')
	time = f.read().split('\n')
	return time

def update_high_score(s):
	a = open('time_best.txt','w')
	a.write(s[0]+'\n'+s[1]+'\n'+s[2])
	a.close()

def game_loop () :
	global u
	DISPLAY.blit(bg,(0,0))
	display_grid()
	message_display(' Press Enter to submit | Press Escape to go back',15,280,560)
	message_display('GUI By Bhavya Saraf',15,300,580)
	start_ticks=pygame.time.get_ticks()
	condition = True
	status = 'npressed'
	a = -1
	b = -1
	rem_a = 0
	rem_b = 0
	pygame.display.update()
	while True :

		if a != -1 and b!=-1:
			rem_a =a
			rem_b =b

		timex = (pygame.time.get_ticks() - start_ticks)//1000
		mouse = pygame.mouse.get_pos()
		a,b,completion=change_color_on_hover(mouse,filled)
		if a != -1 and b!=-1:
			p_a = a
			p_b = b

		#completion = display_number(SUDOKU)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT or condition == False:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN :
				if event.button == 1 :
					#a,b = find_mouse_on_cell(mouse,filled)
					if a==-1 and b==-1:
						continue
					else :
						status = 'pressed'
			if event.type == pygame.KEYDOWN and status == 'pressed':
				if event.key == pygame.K_1 or event.key == pygame.K_KP1 :
					SUDOKU[a][b] = 1
				if event.key == pygame.K_2 or event.key == pygame.K_KP2 :
					SUDOKU[a][b] = 2
				if event.key == pygame.K_3 or event.key == pygame.K_KP3 :
					SUDOKU[a][b] = 3
				if event.key == pygame.K_4 or event.key == pygame.K_KP4 :
					SUDOKU[a][b] = 4
				if event.key == pygame.K_5 or event.key == pygame.K_KP5 :
					SUDOKU[a][b] = 5
				if event.key == pygame.K_6 or event.key == pygame.K_KP6 :
					SUDOKU[a][b] = 6
				if event.key == pygame.K_7 or event.key == pygame.K_KP7 :
					SUDOKU[a][b] = 7
				if event.key == pygame.K_8 or event.key == pygame.K_KP8 :
					SUDOKU[a][b] = 8
				if event.key == pygame.K_9 or event.key == pygame.K_KP9 :
					SUDOKU[a][b] = 9
				if event.key == pygame.K_BACKSPACE :
					SUDOKU[a][b] = 0
				if event.key == pygame.K_RETURN :	 
					if sudoku.sudo_chk(SUDOKU) == 1 and completion == 81 :
						DISPLAY.blit(bg,(0,0))
						message_display('CORRECT :)',90,290,150,GREEN)
						message_display('Time Taken : '+str(timex)+' seconds',50,290,300)
						scores = high_score()
						if (int(scores[u])>timex):
							scores[u] = str(timex)
							update_high_score(scores)
						message_display('Best time : '+scores[u],50,290,350)
						pygame.display.update()
						time.sleep(2)
						return 0
					else :
						DISPLAY.blit(bg,(0,0))
						message_display('INCORRECT :(',85,290,250,RED)
						pygame.display.update()
						time.sleep(1)
						DISPLAY.blit(bg,(0,0))
						display_grid()
						message_display(' Press Enter to submit | Press Escape to go back',15,280,560)
						message_display('GUI By Bhavya Saraf',15,300,580)
						pygame.display.update()
				if event.key == pygame.K_ESCAPE :
					return 1
		pygame.display.update((MATRIX[rem_a][rem_b],MATRIX[p_a][p_b]))
		fpsClock.tick(15)
		
u = main_menu()
game_loop()




