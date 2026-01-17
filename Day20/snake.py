import turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.game_turtles = []
        self.create()
        self.head = self.game_turtles[0]
    
    def create(self):
        for x in STARTING_POSITIONS:
            self.add(x)
                
    def add(self, position):
        t = turtle.Turtle("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.game_turtles.append(t)
    
    def extend(self):
        self.add(self.game_turtles[-1].position())

    def move(self):
        for t_num in range(len(self.game_turtles) - 1 , 0 , -1 ):
            new_x = self.game_turtles[t_num-1].xcor()
            new_y = self.game_turtles[t_num-1].ycor()
            self.game_turtles[t_num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
          
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            