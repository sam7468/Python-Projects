import pygame
from pygame.locals import *
import time
import random

size = 50

class Foodreddy:
    def __init__(self,newscreen):
        self.newscreen = newscreen
        self.reddy = pygame.image.load("files/food.png")
        self.x = 150
        self.y = 150

    #method for class Food

    def draw(self):
        self.newscreen.blit(self.reddy, (self.x, self.y))
        pygame.display.flip()

    def move(self):
       self.x = random.randint(1,19)*size
       self.y = random.randint(1,15)*size


class Anaconda:
    def __init__(self,newscreen,length):
        self.length = length
        self.newscreen = newscreen #creating a new argument for the below draw function to understand
        self.head = pygame.image.load("files/th.png") #load the head in py
        self.x = [size]*length #position x axis
        self.y = [size]*length #position y axis
        self.direction = "right"

    #methods

    def draw(self):  #called by screen
       # everytime creates a new screen
        for i in range(self.length):
            self.newscreen.blit(self.head, (self.x[i], self.y[i]))# importing the head (block) at the new position

        pygame.display.flip()  # display


    def moveup(self):
        self.direction = "up"
    def movedown(self):
        self.direction = "down"
    def moveright(self):
        self.direction = "right"
    def moveleft(self):
        self.direction = "left"

    def addlength(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)


    def move(self):

        for i in range(self.length -1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == "up":
            self.y[0] -= size
        if self.direction == "down":
            self.y[0] += size
        if self.direction == "right":
            self.x[0] += size
        if self.direction == "left":
            self.x[0] -= size

        self.draw()



class Game:

    # this part workss till the anaconda to show up in the screen with given position

    def __init__(self): #defining a class
        pygame.init()  # pygame gets life
        pygame.mixer.init()
        self.display = pygame.display.set_mode((1000, 800))  # display a base window
        self.display.fill((201, 0, 44))  # bg color
        self.head = Anaconda(self.display, 10) #   >>>>>>>>>>>>>>>>>>>>>>>   calling head()      ^^^^^^^^^^^^^^^^^^
        self.reddy = Foodreddy(self.display)
        self.head.draw()
        self.reddy.draw()


    def wheneats(self,x1,y1,x2,y2):
        if x1 >= x2 and x1 < x2 + size:
          if y1 >= y2 and y1 < y2 + size:
              return True

        return False

    def texture(self):
        bg = pygame.image.load("files/bg.jpg")
        self.display.blit(bg, (0,0))

    def play(self):
        self.texture()
        self.head.move()
        self.reddy.draw()
        self.score()
        pygame.display.flip()

        if self.wheneats(self.head.x[0],self.head.y[0],self.reddy.x,self.reddy.y):
          sound = pygame.mixer.Sound("files/eaten.wav")
          pygame.mixer.Sound.play(sound)
          self.head.addlength()
          self.reddy.move()



        for i in range(2,self.head.length):
            if self.wheneats(self.head.x[0],self.head.y[0],self.head.x[i],self.head.y[i]):
                sound = pygame.mixer.Sound("files/lost.wav")
                pygame.mixer.Sound.play(sound)
                raise "GAME OVER"

        if not (0 <= self.head.x[0] <= 1000 and 0 <= self.head.y[0] <= 800):
            sound = pygame.mixer.Sound("files/lost.wav")
            pygame.mixer.Sound.play(sound)
            raise "GAME OVER"


    def gameover(self):

        self.texture()
        bg = pygame.image.load("files/gover.jpg")
        self.display.blit(bg, (0, 0))
        font = pygame.font.SysFont('arial', 27)
        disp = font.render(f"score : {self.head.length}", True, (150,153,151))
        self.display.blit(disp, (870, 10))
        pygame.display.update()


    def score(self):
            font = pygame.font.SysFont('arial', 24)
            score = font.render(f"score : {self.head.length}", True, (28,28,28))
            self.display.blit(score, (860, 5))

    def reset(self):
      self.head = Anaconda(self.display,1)
      self.reddy =  Foodreddy(self.display)


    #this part responsible for the user input and movement of the snake (EVENT)

    def run(self): #method of class

        cond = True  # global condition
        pause = False


        while cond:  # using while to make the window stay still

            for event in pygame.event.get():  # event to happen (input from the user)
                if event.type == KEYDOWN:  # starts looking for an event to happen.

                    if event.key == K_RETURN:
                        pause = False
                    if event.key == K_ESCAPE:  # if escape key pressed
                        cond = False
                    if event.key == K_UP:
                        self.head.moveup()
                    if event.key == K_DOWN:
                        self.head.movedown()
                    if event.key == K_RIGHT:
                        self.head.moveright()
                    if event.key == K_LEFT:
                        self.head.moveleft()
                elif event.type == QUIT:  # if x button clicked quit the game.
                    cond = False


            try:
             if not pause:
              game.play()
            except Exception as e:
                self.gameover()
                pause = True
                self.reset()
            time.sleep(0.2)

if __name__ == "__main__":
    #running the class in main function
    game = Game()  # here geme = Screen() > one object of the class
    game.run()




