import random
import turtle
import math
import pygame
import time
import os

#properties of the head of the snake
snake = turtle.Turtle()
snake.screen.bgcolor("lime")
snake.shape("square")
snake.color("green") 
snake.screen.listen()
snake.penup()
tycord=0
txcord=0 

if os.path.exists("high_score.txt"):
   file_object = open("high_score.txt" , "r")
   file_content = file_object.read()
   file_object.close()
else:
   file_object_write = open("high_score.txt" , "w")
   file_object_write.write("0")
   file_content = 0
   file_object_write.close()
#tail lists
tail=[]
beforetail=[]
xcor_tail = []
ycor_tail = []

#This is where the tails are stored
for i in range(1,100):
   beforetail.append(turtle.Turtle())
for bt in beforetail:
   bt.hideturtle()

#Movement Functions
def up():
   if snake.heading() == 270:
      heading = 270
      return heading
   snake.setheading(90)


def down():
   if snake.heading() == 90:
      heading = 90
      return heading
   snake.setheading(270)


def left():
   if snake.heading() == 0:
      heading = 0
      return heading
   snake.setheading(180)


def right():
   if snake.heading() == 180:
      heading = 180
      return heading
   snake.setheading(0)

#Food Properties
food = turtle.Turtle()
food.shape('circle')
food.penup()
food.color('red')
food.shapesize(1,1)
def make_food():

   food.hideturtle()
   food.goto(random.randint(-460,460),random.randint(-380,390))
   food.showturtle()

make_food()

#Score Properties
score= turtle.Turtle()
score.hideturtle()
score_cntr = 0
score.speed(0)
score.color("blue")
score.penup()
score.goto(-250,350)

fontsize = 18
Font = ('Arial', fontsize, 'normal')

score.write("score:" + str(score_cntr) , font=Font)

high_score_writer = turtle.Turtle()
high_score_writer.hideturtle()
high_score_writer.speed(0)
high_score_writer.color("blue")
high_score_writer.penup()

high_score_writer.goto(250,350)
high_score_writer.write("high score:" + str(file_content) , font=Font)


#Determines if the snake is near the food
def is_Snake_close_to_food():
   distance = math.sqrt(((food.ycor() - snake.ycor())**2 + (food.xcor() - snake.xcor())**2))
   if distance < 20:
      pygame.mixer.init()
      pygame.mixer.music.load("apple_bite.wav")
      pygame.mixer.music.play()
      return True
   elif distance > 20:
      return False

#Increases score by 10
def increment_score(score_cntr):
   score.clear()
   score.goto(-250,350)
   score.write("score:" + str(score_cntr) , font=Font)
   return ""

def high_score(score_cntr):
    file_content = score_cntr
    file_content_write = open("high_score.txt" , "w")
    file_content_write.write(str(file_content))
    file_object.close()
    file_content_write.close()
    high_score_writer.clear()
    high_score_writer.goto(250,350)
    high_score_writer.write("high score:" + str(file_content) , font=Font)


#Displays sound and "GAME OVER"
def game_over():
   pygame.mixer.init()
   pygame.mixer.music.load("Explosion+1.wav")
   pygame.mixer.music.play()
   g = turtle.Turtle()
   g.hideturtle()
   z = 0
   while z == 0:
      for game_over_size in range(10, 101, 10):
         g.write("GAME OVER", align = "center" , font = ("Arial"  , game_over_size, "normal"))
         time.sleep(0.05)
         if game_over_size == 100:
            while z == 0:
               snake.forward(0)
         else:
            g.clear()
         

tail.append(snake)


snake.screen.onkey(up, "Up")
snake.screen.onkey(down, "Down")
snake.screen.onkey(left, "Left")
snake.screen.onkey(right, "Right")

#Displays sound and checks if the snake head collides into itself
def collision():
   length_tail = len(tail)
   if length_tail == 0:
      return ""
   if length_tail == 1:
      return ""
   for x_and_y_coordinate in range(1, length_tail - 1):
        snake_pos1 = snake.xcor()
        snake_pos2 = snake.ycor()
       
        xcoordinate1 = int(tail[x_and_y_coordinate].xcor())
        ycoordinate2 = int(tail[x_and_y_coordinate].ycor())
        distance = math.sqrt(((ycoordinate2 - snake_pos2)**2 + (xcoordinate1 - snake_pos1)**2))
        if distance <= 10:
           game_over()
     
#Main "while loop" where all of the functions come into play
while snake.ycor()<=390 and snake.ycor()>=-380 and snake.xcor()<=460 and snake.xcor()>=-460:
   color_list = ["green" , "blue" , "red" , "yellow" , "gold" , "orange" , "red" , "maroon" , "violet" , "magenta" , "purple" , "navy" , "skyblue" , "cyan" , "turquoise" , "chocolate"]
   
   snakeycord=snake.ycor()
   snakexcord=snake.xcor()
   snake.forward(10)
   snake.speed(0)
   collision()
   counter = 0
   for index in range(1,len(tail)-1):
      tailxcor = tail[index].xcor()
      tailycor = tail[index].ycor()
      xcor_tail.append(tailxcor)
      ycor_tail.append(tailycor)
      newsnakexcord=tail[index].xcor()
      newsnakeycord=tail[index].ycor()
      tail[index].goto(snakexcord,snakeycord)
      snakexcord=newsnakexcord
      snakeycord=newsnakeycord
   

   if is_Snake_close_to_food() is True:
      make_food()
      score_cntr = score_cntr + 10
      increment_score(score_cntr)
         
      if int(score_cntr) > int(file_content):
         high_score(score_cntr)
         
      snakeycord=snake.ycor()
      snakexcord=snake.xcor()
      snake.forward(10)
      
      realscore=int((score_cntr/10)-1)
     
      tail.append(beforetail[realscore])
      
      tail[realscore].speed(0)
      tail[realscore].hideturtle()
      tail[realscore].shape('square')
      tailc_name = color_list[random.randrange(0, len(color_list) - 1)]
      if realscore == 0:
         tail[realscore].color("green")
         tail[realscore].penup()
         tail[realscore].showturtle()
      else:
         tail[realscore].color(tailc_name)
         tail[realscore].penup()
         tail[realscore].showturtle()
     
      for index in range(1,len(tail)-1):
     
         newsnakexcord=tail[index].xcor()
         newsnakeycord=tail[index].ycor()
         tail[index].goto(snakexcord,snakeycord)
         snakexcord=newsnakexcord
         snakeycord=newsnakeycord

     
     
   else:
         continue

game_over()
