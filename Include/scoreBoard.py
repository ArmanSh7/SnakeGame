# turn magic values to constants
from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        # self.shape("")
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.highScore =0
        self.write(f"Score: {self.score}", move=True, align="right", font=("Arial",20, "normal"))


    def gameOver(self):
        self.goto(0, 0)
        self.write(f"Game Over!", move=False, align="center", font=("Arial", 40, "normal"))

    def increaseScore(self):
        self.clear()
        self.score = self.score + 1
        self.write(f"Score: {self.score}", move=True, align="right", font=("Arial", 20, "normal"))

        