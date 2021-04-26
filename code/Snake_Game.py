# Game_Arcade/Games/Snake_Game.py
import tkinter as tk
import turtle
from random import randrange
from time import sleep

def Play():
    # Set Up Screen
    window = turtle.Screen()
    window.title("Snake Game")
    window.bgcolor('forest green')
    window.setup(width=600, height=700)
    window.tracer(0)

    # Snake Head
    head = turtle.Turtle()
    head.speed(0)
    head.shape('square')
    head.color('black')
    head.penup()
    head.goto(0, 0)
    head.direction = 'stop'

    # Snake Food
    food = turtle.Turtle()
    food.speed(0)
    food.shape('circle')
    food.color('red2')
    food.penup()
    food.goto(0, 100)

    # Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape('square')
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 320)
    pen.write('Score: 0   High Score: 0', align='center', font=('Courier', 24, 'normal'))

    # Boundary
    border_1 = turtle.Turtle()
    border_1.speed(0)
    border_1.shape('square')
    border_1.shapesize(stretch_wid=1, stretch_len=30)
    border_1.color('darkgreen')
    border_1.penup()
    border_1.goto(0, 300)
    border_1.clone().goto(0, -300)

    border_2 = turtle.Turtle()
    border_2.speed(0)
    border_2.shape('square')
    border_2.shapesize(stretch_wid=30, stretch_len=1)
    border_2.color('darkgreen')
    border_2.penup()
    border_2.goto(300, 0)
    border_2.clone().goto(-300, 0)

    # Snake Body, Delay , Score, Loop Counter
    segments = []
    delay1 = 0.1
    score = 0
    high_score = 0
    count = 0

    # Change In Coordinates
    def move():
        if head.direction == 'up':
            y = head.ycor()
            head.sety(y + 20)

        elif head.direction == 'down':
            y = head.ycor()
            head.sety(y - 20)

        if head.direction == 'right':
            x = head.xcor()
            head.setx(x + 20)

        elif head.direction == 'left':
            x = head.xcor()
            head.setx(x - 20)

    # Change In Direction
    def go_up():
        if head.direction != 'down':
            head.direction = 'up'

    def go_down():
        if head.direction != 'up':
            head.direction = 'down'

    def go_right():
        if head.direction != 'left':
            head.direction = 'right'

    def go_left():
        if head.direction != 'right':
            head.direction = 'left'

    # Keyboard Bindings
    window.listen()
    window.onkeypress(go_up, 'Up')
    window.onkeypress(go_down, 'Down')
    window.onkeypress(go_left, 'Left')
    window.onkeypress(go_right, 'Right')


    # Main Game Loop
    while True:
        window.update()

        # Check for collision with border
        if head.xcor() < -290 or head.xcor() > 290 or head.ycor() < -290 or head.ycor() > 290:
            sleep(1.0)
            head.goto(0, 0)
            head.direction = 'stop'

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            
            segments.clear()     # Clear segments list    
            score = 0            # Reset score
            delay1 = 0.1         # Reset delay
            count = 0            # Food count

            # Display score and high score
            pen.clear()
            pen.write(f'Score: {score}   High Score: {high_score}', align='center', font=('Courier', 24, 'normal'))

        # Check if there is a collision with food
        if head.distance(food) < 20:
            # Move food to a new random coordinate
            x = randrange(-280, 281, 20)
            y = randrange(-280, 281, 20)
            food.goto(x, y)

            # Add a segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape('square')
            new_segment.color('blue')
            new_segment.penup()
            segments.append(new_segment)
                
            score += 10          # Increment score
            count += 1           # Increment food counter

            # Increasing speed for every 3 food eaten
            if count % 3 == 0:
                delay1 -= 0.008

        # Change high score
        if score > high_score:
            high_score = score
            
        # Display score and high score
        pen.clear()
        pen.write(f'Score: {score}   High Score: {high_score}', align='center', font=('Courier', 24, 'normal'))

        # Move end segments first in reverse order
        for index in range(len(segments)-1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)
            
        # Move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

        move()                   # Moving the snake

        # Check for head collision with body segment
        for segment in segments:
            if segment.distance(head) < 20:
                sleep(1.0)
                head.goto(0, 0)
                head.direction == 'stop'

                # Hide the segments
                for segment in segments:
                    segment.goto(1000, 1000)

                    
                segments.clear() # Clear segments list
                score = 0        # Reset score
                delay1 = 0.1     # Reset delay
                count = 0        # Reset food count

                # Display score and high score
                pen.clear()
                pen.write(f'Score: {score}   High Score: {high_score}', align='center', font=('Courier', 24, 'normal'))

            sleep(delay1)        # Slowing down speed of while loop

def About():
    return '''
    AIM:
    The objective of the game is to collect as many apples as possible and create a maximum score.

    SCORING:
    The score is incremented by 10 for every apple eaten.
    The length of snake increases by 1 unit for every apple eaten.

    LOSING:
    The player can get out in the following ways:
    1) Head-on collision with bush.
    2) Head-on collision with own body.

    CONTROL:
    The snake can be controlled using the arrow keys(Up key, Right key, Down key and Left key)
            
    Developed by : Siddhesh Agarwal'''