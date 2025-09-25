from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

snake = Snake()


screen.update()

gameIsOn = True
while gameIsOn:
    screen.update()
    time.sleep(0.1)

    snake.move()






screen.exitonclick()

