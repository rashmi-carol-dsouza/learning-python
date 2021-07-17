from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-260, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Level = {self.level}', align="left", font=("Courier", 22, "bold"))

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align="center", font=("Courier", 28, "bold"))

