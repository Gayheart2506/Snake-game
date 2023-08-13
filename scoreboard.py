from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scores = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 268)
        self.hideturtle()
        self.new_update()

    def new_update(self):
        self.write(f"SCORE: {self.scores}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER !!!", align=ALIGN, font=FONT)

    def update_score(self):
        self.scores += 1
        self.clear()
        self.new_update()
