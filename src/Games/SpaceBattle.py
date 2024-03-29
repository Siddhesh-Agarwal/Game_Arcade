# Game_Arcade/Games/SpaceBattle.py
import math
import random
import time
import turtle


def Play():
    root = turtle.Screen()
    root.setup(1200, 800)
    root.bgcolor("black")
    root.title("Bpace Battle")
    root.tracer(0)

    # Testing / Start of game values
    num_of_defenders = 30  # Total possible number of defenders
    num_of_attackers = 200  # Total possible number of Attackers
    defender_hits_per_sec = 30  # Number of defender hits per second
    attacker_hits_per_sec = 20  # Number of attacker hits per second

    # Main class of the game
    class Sprite:
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
            d = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
            if d < tolerance:
                return True
            else:
                return False

    # Subclass of Sprite class. Class for defenders
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
            if self.health > 35:
                color = "green"
            elif self.health > 15:
                color = "yellow"
            else:
                color = "red"

            Sprite.pen.goto(self.x + 20, self.y)
            Sprite.pen.setheading(90)
            Sprite.pen.pendown()
            Sprite.pen.width(3)
            Sprite.pen.color(color)
            Sprite.pen.circle(20)
            Sprite.pen.penup()

    # Subclass of Sprite class. Class for defender weapons
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

    # Subclass of Sprite class. Class for Attackers
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

            if self.y > 390:
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

    defenders = []  # List containing Defender sprites
    defender_weapons = []  # List containing Defender Weapon sprites
    attackers = []  # List containing Attacker sprites
    attacker_weapons = []  # List containing Attacker Weapon sprites
    particles = []  # List containing Particles projected

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

    # Weapons
    for _ in range(defender_hits_per_sec):
        x = -1000
        y = -1000
        defender_weapons.append(DefenderWeapon(x, y, "circle", "lightblue"))
        defender_weapons[-1].active = False

    for _ in range(attacker_hits_per_sec):
        x = -1000
        y = -1000
        attacker_weapons.append(DefenderWeapon(x, y, "circle", "pink"))
        attacker_weapons[-1].active = False

    def add_defender(x, y):
        defenders.append(Defender(x, y, "circle", "blue"))
        defender_weapons.append(DefenderWeapon(-1000, -1000, "circle", "lightblue"))
        defender_weapons[-1].active = False

    root.onclick(add_defender)

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
                weapon.heading = (
                    math.atan2(attacker.y - defender.y, attacker.x - defender.x)
                    * 57.298
                )
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
                weapon.heading = (
                    math.atan2(defender.y - attacker.y, defender.x - attacker.x)
                    * 57.298
                )
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

        Sprite.draw_text(-300, 340, f"Defenders: {len(defenders)}")
        Sprite.draw_text(200, 340, f"Attackers: {len(attackers)}")
        root.update()  # Update screen

        # Check for a win
        if len(attackers) == 0:  # Defender win if number of attackers is zero
            print("The defenders win.")  # Display winner in IDE
            time.sleep(3)  # 3 second sleep
            exit()  # closes window

        if len(defenders) == 0:  # Attackers win if number of attackers is zero
            print("The attackers win.")  # Display winner in IDE
            time.sleep(3)  # 3 second sleep
            exit()  # closes window

        Sprite.pen.clear()  # Clear screen


def About():
    return """
    AIM:
    The main objective of the game is to eliminate enemy spaceships while making sure that you do not run out of your spaceships on the battlefield.

    LOSING:
    You can lose the game if:

    You run out of spaceships while there are still opponent spaceships on the battlefront.
    Your spaceships on the battleground are destroyed and the on-field spaceships are 0 (though you may still have spare ships).
    WIN:
    You win the game if you destroy all the enemy spaceships.

    CONTROL:
    Left click in the place where you want to deploy your ship in the screen"""
