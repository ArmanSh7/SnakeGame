from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard

coordinates = [(0,0), (-20,0), (-40,0)]
junk = Food()
screen = Screen()
screen.setup(600,600)
screen.bgcolor("green")
screen.title("Snake game")
screen.tracer(0)
Snakes = Snake()
screen.listen()
SCORE = ScoreBoard()
screen.onkey(key="Up", fun=Snakes.snakeGoUp)
screen.onkey(key="Down", fun=Snakes.snakeGoDown)
screen.onkey(key="Left", fun=Snakes.snakeGoLeft)
screen.onkey(key="Right", fun=Snakes.snakeGoRight)
notstop = True
from scoreBoard import ScoreBoard

while (notstop):
    screen.update()
    time.sleep(0.1)
    Snakes.snakeMove()

    if Snakes.head.distance(junk)<15:
        Snakes.incrementSnakeSize()
        junk.refresh()
        SCORE.increaseScore()
    if Snakes.head.xcor() > 300 or  Snakes.head.xcor() < -300 or (Snakes.head.ycor() > 300) or  (Snakes.head.ycor() < -300):
        notstop = False
        SCORE.gameOver()

    for segment in Snakes.segments[1:]:
        if Snakes.segments[0].distance(segment) < 10:
            notstop = False
            SCORE.gameOver()






screen.exitonclick()
