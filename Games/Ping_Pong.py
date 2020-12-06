# Game_Arcade/Games/Ping_Pong.py
import turtle
from time import sleep
import tkinter as tk

def Play_Ping_Pong():

    # Button Parameters
    btn_params = {
    'padx': 16,
    'pady': 1,
    'bd': 4,
    'fg': 'black',
    'bg': 'gainsboro',
    'font': ('arial', 20),
    'width': 20,
    'height': 2,
    'activebackground': 'yellow'
    }
    
    # Play
    def play():
        # Window
        window = turtle.Screen()
        window.title("Ping Pong")
        window.bgcolor('green')
        window.setup(800, 600)
        window.tracer(0)

        # Paddle A
        paddle_a = turtle.Turtle()
        paddle_a.speed(0)
        paddle_a.color("black")
        paddle_a.shape("square")
        paddle_a.shapesize(stretch_wid=5, stretch_len=1)
        paddle_a.penup()
        paddle_a.goto(-340, 0)
        paddle_a.direction = 'stop'

        # Paddle B
        paddle_b = turtle.Turtle()
        paddle_b.speed(0)
        paddle_b.color("black")
        paddle_b.shape("square")
        paddle_b.shapesize(stretch_wid=5, stretch_len=1)
        paddle_b.penup()
        paddle_b.goto(340, 0)
        paddle_b.direction = 'stop'

        # Ball
        ball = turtle.Turtle()
        ball.speed(0)
        ball.color("red")
        ball.shape("circle")
        ball.penup()
        ball.goto(0, 0)
        ball.dx = 10
        ball.dy = 10

        # Killing window before starting new one
        window1.destroy()

        # Pen
        pen = turtle.Turtle()
        pen.speed(0)
        pen.color('black')
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 260)
        pen.write("Player 1: 0  Player 2: 0", align='center', font=('Courier', 20, 'bold'))

        # Score
        score_a = 0
        score_b = 0

        # delay
        delay = 0.1

        # Functions
        def paddle_a_up():
            paddle_a.direction = 'up'

        def paddle_a_down():
            paddle_a.direction = 'down'

        def paddle_b_up():
            paddle_b.direction = 'up'

        def paddle_b_down():
            paddle_b.direction = 'down'

        def move():
            if paddle_a.direction == 'up':
                y = paddle_a.ycor()
                paddle_a.sety(y + 20)

            if paddle_a.direction == 'down':
                y = paddle_a.ycor()
                paddle_a.sety(y - 20)

            if paddle_b.direction == 'up':
                y = paddle_b.ycor()
                paddle_b.sety(y + 20)

            if paddle_b.direction == 'down':
                y = paddle_b.ycor()
                paddle_b.sety(y - 20)

        # Quit game
        def finish():
            window.bye()

        # Keyboard Binding
        window.listen()
        window.onkeypress(paddle_a_up, 'w')
        window.onkeypress(paddle_a_down, 's')
        window.onkeypress(paddle_b_up, 'Up')
        window.onkeypress(paddle_b_down, 'Down')
        window.onkeypress(finish, 'q')

        # Mainloop
        while True:
            window.update()

            # Move the ball
            ball.setx(ball.xcor() + ball.dx)
            ball.sety(ball.ycor() + ball.dy)

            # Move the paddle
            move()

            # Border check for ball
            if ball.ycor() > 290:
                ball.dy *= -1

            elif ball.ycor() < -290:
                ball.dy *= -1

            if ball.xcor() > 390:
                ball.goto(0, 0)
                ball.dx *= -1
                score_a += 10
                pen.clear()
                pen.write("Player 1: {}  Player 2: {}".format(score_a, score_b), align='center', font=('Courier', 20, 'bold'))

            elif ball.xcor() < -390:
                ball.goto(0, 0)
                ball.dx *= -1
                score_b += 10
                pen.clear()
                pen.write("Player 1: {}  Player 2: {}".format(score_a, score_b), align='center', font=('Courier', 20, 'bold'))

            # Paddle and ball collision
            if ball.xcor() == 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
                ball.dx *= -1
            if ball.xcor() == -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
                ball.dx *= -1

            # Border check for paddle
            if paddle_a.ycor() > 250:
                paddle_a.direction = 'down'

            elif paddle_a.ycor() < -250:
                paddle_a.direction = 'up'

            if paddle_b.ycor() > 250:
                paddle_b.direction = 'down'

            elif paddle_b.ycor() < -250:
                paddle_b.direction = 'up'

            # Slowing down while loop
            sleep(delay)

            # checking if player 1 won
            if score_a == 110:
                # Displaying winner
                pen.clear()
                pen.write('Player 1 Wins', align='center', font=('Courier', 20, 'bold'))
                sleep(2)

                # Reseting
                pen.clear()
                pen.write("Player 1: 0  Player 2: 0", align='center', font=('Courier', 20, 'bold'))
                ball.goto(0, 0)
                paddle_a.goto(-350, 0)
                paddle_b.goto(350, 0)
                score_a = 0
                score_b = 0

                # Starting again
                move()

            # checking if player 1 won
            if score_b == 110:
                # Displaying winner
                pen.clear()
                pen.write('Player 2 Wins', align='center', font=('Courier', 20, 'bold'))
                sleep(2)

                # Reseting
                pen.clear()
                pen.write("Player 1: 0  Player 2: 0", align='center', font=('Courier', 20, 'bold'))
                ball.goto(0, 0)
                paddle_a.goto(-350, 0)
                paddle_b.goto(350, 0)
                score_a = 0
                score_b = 0

                # Starting again
                move()

        # Keeps Screen Open
        window.mainloop()

    # About
    def about():
        def helper():
            about.destroy()
            Play_Ping_Pong()

        # Text
        text = '''
        AIM:
        The objective of the game is to score 110 points before the other player.

        SCORING:
        The score is incremented by 10 for every miss by the opponent.

        LOSING:
        A player can lose if the opponent player scores 110 points before one does.

        CONTROL:
        The player A paddle can be controlled using the "w" and "s" keys for up and down respectively.
        The player B paddle can be controlled using the up arrow and down arrow for up and down respectively.
        
        Developed by     : Siddhesh Agarwal
        Contact (e-mail) : siddhesh.agarwal@gmail.com
        Repository link  : https://github.com/Siddhesh-Agarwal/Ping_pong
        '''
        
        window1.destroy()

        about = tk.Tk()
        about.title("About")
        about.resizable(0, 0)

        screen = tk.Text(about, height=30, width=120)
        screen.pack()
        screen.insert(tk.END, text)
        
        BackButton = tk.Button(about, btn_params, text="← Back", command=helper)
        BackButton.place(x=300, y=350)

        about.mainloop()

    # Setting up window
    window1 = tk.Tk()
    window1.title("PING PONG")

    # Play Button
    PlayButton = tk.Button(window1, btn_params, text="Play",  command=play)
    PlayButton.grid(row=0, column=0)

    # About Button
    AboutButton = tk.Button(window1, btn_params, text="About", command=about)
    AboutButton.grid(row=1, column=0)

    # Keeps Window Open
    window1.mainloop()
