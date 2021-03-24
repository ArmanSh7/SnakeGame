from turtle import Turtle, Screen
COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    
    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]

    def snakeMove(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y =  self.segments[segment - 1].ycor()
            self.segments[segment].setposition(new_x, new_y)
        self.segments[0].forward(20)

    def createSnake(self):
        for i in range(0, 3):
            segment = Turtle()
            segment.shape("circle")
            segment.color("yellow")
            segment.penup()
            segment.goto(COORDINATES[i])
            self.segments.append(segment)

    def snakeGoUp(self):
        if (self.head.heading() != DOWN):
            self.head.setheading(UP)


    def snakeGoDown(self):
        if (self.head.heading() != UP):
            self.head.setheading(DOWN)

    def snakeGoRight(self):
        if (self.head.heading() != LEFT):
            self.head.setheading(RIGHT)

    def snakeGoLeft(self):
        if(self.head.heading()!=RIGHT):
            self.head.setheading(LEFT)

    def incrementSnakeSize(self):
        segment = Turtle()
        segment.penup()
        segment.hideturtle()
        segment.shape("circle")
        segment.color("yellow")
        segment.goto(self.segments[-1].position())
        self.segments.append(segment )
        segment.penup()
        segment.showturtle()
