import pygame,sys,random


#always initiate pygame
pygame.init()
clock = pygame.time.Clock() #using it to set the frame rate


width = 1280
height = 960
#creating base screen
window = pygame.display.set_mode((width,height))

#ball frame changing speed
ballx = 7
bally = 7

#colors
grey = pygame.Color('grey12')
red = (255,0,0)

#empty rectangles
#creating ball , 2 plate sizes
ball = pygame.Rect(width/2 - 15,height/2 - 10,40,40) #placing in the middle
plate1 = pygame.Rect(width-20,height/2 - 70 , 10 , 180)
plate2 = pygame.Rect(10,height/2 - 70 , 10 , 180)


# for plate movement border condition
def platemovement():
    if plate2.top <= 0:
        plate2.top = 0
    if plate2.bottom >= height:
        plate2.bottom = height

def opponentmovement():
    if plate1.top <= 0:
        plate1.top = 0
    if plate1.bottom >= height:
        plate1.bottom = height

def ballrestart():

    global ballx
    ball.x = width/2 - 15
    ballx *= random.choice((1,-1))

def ballmovement():
    global ballx,player
    global bally,opponent

    # moving the ball
    ball.x += ballx
    ball.y += bally

    # border bounce condition
    if ball.top <= 0 or ball.bottom >= height:
        bally *= -1  # reversing the above process to bounce back
    if ball.left <= 0:
       opponent += 1
       ballrestart()
    if ball.right >= width:
       player += 1
       ballrestart()


    # same bounce condition for plates
    if ball.colliderect(plate1) or ball.colliderect(plate2):
        ballx *= -1

#opponent plate 1
opponentspeed = 7

#variable for plate movement
platespeed = 0

#creating variables for fonts
player = 0
opponent = 0
font = pygame.font.Font("freesansbold.ttf",20)

#looping with true condition till event occur..
while True:
    for event in pygame.event.get(): #waiting for the events
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            #making plate to move up down
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_DOWN:
               platespeed += 7
           if event.key == pygame.K_UP:
               platespeed -= 7
        #it will stop the movement when key got released
        if event.type == pygame.KEYUP:
           if event.key == pygame.K_DOWN:
               platespeed -= 7
           if event.key == pygame.K_UP:
               platespeed += 7


    platemovement() #condition actually
    ballmovement()


    #opponent movement deciding

    if plate1.top < ball.y:
        plate1.top += opponentspeed
    if plate1.bottom > ball.y:
        plate1.bottom -= opponentspeed
    opponentmovement()


    #platemovement
    plate2.y += platespeed  #increment decrement will happen from the event loop :)

    #backgroung color for base window
    window.fill((255,255,255))

    #draw function should be happen inside the loop
    #draw ball and plates
    pygame.draw.ellipse(window, red, ball)
    pygame.draw.rect(window, grey, plate1)
    pygame.draw.rect(window, grey, plate2)

    #score text
    text = font.render(f"{player}", True , (255,0,0))
    window.blit(text,(600,470))

    text2 = font.render(f"{opponent}", True, (255, 0, 0))
    window.blit(text2, (670, 470))


    #draw a line seperating the window
    pygame.draw.aaline(window,grey,(width/2,0),(width/2,height))



    pygame.display.flip()
    clock.tick(60)