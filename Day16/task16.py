import random
import turtle
from prettytable import PrettyTable

t = turtle.Turtle()
turtle.colormode(255)

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)



my_screen = turtle.Screen()
print(my_screen.canvheight)
t.shape("turtle")
t.color(random_colour())
t.forward(10)
t.penup()
t.forward(10)
t.pendown()
t.speed("fastest")

colours = ["red", "green", "yellow", "blue"]

directions = [0, 90, 180, 270]

#t.pensize(15)

# for i in range(200):
#     t.color(random_colour())
#     t.forward(30)
#     t.setheading(random.choice(directions))
        

# for i in range(3,11):
#     t.color(random_colour())
#     for j in range(i):
#         t.forward(100)
#         t.right(360/i)

for i in range(0,360, 5):
    t.color(random_colour())
    t.circle(100)
    t.setheading(i)

my_screen.exitonclick()


table = PrettyTable()

table.add_column("A",[1, 2 , 3, 4])
table.add_column("B",[1, 2 , 3, 4])

table.align = "l"

print(table)
