import Games.Ping_Pong as PP
import Games.Snake_Game as SG
import Games.Space_Battle as SB
import Games.Tic_Tac_Toe as TTT
from tkinter import *

#Button Parameters
btn_params = {
    'padx': 16,
    'pady': 1,
    'bd': 4,
    'bg': '#fbfbfb',
    'fg': '#000000',
    'font': ('arial', 22),
    'width': 20,
    'height': 2,
    'activebackground': 'yellow'
}

def dark():
    global btn_params
    btn_params['relief'] = 'flat'
    btn_params['bg'] = "#121212"
    btn_params['fg'] = "#0000FF"

def light():
    global btn_params
    btn_params['relief'] = 'raised'
    btn_params['bg'] = "#fbfbfb"
    btn_params['fg'] = "#121212"

# takes Back to Main menu
def Back(window):
    window.destroy()
    MainMenu()

# Opens Submenu with further options
def Play(game):
    def helper():
        global about
        about.destroy()
        Play(game)

    def PlayGame(game):
        if game == 'Ping Pong': PP.Play()
        if game == 'Snake Game': SG.Play()
        if game == 'Space Battle': SB.Play()
        if game == 'Tic Tac Toe': TTT.Play()

    def GameInfo(game):
        subroot.destroy()

        if game == 'Ping Pong': text = PP.About()
        if game == 'Snake Game': text = SG.About()
        if game == 'Space Battle': text = SB.About()
        if game == 'Tic Tac Toe': text = TTT.About()

        global about
        about = Tk()
        about.resizable(0, 0)
        about.title("About")

        screen = Text(about, height=30, width=120, wrap=WORD)
        screen.pack()
        screen.insert(END, text)

        BackButton = Button(about, btn_params, text="← Back", command=helper)
        BackButton.pack(anchor=S)
            
        about.mainloop()
        
    global mainroot
    mainroot.destroy()

    subroot = Tk()
    subroot.title(game)
    subroot.resizable(0, 0)

    btn1 = Button(subroot, **btn_params, text='Play Game', command=lambda: PlayGame(game)).pack()              # Play Button
    btn2 = Button(subroot, **btn_params, text='Game Information', command=lambda: GameInfo(game)).pack()       # Info Button
    btn3 = Button(subroot, **btn_params, text='Back to Main Menu', command=lambda: Back(subroot)).pack()       # Back button

    subroot.mainloop()

# Information of main app
def Info(window: Tk): #! Doesn't contain the details of each game but only the list
    text = '''GAME ARCADE
    This Project contains 4 games:
    1) Ping Pong (2 player)
    2) Snake game (single player)
    3) Space battle (single player)
    4) Tic Tac Toe (2 player)

    Developed by     : Siddhesh Agarwal
    '''

    window.destroy()

    about = Tk()
    about.resizable(0, 0)
    about.title("About")

    screen = Text(about, height=10, width=50)
    screen.pack()
    screen.insert(END, text)

    BackButton = Button(about, btn_params, text="← Back", command=lambda: Back(about))
    BackButton.pack(anchor=S)
        
    about.mainloop()

# Main menu
def MainMenu():
    global mainroot
    mainroot = Tk()
    mainroot.title('Game Arcade')
    mainroot.resizable(0, 0)

    btn1 = Button(mainroot, **btn_params, text='Ping Pong', command=lambda: Play('Ping Pong')).pack()
    btn2 = Button(mainroot, **btn_params, text='Snake Game', command=lambda: Play('Snake Game')).pack()
    btn3 = Button(mainroot, **btn_params, text='Space Battle', command=lambda: Play('Space Battle')).pack()
    btn4 = Button(mainroot, **btn_params, text='Tic Tac Toe', command=lambda: Play('Tic Tac Toe')).pack()
    info = Button(mainroot, **btn_params, text='Information', command=lambda: Info(mainroot)).pack()

    mainroot.mainloop()

#############################
##     Driver  Program     ##
#############################
if __name__ == '__main__':
    MainMenu()
