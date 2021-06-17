import pygame,sys
import time
import random
#part 1
pygame.init()

white=(255,255,255)
black=(10,0,0)
red=(255,0,0)
green=(0,100,0)
window_width=1350
window_height=700
w_s_h=200
w_s_w=20
w_w=window_width-220
w_h=window_height-40
screen=pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Snake Xangia")
font=pygame.font.SysFont(None,25,bold=True)

def myquit():
	pygame.quit()
	sys.exit(0)
#part 2
clock =pygame.time.Clock()#clock helps us to keep track of the events based on their timing
FPS=5#frames per second....screen gets refreshed 5 times per second
blockSize=20
noPixel=0
prev=5
#part 3
#drawing the snake
def snake(blockSize,snakelist):
	t=0
	for size in snakelist:
		pygame.draw.rect(screen,black,[size[0],size[1],blockSize,blockSize],2,border_radius=7)#[],border ki length, radius gol banane k liye
		if t==len(snakelist)-1:
			pygame.draw.circle(screen,(0,0,0),(size[0]+10,size[1]+5),2)
		t+=1;
	

def message_to_screen(msg,color,i):
	screen_text=font.render(msg,True,color)
	screen.blit(screen_text,[window_width/2,window_height/2+i])
#Blitting is one of the slowest operations in any game, so you need to be careful not to blit too much onto the screen in every frame.
def message_to_screen1(msg,color,i,h,w):
	screen_text=font.render(msg,True,color)
	screen.blit(screen_text,[h,w+i])

def gameLoop():
	pygame.display.update()
	gameExit=False
	gameOver=False
	
	lead_x=(w_w+w_s_h)/2
	lead_y=w_h/2

	change_pixels_x=0
	change_pixels_y=0

	snakelist=[]
	snakeLength=1

	randomAppleX=round(random.randrange(w_s_h+blockSize,w_w+w_s_h-blockSize*2))
	randomAppleY=round(random.randrange(w_s_w+blockSize,w_h+w_s_w-blockSize*2))
	x=1
	while not gameExit:
		global FPS
		if gameOver==True:
			
			message_to_screen("GAME OVER",red,0)
			pygame.display.update()
			pygame.time.delay(3001)
		while gameOver==True:
			screen.fill(white)
			message_to_screen("GAME OVER",black,-70)
			message_to_screen("**********************",green,-50)
			message_to_screen("YOUR SCORE",red,-40)
			message_to_screen(str(snakeLength),black,-20)
			message_to_screen("**********************",green,-5)
			message_to_screen("C->PLAY AGAIN",red,20)
			message_to_screen("X->EXIT",red,40)
			FPS=10
			x=1
			pygame.display.update()

			for event in pygame.event.get():

				if event.type==pygame.QUIT:
					gameOver=False
					gameExit=True
				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_x:
						gameExit=True
						gameOver=False
					if event.key==pygame.K_c:
						gameLoop()

		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				gameExit=True
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_ESCAPE:
					myquit()
				elif event.key==pygame.K_LEFT:
					change_pixels_x=-blockSize
					change_pixels_y=noPixel
				elif event.key==pygame.K_RIGHT:
					change_pixels_y=noPixel
					change_pixels_x=blockSize
				elif event.key==pygame.K_UP:
					change_pixels_x=noPixel
					change_pixels_y=-blockSize
				elif event.key==pygame.K_DOWN:
					change_pixels_y=blockSize
					change_pixels_x=noPixel
		
		lead_y+=change_pixels_y
		lead_x+=change_pixels_x
			#takraya ya nahi
		if lead_x>=w_w+w_s_h-20 or lead_x<w_s_h or lead_y>=w_h+w_s_w-20 or lead_y<w_s_w:
			gameOver=True
			continue
		screen.fill(white)
		AppleThickness=20
		print([(randomAppleX),(randomAppleY),AppleThickness,AppleThickness])

		pygame.draw.rect(screen,red,[randomAppleX,randomAppleY,AppleThickness,AppleThickness])
		pygame.draw.rect(screen,green,[200,20,window_width-220,window_height-40],20)
		allspriteslist=[]
		allspriteslist.append(lead_x)
		allspriteslist.append(lead_y)#current khopdi tupple
		snakelist.append(allspriteslist)
		if len(snakelist)>snakeLength:
   			del snakelist[0]
   		#crashing into himself
		for eachSegment in snakelist[:-1]:
			if eachSegment==allspriteslist:#crash 
				gameOver=True
		snake(blockSize,snakelist)
		pygame.display.update()

		if lead_x >= randomAppleX and lead_x <= randomAppleX + AppleThickness:
			if lead_y >= randomAppleY and lead_y <= randomAppleY + AppleThickness:
				randomAppleX=round(random.randrange(w_s_h+blockSize,w_w+w_s_h-blockSize*2)/10.0)*10.0
				randomAppleY = round(random.randrange(w_s_w+blockSize,w_h+w_s_w-blockSize*2)/10.0)*10.0
				snakeLength += 1
		global prev
		#global FPS
		if(snakeLength>=prev*2):
			prev=snakeLength
			FPS=1.5*FPS
			x+=1
		level="LEVEL "+str(x)
		score="SCORE::::"+str(snakeLength)
		speed="SPEED::::"+str(x)+"X"
		message_to_screen1(level,black,5,15,10)
		message_to_screen1(score,black,5,15,35)
		message_to_screen1(speed,red,5,15,55)
		pygame.display.update()
		clock.tick(FPS)
	pygame.quit()
	quit()
gameLoop()
