from turtle import Turtle, Screen
import time
from random import randint, choice



class Thanhtruot(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(5,1)
        self.penup()
        self.goto(pos)
    def up(self):
        y_new = self.ycor() + 30
        if y_new >= 300:
            y_new = 270
        self.goto(self.xcor(), y_new)
    def down(self):
        y_new = self.ycor() - 30
        if y_new <= -300:
            y_new = -270
        self.goto(self.xcor(), y_new)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()
    def move(self,x,y):
        x_new = self.xcor() + x
        y_new = self.ycor() + y
        self.goto(x_new, y_new)
    
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.Score_player_1 = 0
        self.Score_player_2 = 0
        self.update_Score()
        
    def update_Score(self):
        self.clear()
        self.goto(-140, 270)
        self.write(self.Score_player_1, align="center", font=("Arial", 18, "normal"))
        self.goto(140, 270)
        self.write(self.Score_player_2, align="center", font=("Arial", 18, "normal"))
        self.goto(0, 270)
        self.write("SCORE", align="center", font=("Arial", 18, "normal"))

    def win_player_1(self):
        self.Score_player_1 += 1
        self.update_Score()     
    def win_player_2(self):
        self.Score_player_2 += 1
        self.update_Score()

display = Screen()
display.setup(800, 600)
display.bgcolor("black")
display.title("Pong Game")
display.tracer(0)

right = Thanhtruot((350, 0))
light = Thanhtruot((-350,0))
ball = Ball()
player = Player()



display.listen()
display.onkey(key="Up", fun = right.up)
display.onkey(key="Down", fun = right.down)
display.onkey(key="w", fun = light.up)
display.onkey(key="s", fun = light.down)
list_xy = [5, -5, 10, -10, 15, -15]
x_ran = choice(list_xy)
y_ran = choice(list_xy)
time_play = 0.2
Start_game = True

while Start_game:
    time.sleep(time_play)
    display.update()
    ball.move(x_ran,y_ran)
    
    if ball.ycor() > 290 or ball.ycor() < -290:
        y_ran *= -1
    if ball.xcor() > 398 or ball.xcor() < -398:
        if ball.xcor() > 398:
            player.win_player_1()
        elif ball.xcor() < -390:
            player.win_player_2()
        time_play = 0.2
        ball.goto(0,0)
        time.sleep(3)
        x_ran = choice(list_xy)
        y_ran = choice(list_xy)
    elif (ball.distance(right) < 70 and ball.xcor() > 320) or (ball.distance(light) < 70 and ball.xcor() < -320):
        x_ran *= -1
        time_play *= 0.85
    

display.exitonclick()