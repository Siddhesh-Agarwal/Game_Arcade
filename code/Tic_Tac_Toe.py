# Game_Arcade/Games/Tic_Tac_Toe.py
from tkinter import *
from tkinter import messagebox
from random import choice

def Play():
    # main window
    root = Tk()
    root.title("Tic Tac Toe")
    root.resizable(0, 0)
    root.config(bg='peachpuff2', border=10)

    # Variables
    global turn, moves, winner
    turn = choice(['O', 'X'])         # Used to assign first move
    moves = 0                         # Move count
    winner = None                     # Contains name of winner

    # Check if someone won
    def check_win():
        global winner
        if btn_11['text'] == 'X' and btn_12['text'] == 'X' and btn_13['text'] == 'X':
            btn_11.config(bg='red')
            btn_12.config(bg='red')
            btn_13.config(bg='red')
            winner = 'X'
            messagebox.showinfo("Game Over!", "Congrats!!! X has won the game.\nReset to continue.")

        elif btn_21['text'] == 'X' and btn_22['text'] == 'X' and btn_23['text'] == 'X':
            btn_21.config(bg='red')
            btn_22.config(bg='red')
            btn_23.config(bg='red')
            winner = 'X'
            messagebox.showinfo("Game Over!", "Congrats!!! X has won the game.\nReset to continue.")

        elif btn_31['text'] == 'X' and btn_32['text'] == 'X' and btn_33['text'] == 'X':
            btn_31.config(bg='red')
            btn_32.config(bg='red')
            btn_33.config(bg='red')
            winner = 'X'
            messagebox.showinfo("Game Over!", "Congrats!!! X has won the game.\nReset to continue.")

        elif btn_11['text'] == 'X' and btn_21['text'] == 'X' and btn_31['text'] == 'X':
            btn_11.config(bg='red')
            btn_21.config(bg='red')
            btn_31.config(bg='red')
            winner = 'X'
            messagebox.showinfo("Game Over!", "Congrats!!! X has won the game.\nReset to continue.")

        elif btn_12['text'] == 'X' and btn_22['text'] == 'X' and btn_32['text'] == 'X':
            btn_12.config(bg='red')
            btn_22.config(bg='red')
            btn_32.config(bg='red')
            winner = 'X'
            messagebox.showinfo("Game Over!", "Congrats!!! X has won the game.\nReset to continue.")

        elif btn_13['text'] == 'X' and btn_23['text'] == 'X' and btn_33['text'] == 'X':
            btn_13.config(bg='red')
            btn_23.config(bg='red')
            btn_33.config(bg='red')
            winner = 'X'
            messagebox.showinfo("Game Over!", "Congrats!!! X has won the game.\nReset to continue.")

        elif btn_11['text'] == 'X' and btn_22['text'] == 'X' and btn_33['text'] == 'X':
            btn_11.config(bg='red')
            btn_22.config(bg='red')
            btn_33.config(bg='red')
            winner = 'X'
            messagebox.showinfo("Game Over!", "Congrats!!! X has won the game.\nReset to continue.")

        elif btn_13['text'] == 'X' and btn_22['text'] == 'X' and btn_31['text'] == 'X':
            btn_13.config(bg='red')
            btn_22.config(bg='red')
            btn_31.config(bg='red')
            winner = 'X'
            messagebox.showinfo("Game Over!", "Congrats!!! X has won the game.\nReset to continue.") 


        if btn_11['text'] == 'O' and btn_12['text'] == 'O' and btn_13['text'] == 'O':
            btn_11.config(bg='red')
            btn_12.config(bg='red')
            btn_13.config(bg='red')
            winner = 'O'
            messagebox.showinfo("Game Over!", "Congrats!!! O has won the game.\nReset to continue.")

        elif btn_21['text'] == 'O' and btn_22['text'] == 'O' and btn_23['text'] == 'O':
            btn_21.config(bg='red')
            btn_22.config(bg='red')
            btn_23.config(bg='red')
            winner = 'O'
            messagebox.showinfo("Game Over!", "Congrats!!! O has won the game.\nReset to continue.")

        elif btn_31['text'] == 'O' and btn_32['text'] == 'O' and btn_33['text'] == 'O':
            btn_31.config(bg='red')
            btn_32.config(bg='red')
            btn_33.config(bg='red')
            winner = 'O'
            messagebox.showinfo("Game Over!", "Congrats!!! O has won the game.\nReset to continue.")

        elif btn_11['text'] == 'O' and btn_21['text'] == 'O' and btn_31['text'] == 'O':
            btn_11.config(bg='red')
            btn_21.config(bg='red')
            btn_31.config(bg='red')
            winner = 'O'
            messagebox.showinfo("Game Over!", "Congrats!!! O has won the game.\nReset to continue.")

        elif btn_12['text'] == 'O' and btn_22['text'] == 'O' and btn_32['text'] == 'O':
            btn_12.config(bg='red')
            btn_22.config(bg='red')
            btn_32.config(bg='red')
            winner = 'O'
            messagebox.showinfo("Game Over!", "Congrats!!! O has won the game.\nReset to continue.")

        elif btn_13['text'] == 'O' and btn_23['text'] == 'O' and btn_33['text'] == 'O':
            btn_13.config(bg='red')
            btn_23.config(bg='red')
            btn_33.config(bg='red')
            winner = 'O'
            messagebox.showinfo("Game Over!", "Congrats!!! O has won the game.\nReset to continue.")

        elif btn_11['text'] == 'O' and btn_22['text'] == 'O' and btn_33['text'] == 'O':
            btn_11.config(bg='red')
            btn_22.config(bg='red')
            btn_33.config(bg='red')
            winner = 'O'
            messagebox.showinfo("Game Over!", "Congrats!!! O has won the game.\nReset to continue.")

        elif btn_13['text'] == 'O' and btn_22['text'] == 'O' and btn_31['text'] == 'O':
            btn_13.config(bg='red')
            btn_22.config(bg='red')
            btn_31.config(bg='red')
            winner = 'O'
            messagebox.showinfo("Game Over!", "Congrats!!! O has won the game.\nReset to continue.")

    # Check draw
    def check_draw():
        if moves == 9:
            if winner == None:
                messagebox.showinfo("Game Over!", "Draw! The game has ended in a draw.\nReset to continue.")

    # Checking win/draw
    def check():
        check_win()
        check_draw()

    # Button clicked function
    def b_click(btn):
        global turn, moves
        if btn["text"] == " ":
            btn["text"] = turn

            moves += 1                       # Increment total moves
            if turn == 'X': turn = 'O'       # change turn to O
            else: turn = 'X'                 # change turn to X
            check()                          # Checking for win/draw
        else:
            messagebox.showerror("Invalid move!", "This box has already been selected.\nPick another box to continue.")

        # Reset button
    def reset():
        # reset btn text and color
        btn_11.config(text=' ', bg='lemon chiffon')
        btn_12.config(text=' ', bg='lemon chiffon')
        btn_13.config(text=' ', bg='lemon chiffon')

        btn_21.config(text=' ', bg='lemon chiffon')
        btn_22.config(text=' ', bg='lemon chiffon')
        btn_23.config(text=' ', bg='lemon chiffon')
            
        btn_31.config(text=' ', bg='lemon chiffon')
        btn_32.config(text=' ', bg='lemon chiffon')
        btn_33.config(text=' ', bg='lemon chiffon')

        # reset variables
        global turn, moves, winner
        turn = choice(['O', 'X'])
        moves = 0
        winner = None

    # Button Parameter
    btn_param = {
        'padx': 16,
        'pady': 1,
        'bd': 4,
        'fg': 'Black',
        'bg': 'lemon chiffon',
        'font': ('arial', 20),
        'width': 3,
        'height': 2
    }

    # Buttons
    btn_11 = Button(root, btn_param, text=' ', command=lambda: b_click(btn_11))
    btn_12 = Button(root, btn_param, text=' ', command=lambda: b_click(btn_12))
    btn_13 = Button(root, btn_param, text=' ', command=lambda: b_click(btn_13))
    btn_21 = Button(root, btn_param, text=' ', command=lambda: b_click(btn_21))
    btn_22 = Button(root, btn_param, text=' ', command=lambda: b_click(btn_22))
    btn_23 = Button(root, btn_param, text=' ', command=lambda: b_click(btn_23))
    btn_31 = Button(root, btn_param, text=' ', command=lambda: b_click(btn_31))
    btn_32 = Button(root, btn_param, text=' ', command=lambda: b_click(btn_32))
    btn_33 = Button(root, btn_param, text=' ', command=lambda: b_click(btn_33))

    btn_11.grid(row=1, column=1)
    btn_12.grid(row=1, column=2)
    btn_13.grid(row=1, column=3)
    btn_21.grid(row=2, column=1)
    btn_22.grid(row=2, column=2)
    btn_23.grid(row=2, column=3)
    btn_31.grid(row=3, column=1)
    btn_32.grid(row=3, column=2)
    btn_33.grid(row=3, column=3)

    # Reset button
    reset_btn = Button(root, text='RESET', fg='black', bg='blanched almond', height=2, width=16, font=('arial', 20, 'bold'), command=reset)
    reset_btn.grid(row=4, column=1, columnspan=3)

    # Keeping window open
    root.mainloop()

def About():
    return '''
    AIM:
    The goal of the game is for players to position their marks so that they make a continuous line of three cells vertically, horizontally, or diagonally.

    WIN:
    If one player makes a line of 3 cells vertically, horizontally or diagonally, then that player wins the game.

    DRAW:
    If none of the players are successful in makingt a line of 3 cells vertically, horizontally or diagonally even after all the 9 cells have been used up, The game ends in a draw (neither players win/lose).

    HOW TO PLAY:
    Players are required to alternate turns and click on the box they would like to fill.
    Once the game is over, the board should be reset to play again.

    Developed by     : Siddhesh Agarwal'''