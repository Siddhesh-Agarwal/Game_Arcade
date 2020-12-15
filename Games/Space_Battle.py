# Game_Arcade/Games/Space_Battle.py
from tkinter import *
import turtle
import random
import math

def Play_Space_Battle():
    # play
    def play():
        # setting up main Screen
        wn = turtle.Screen()
        wn.setup(1200, 800)
        wn.bgcolor("black")
        wn.title("Space Battle")
        wn.tracer(0)

        # Testing / Start of game values
        global spare_defenders
        num_of_defenders = 30
        spare_defenders = 100
        num_of_attackers = 250
        num_of_defender_weapons = 30
        num_of_attacker_weapons = 20

        # Sprite class
        class Sprite():
            pen = turtle.Turtle()
            pen.hideturtle()
            pen.speed(0)
            pen.penup()
            
            def draw_text(x, y, text):
                Sprite.pen.goto(x, y)
                Sprite.pen.color("white")
                Sprite.pen.write(text, font=("Courier New", 24, "normal"))
            
            def __init__(self, x, y, shape, color):
                self.x = x
                self.y = y
                self.shape = shape
                self.color = color
                self.dx = 0
                self.dy = 0
                self.speed = 0
                self.active = True
                self.heading = 0
                self.health = 10
                
            def render(self):
                Sprite.pen.shapesize(1, 1, 0)
                Sprite.pen.goto(self.x, self.y)
                Sprite.pen.shape(self.shape)
                Sprite.pen.color(self.color)
                Sprite.pen.stamp()
                
            def move(self):
                self.dx = math.cos(self.heading * 3.14159 / 180) * self.speed
                self.dy = math.sin(self.heading * 3.14159 / 180) * self.speed
                
                self.x += self.dx
                self.y += self.dy
                
            def is_collision(self, other, tolerance):
                d = ((self.x-other.x)**2 + (self.y-other.y)**2)**0.5
                if d < tolerance: return True
                else: return False

        class Defender(Sprite):
            def __init__(self, x, y, shape, color):
                Sprite.__init__(self, x, y, shape, color)
                self.health = 100
                
            def render(self):
                Sprite.pen.shapesize(2, 2, 0)
                    
                Sprite.pen.goto(self.x, self.y)
                Sprite.pen.shape(self.shape)
                Sprite.pen.color(self.color)
                Sprite.pen.stamp()
                
                # Draw shields
                color = "green"
                if self.health > 35: color = "green"
                elif self.health > 15: color = "yellow"
                else: color = "red"
                
                Sprite.pen.goto(self.x + 20, self.y)
                Sprite.pen.setheading(90)
                Sprite.pen.pendown()
                Sprite.pen.width(3)
                Sprite.pen.color(color)
                Sprite.pen.circle(20)
                Sprite.pen.penup()
            
        class DefenderWeapon(Sprite):
            def __init__(self, x, y, shape, color):
                Sprite.__init__(self, x, y, shape, color)
                self.speed = 10
                
            def render(self):
                Sprite.pen.shapesize(0.2, 0.2, 0)
                Sprite.pen.goto(self.x, self.y)
                Sprite.pen.shape(self.shape)
                Sprite.pen.color(self.color)
                Sprite.pen.stamp()
                
            def move(self):
                self.dx = math.cos(self.heading * 3.14159 / 180) * self.speed
                self.dy = math.sin(self.heading * 3.14159 / 180) * self.speed
                
                self.x += self.dx
                self.y += self.dy
                
                # Border checks
                if self.x > 600 or self.x < -600 or self.y > 400 or self.y < -400:
                    self.x = -1000
                    self.active = False

        class Attacker(Sprite):
            def __init__(self, x, y, shape, color):
                Sprite.__init__(self, x, y, shape, color)
                self.health = 50
                
            def render(self):
                Sprite.pen.shapesize(1, 1, 0)
                Sprite.pen.goto(self.x, self.y)
                Sprite.pen.shape(self.shape)
                Sprite.pen.color(self.color)
                Sprite.pen.stamp()
                
            def move(self):
                
                self.dx = math.cos(self.heading * 3.14159 / 180) * self.speed
                self.dy = math.sin(self.heading * 3.14159 / 180) * self.speed
                
                self.x += self.dx
                self.y += self.dy
            
                if self.y > 390 :
                    self.heading = random.randint(190, 210)
                elif self.y < -390:
                    self.heading = random.randint(140, 170)
                    
                # Moves off screen
                if self.x < -600:
                    self.x += random.randint(1200, 1500)
                    self.speed *= 1.1

        class Particle(Sprite):
            def __init__(self, x, y, shape, color):
                Sprite.__init__(self, x, y, shape, color)
                self.active = False
                self.speed = 20

            def render(self):
                if self.active == True:
                    Sprite.pen.shapesize(0.1, 0.1, 0)
                    Sprite.pen.goto(self.x, self.y)
                    Sprite.pen.shape(self.shape)
                    Sprite.pen.color(self.color)
                    Sprite.pen.stamp()
                
            def move(self):
                if self.active == True:
                    self.dx = math.cos(self.heading * 3.14159 / 180) * self.speed
                    self.dy = math.sin(self.heading * 3.14159 / 180) * self.speed
                    
                    self.x += self.dx
                    self.y += self.dy
                        
                    # Moves off screen
                    if self.x < -600 or self.x > 600 or self.y > 400 or self.y < -400:
                        self.x = -1000
                        self.y = 0
                        self.active = False
                        
                    if random.randint(0, 100) > 80:
                        self.x = -1000
                        self.y = 0
                        self.active = False

        global sprites                
        sprites = []

        global defender, defender_weapons
        defenders = []
        defender_weapons = []

        global attacker, attacker_weapons
        attackers = []
        attacker_weapons = []

        global particles
        particles = []

        colors = ["red", "white", "orange", "yellow"]

        for _ in range(50):
            color = random.choice(colors)
            particles.append(Particle(-1000, 0, "circle", color))

        # Defenders
        for _ in range(num_of_defenders):
            x = random.randint(-500, -300)
            y = random.randint(-300, 300)
            defenders.append(Defender(x, y, "circle", "blue"))

        # Attackers
        for _ in range(num_of_attackers):
            x = random.randint(300, 500)
            y = random.randint(-300, 300)
            attackers.append(Attacker(x, y, "circle", "red"))
            attackers[-1].speed = random.randint(2, 5)
            attackers[-1].heading = random.randint(160, 200)

        # Defender Weapons
        for _ in range(num_of_defender_weapons):
            x = -1000
            y = -1000
            defender_weapons.append(DefenderWeapon(x, y, "circle", "lightblue"))
            defender_weapons[-1].active = False

        # Attacker weapons
        for _ in range(num_of_attacker_weapons):
            x = -1000
            y = -1000
            attacker_weapons.append(DefenderWeapon(x, y, "circle", "pink"))
            attacker_weapons[-1].active = False

        # adding defenders
        def add_defender(x, y):
            global spare_defenders
            if spare_defenders >0:
                defenders.append(Defender(x, y, "circle", "blue"))
                defender_weapons.append(DefenderWeapon(-1000, -1000, "circle", "lightblue"))
                defender_weapons[-1].active = False
                spare_defenders -= 1

        wn.listen
        wn.onclick(add_defender)

        # Main game loop
        while True:
            # Assign weapon to sprite
            for weapon in defender_weapons:
                if weapon.active == False:
                    defender = random.choice(defenders)
                    weapon.x = defender.x
                    weapon.y = defender.y
                    weapon.active = True
                    
                    # Find enemy to aim at
                    attacker = random.choice(attackers)
                    weapon.heading = math.atan2(attacker.y - defender.y, attacker.x - defender.x) * 57.298 
                    break

            # Assign weapon to sprite
            for weapon in attacker_weapons:
                if weapon.active == False:
                    attacker = random.choice(attackers)
                    weapon.x = attacker.x
                    weapon.y = attacker.y
                    weapon.active = True
                    
                    # Find enemy to aim at
                    defender = random.choice(defenders)
                    weapon.heading = math.atan2(defender.y - attacker.y, defender.x - attacker.x) * 57.298
                    break
            
            # Check for collisions between enemy and weapons
            for weapon in defender_weapons:
                if weapon.active == True:
                    for attacker in attackers:
                        if attacker.is_collision(weapon, 12):
                            # Start particles
                            count = 0
                            for particle in particles:
                                if particle.active == False:
                                    particle.active = True
                                    particle.heading = random.randint(0, 360)
                                    particle.x = weapon.x
                                    particle.y = weapon.y
                                    count += 1
                                    
                                    if count > 5:
                                        break
                                    
                            attacker.health -= random.randint(3, 7)
                            
                            if attacker.health <= 0:
                                attackers.remove(attacker)
                            else:
                                attacker.x += weapon.dx
                                attacker.y += weapon.dy
                                
                            weapon.x = -1000
                            weapon.active = False
                            weapon.dx = 0
                            break

            # Check for collisions between enemy and weapons
            for weapon in attacker_weapons:
                if weapon.active == True:
                    for defender in defenders:
                        if defender.is_collision(weapon, 22):
                            # Start particles
                            count = 0
                            for particle in particles:
                                if particle.active == False:
                                    particle.active = True
                                    particle.heading = random.randint(0, 360)
                                    particle.x = weapon.x
                                    particle.y = weapon.y
                                    count += 1
                                    if count > 5:
                                        break
                                    
                            defender.health -= random.randint(3, 7)
                            
                            if defender.health <= 0:
                                defenders.remove(defender)
                                defender_weapons.remove(defender_weapons[-1])
                                
                            weapon.x = -1000
                            weapon.active = False
                            weapon.dx = 0
                            break
                            
            # Check for collisions between attackers and defenders
            for defender in defenders:
                for attacker in attackers:
                    if attacker.is_collision(defender, 30):
                        # Lower attacker health
                        attacker.health -= random.randint(3, 7)
                        if attacker.health <= 0:
                            attackers.remove(attacker)
                        else:
                            attacker.x += 25
                            
                        # Lower defender health
                        defender.health -= random.randint(3, 7)
                        
                        if defender.health <= 0:
                            defenders.remove(defender)
                        break

            # Move
            for sprite in defenders:
                sprite.move()
                sprite.render()

            for sprite in defender_weapons:
                sprite.move()
                sprite.render()
                
            for sprite in attacker_weapons:
                sprite.move()
                sprite.render()
                
            for sprite in attackers:
                sprite.move()
                sprite.render()
                
            for sprite in particles:
                sprite.move()
                sprite.render()        

            Sprite.draw_text(-500, 340, f"Defenders: {len(defenders)}")
            Sprite.draw_text(-100, 340, f"Spare: {spare_defenders}")
            Sprite.draw_text(300, 340, f"Attackers: {len(attackers)}")
            
            # Update screen
            wn.update()
            
            # Check for a win
            if len(attackers) == 0:
                wn.clearscreen()
                wn.bgcolor("black")
                Sprite.draw_text(-120, 0, "The defenders win")
                break
            
            elif len(defenders) == 0:
                wn.clearscreen()
                wn.bgcolor("black")
                Sprite.draw_text(-120, 0, "The attackers win")
                break
            
            # Clear screen
            Sprite.pen.clear()

    btn_params = {
        'padx': 16,
        'pady': 1,
        'bd': 4,
        'fg': 'yellow',
        'bg': 'gray2',
        'font': ('arial', 20),
        'width': 20,
        'height': 2,
        'relief': 'flat',
        'activebackground': 'red2'
    }

    def about():
        def helper():
            about.destroy()
            Play_Space_Battle()      

        
        text = """
        AIM:
        The main objective of the game is to eliminate enemy spaceships while making sure that you do not run out of 
        your spaceships on the battlefield.
    
        LOSING:
        You can lose the game if:
        1) You run out of spaceships while there are still opponent spaceships on the battlefront.
        2) Your spaceships on the battleground are destroyed and the on-field spaceships are 0 (though you may
           still have spare ships).

        WIN:
        You win the game if you destroy all the enemy spaceships.

        CONTROL:
        Left click in the place where you want to deploy your ship in the screen.

        Developed by     : Siddhesh Agarwal
        """

        window1.destroy()

        about = Tk()
        about.title("About")
        about.resizable(0, 0)

        screen = Text(about, height=30, width=120)
        screen.pack()
        screen.config(bg='gray63', border=20)
        screen.insert(END, text)

        BackButton = Button(about, btn_params, text="← Back", command=helper)
        BackButton.place(x=300, y=350)

        about.mainloop()

    # Setting up window
    window1 = Tk()
    window1.resizable(0, 0)
    window1.title("SPACE BATTLE")
    window1.config(bg='gray19', border=5)

    # Play/About Buttons
    PlayButton = Button(window1, btn_params, text="Play", command=play).pack()
    AboutButton = Button(window1, btn_params, text="About", command=about).pack()

    # Keeps Window Open
    window1.mainloop()
