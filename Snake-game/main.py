from turtle import Screen, Turtle
import time
from snake import Snake


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)

# # Step 1 . Creating a snake body

snake = Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
snake.reset()



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

    
# Step 3 . Control the snake
    


# Step 4 . Detect collision with food


# Step 5 . Create a scoreboard
    










screen.exitonclick()
