import turtle
import time
import snake
import food
import scoreboard

s = turtle.Screen()
s.setup(600, 600)
s.bgcolor("black")
s.title("Game")
s.tracer(0)

game_snake = snake.Snake()
game_food = food.Food()
game_scoreboard = scoreboard.Scoreboard()
is_game_on = True

      
s.listen()

s.onkey(game_snake.up, "Up")
s.onkey(game_snake.down, "Down")
s.onkey(game_snake.right, "Right")
s.onkey(game_snake.left, "Left")

while is_game_on:
    s.update()
    time.sleep(0.1)
    game_snake.move()

    # Detect collision with Food
    if game_snake.head.distance(game_food) < 15:
        game_food.refresh()
        game_snake.extend()
        game_scoreboard.increase_score()
        game_scoreboard.update_scoreboard()        
        
    # Detect collision with Wall
    if game_snake.head.xcor() > 280 or game_snake.head.xcor() < -280 or game_snake.head.ycor() > 280 or game_snake.head.ycor() < -280:
        is_game_on = False
        game_scoreboard.game_over()
        
    # Detect collision with tail
    for t in game_snake.game_turtles[1:]:
        if game_snake.head.distance(t) < 10:
            is_game_on = False
            game_scoreboard.game_over()
            
    
s.exitonclick()
