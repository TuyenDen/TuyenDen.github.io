import pygame
import time 
import math

pygame.init()

screen = pygame.display.set_mode((500,600))

GREY = (150,150,150)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
font = pygame.font.SysFont('sans',50)
font1 = pygame.font.SysFont('sans',100)
b1 = font.render('+',True,BLACK)
b2 = font.render('-',True,BLACK)
b3 = font.render('Min',True,BLACK)
b4 = font.render('Sec',True,BLACK)
b5 = font.render('Start',True,BLACK)
b6 = font.render('Reset',True,BLACK)
clock = pygame.time.Clock()
mins = 0
secs = 0
total = 0
total_secs = 0
start = False
sound1 = pygame.mixer.Sound('tick.wav')
sound2 = pygame.mixer.Sound('timeout.wav')
running = True

while running:
	screen.fill(GREY)

	mouse_x, mouse_y = pygame.mouse.get_pos()

	pygame.draw.rect(screen,WHITE, (100,50,50,50))
	pygame.draw.rect(screen,WHITE, (100,130,50,50))
	pygame.draw.rect(screen,WHITE, (350,50,50,50))
	pygame.draw.rect(screen,WHITE, (350,130,50,50))
	pygame.draw.rect(screen,WHITE, (50,200,170,50)) 
	pygame.draw.rect(screen,WHITE, (280,200,170,50))
	pygame.draw.rect(screen,WHITE, (45,495,410,60))
	pygame.draw.rect(screen,WHITE, (50,500,400,50))


	screen.blit(b3,(10,45))
	screen.blit(b3,(420,45))
	screen.blit(b4,(10,125))
	screen.blit(b4,(420,125))
	screen.blit(b1,(110,45))
	screen.blit(b1,(110,125))
	screen.blit(b2,(365,45)) 
	screen.blit(b2,(365,125))
	screen.blit(b5,(90,200))
	screen.blit(b6,(320,200))

	pygame.draw.circle(screen,BLACK,(250,380),100)
	pygame.draw.circle(screen,WHITE,(250,380),98)
	pygame.draw.circle(screen,BLACK,(250,380),5)



	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if (100<mouse_x<150) and (50<mouse_y<100):
					total_secs+=60
					total = total_secs
				if (100<mouse_x<150) and (130<mouse_y<180):
					total_secs+=1
					total = total_secs
				if (350<mouse_x<400) and (50<mouse_y<100):
					total_secs-=60
					total = total_secs
				if (350<mouse_x<450) and (130<mouse_y<180):
					total_secs-=1
					total = total_secs
				if (280<mouse_x<450) and (200<mouse_y<250):
					total = total_secs
					start+=True
				if (50<mouse_x<220) and (200<mouse_y<250):
					total_secs+=0

	if start:
		if total_secs>0:
			pygame.mixer.Sound.play(sound1)
			total_secs-=1
			time.sleep(1)	
		else:
			pygame.mixer.Sound.play(sound2)
			start = False
	mins = total_secs//60
	secs = total_secs - (mins*60)			
	text_time = font1.render(str(mins)+':'+str(secs),True,RED)	
	screen.blit(text_time,(180,50))	
	x_sec = 250+90*math.sin(6*secs*math.pi/180)
	y_sec = 380-90*math.cos(6*secs*math.pi/180)
	pygame.draw.line(screen,RED,(250,380),(int(x_sec),int(y_sec)))
	x_min = 250+50*math.sin(6*mins*math.pi/180)
	y_min = 380-50*math.cos(6*mins*math.pi/180)
	pygame.draw.line(screen,BLACK,(250,380),(int(x_min),int(y_min)))
	if 	total!=0:

		pygame.draw.rect(screen,RED,(50,500,int(400*(total_secs/total)),50))
	pygame.display.flip()

pygame.quit()	