import turtle
import random

FONT = ("Arial", 8, "normal")
ALIGN = "center"
class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write(f"Scoreboard: {self.score} ", align = ALIGN, font =FONT)
      
    def update_scoreboard(self):
        self.write(f"Scoreboard: {self.score} ", align = ALIGN, font =FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align = ALIGN, font =FONT)
        
    def increase_score(self):
        self.score += 1
        self.clear()