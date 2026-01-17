import turtle
import random

colours = ["red", "green", "yellow", "blue", "purple", "orange"]

s = turtle.Screen()
s.setup(500, 400)

y_positions = [-110,-80, -50, -20, 10, 40]
turtles = []

for i in range(0, 6):
    t = turtle.Turtle("turtle")
    turtles.append(t)
    t.color(colours[i])
    t.penup()
    t.goto(-240, y_positions[i])
    
user_bet = s.textinput("Make your bet", "Which turtle will win the race? Enter your color:")

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for t in turtles:
        if t.xcor() > 230:
            is_race_on = False
            winning_color = t.pencolor()
            if winning_color == user_bet:
                print(f"Your {winning_color} turtle won the race")
            else:
                print(f"Your {user_bet} turtle lost the race, {winning_color} turtle is the winner")
        random_distance = random.randint(0, 10)
        t.forward(random_distance)
        
s.exitonclick()

