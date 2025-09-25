from turtle import Screen, Turtle
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

starting_positions = [(0,0), (-20,0), (-40,0)]

segments = []

for positions in starting_positions:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(positions)
    segments.append(segment)


screen.update()

gameIsOn = True
while gameIsOn:
    screen.update()
    time.sleep(0.1)

    for segment_number in range( len(segments) -1, 0, -1):
        new_x = segments[segment_number - 1].xcor()
        new_y =  segments[segment_number -1].ycor()
        segments[segment_number].goto(new_x, new_y)

    segments[0].forward(20)







screen.exitonclick()

