import colorgram
import turtle
import random

# colours = colorgram.extract('Day17and18\image.jpg', 30)

# rgb = []
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.r
#     b = colour.rgb.r
#     rgb.append((r, g, b))
# print(rgb)

colour_list = [(228, 228, 228), (244, 244, 244), (2, 2, 5), (236, 236, 236), (33, 33, 32), (133, 133, 133), (46, 46, 46), (147, 147, 147), (9, 9, 9), (189, 189, 189), (225, 225, 225), (62, 62, 62), (68, 68, 68), (58, 58, 58), (185, 185, 185), (136, 136, 136), (136, 136, 136), (131, 131, 131), (14, 14, 14), (18, 18, 18), (121, 121, 121), (170, 170, 170), (92, 92, 92), (175, 175, 175), (86, 86, 86), (183, 183, 183), (22, 22, 22), (67, 67, 67), (210, 210, 210), (89, 89, 89)]

t = turtle.Turtle()
turtle.colormode(255)
t.speed("fastest")
t.penup()
t.hideturtle()

my_screen = turtle.Screen()

t.setheading(225)
t.forward(300)
t.setheading(0)

for i in range(1, 101):
    t.dot(20, random.choice(colour_list))
    t.forward(50)
    if i % 10 == 0 :
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


my_screen.exitonclick()