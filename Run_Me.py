# Game_Arcade/Run_Me.py
import tkinter as tk
from Games.Snake_Game import Play_Snake_Game
from Games.Ping_Pong import Play_Ping_Pong
from Games.Tic_Tac_Toe import Play_TicTacToe
from Games.Space_Battle import Play_Space_Battle

def helper(function):
    root.destroy()
    function()
    
btn_params = {
    'padx': 16,
    'pady': 1,
    'bd': 4,
    'bg': 'gainsboro',
    'fg': 'black',
    'font': ('arial', 22),
    'width': 20,
    'height': 2,
    'activebackground': 'yellow'
}

# Main Screen
root = tk.Tk()
root.title('GAME ARCADE')
root.resizable(0, 0)

# Button for Snake Game
game_btn_1 = tk.Button(root, btn_params, text='Snake Game', command=lambda: helper(Play_Snake_Game)).grid(row=0)

# Button for Ping Pong
game_btn_2 = tk.Button(root, btn_params, text='Ping Pong', command=lambda: helper(Play_Ping_Pong)).grid(row=1)

# Button for Tic Tac Toe
game_btn_3 = tk.Button(root, btn_params, text='Tic-Tac-Toe', command=lambda: helper(Play_TicTacToe)).grid(row=2)

# Button for Space Battle
game_btn_4 = tk.Button(root, btn_params, text='Space Battle', command=lambda: helper(Play_Space_Battle)).grid(row=3)

# keeping screen open
root.mainloop()