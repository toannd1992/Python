from turtle import Turtle, Screen
import time
from random import randint,choice

COLORS = ["white", "green", "yellow", "cyan", "magenta", "blue", "orange"]
class Snake():
    def __init__(self):
        self.nodes = []
        self.init_snake()
        self.update_heading = 0

    def init_snake(self):
        for i in [0,-20,-40]:
            self.init_append(i,0)

    def init_append(self, x, y):
        snake = Turtle()
        snake.color(choice(COLORS))
        snake.shape("square")
        snake.penup()
        snake.goto(x,y)
        self.nodes.append(snake)

    def Eat(self):
        node = self.nodes[-1]
        self.init_append(node.xcor(), node.ycor())

    def move(self):
        for i in range(len(self.nodes)-1, 0,-1):
            x_new = self.nodes[i-1].xcor()
            y_new = self.nodes[i-1].ycor()
            self.nodes[i].goto(x_new, y_new)
        self.nodes[0].forward(20)
        self.update_heading = self.nodes[0].heading()

        head = self.nodes[0]
        x,y = head.xcor(), head.ycor()
        if x > 280:
            head.setx(-280)
        elif x < -280:
            head.setx(280)

        if y > 280:
            head.sety(-280)
        elif y < -280:
            head.sety(280)
    
    def up(self):
        if self.update_heading != 270:
            self.nodes[0].setheading(90)
    def down(self):
        if self.update_heading != 90:
            self.nodes[0].setheading(270)
    def left(self):
        if self.update_heading != 0:
            self.nodes[0].setheading(180)
    def right(self):
        if self.update_heading != 180:
            self.nodes[0].setheading(0)
    
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.6)
        self.penup()
        self.color("red")
    def init_food(self, nodes):
        while True:
            x = randint(-280,280)
            y = randint(-280,280)
            z = False
            for node in nodes:
                if node.distance(x,y) < 10:
                    z = True
                    break
            if not z:
                self.goto(x,y)
                break

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.update_score()
    def up_score(self):
        self.score += 1
        self.update_score()
    def update_score(self):
        self.clear()
        self.write(f"SCORE: {self.score}", align="center", font=("Courier", 18, "bold"))
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=("Courier", 30, "bold"))
        self.goto(0,-30)
        self.write(f"Press Space To Continue", align="center", font=("Courier", 20, "bold"))


display = Screen()
display.setup(600, 600)
display.bgcolor("black")
display.title("Snake Game - by Toàn")
display.tracer(0)

def main():
    snake = Snake()
    food = Food()
    food.init_food(snake.nodes)
    score = Score()

    display.listen()
    display.onkey(snake.up,"Up")
    display.onkey(snake.down,"Down")
    display.onkey(snake.left,"Left")
    display.onkey(snake.right,"Right")

    Start_game = True
    speed = 0.15
    while Start_game:
        time.sleep(speed)
        display.update()
        snake.move()
        if snake.nodes[0].distance(food) < 15:
            food.init_food(snake.nodes)
            snake.Eat()
            score.up_score()
            speed *= 0.998
        for i in range(1,len(snake.nodes)):
            if snake.nodes[0].distance(snake.nodes[i]) < 10:
                Start_game = False
                score.game_over()

def game_continue():
    display.reset()
    main()

main()
display.onkey(game_continue, "space")
display.exitonclick()