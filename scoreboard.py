FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.goto(-280, 300)
        self.write(f'Level :{self.l_score}', align="center", font=("Arial", 24, "normal"))
        #self.goto(250, 250)

    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 300)
        self.write(f'Level :{self.l_score}', align="center", font=("Arial", 24, "normal"))


    def increase_score(self):
        self.l_score += 1
        self.clear()

    def game_over(self):
        self.goto(0, 0)
        self.color('red')
        self.write(f'Game over!!!. Your final score was {self.l_score}', align="center", font=FONT)
        self.goto(200, 250)


