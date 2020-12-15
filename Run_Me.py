# Game_Arcade/Run_Me.py
from tkinter import *
from Games.Snake_Game import Play_Snake_Game
from Games.Ping_Pong import Play_Ping_Pong
from Games.Tic_Tac_Toe import Play_TicTacToe
from Games.Space_Battle import Play_Space_Battle

def helper(function):
    root.destroy()
    function()
    
def info():
    def local_helper():
        about.destroy()
        menu()
        
    text = '''
    GAME ARCADE
    
    This Project contains 4 games:
    1) Ping Pong (2 player)
    2) Snake game (single player)
    3) Space battle (single player)
    4) Tic Tac Toe (2 player)

    Further details can be found by choosing a game and clicking on "about"
    Button

    Developed by     : Siddhesh Agarwal
    '''

    root.destroy()

    about = Tk()
    about.title("About")
    about.resizable(0, 0)
    
    screen = Text(about, height=22, width=80)
    screen.pack()
    screen.config(borderwidth=20)
    screen.insert(END, text)

    BackButton = Button(about, btn_params, text="← Back", command=local_helper)
    BackButton.place(x=165, y=245)
        
    about.mainloop()

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

def menu():
    # Main Screen
    global root
    root = Tk()
    root.title('GAME ARCADE')
    root.config(borderwidth=5)
    root.geometry('350x480+100+100')
    root.resizable(0, 0)

    # Buttons
    game_btn_1 = Button(root, btn_params, text='Snake Game', command=lambda: helper(Play_Snake_Game)).pack()
    game_btn_2 = Button(root, btn_params, text='Ping Pong', command=lambda: helper(Play_Ping_Pong)).pack()
    game_btn_3 = Button(root, btn_params, text='Tic-Tac-Toe', command=lambda: helper(Play_TicTacToe)).pack()
    game_btn_4 = Button(root, btn_params, text='Space Battle', command=lambda: helper(Play_Space_Battle)).pack()
    info_btn = Button(root, btn_params, text='Information', command=info).pack()

    root.mainloop()

if __name__ == '__main__':
    menu()
