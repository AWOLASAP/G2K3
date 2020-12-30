import math
from pyglet.window import key
from . import resources


class Player():
    """Class for all things the player needs"""

    def __init__(self, *args, **kwargs):

        # Base stuff for a sprite
        self.type = "player"
        self.alive = True
        self.lives = 3
        self.kills = 0
        self.sprite = resources.createPlayer()
        self.x, self.y = 1920/2, 1080/2
        self.velocity_x, self.velocity_y = 0, 0
        self.new_angle = 0

        # Set some easy-to-tweak constants
        self.speed = 1000.0

        # Keys to keep track of for the players actions
        self.keys = dict(left=False, right=False, up=False, down=False)

    def on_key_press(self, symbol, modifiers):
        # Keep track of keys that were pressed
        if symbol == key.W:
            self.keys['up'] = True
        if symbol == key.S:
            self.keys['down'] = True
        elif symbol == key.A:
            self.keys['left'] = True
        elif symbol == key.D:
            self.keys['right'] = True

    def on_key_release(self, symbol, modifiers):
        # Keep track of keys that were released
        if symbol == key.W:
            self.keys['up'] = False
        if symbol == key.S:
            self.keys['down'] = False
        elif symbol == key.A:
            self.keys['left'] = False
        elif symbol == key.D:
            self.keys['right'] = False

    def on_mouse_motion(self, mouse_x, mouse_y):
        # Angle the player according to the mouse location
        if (mouse_x - self.x) == 0 and (mouse_y > self.y):
            self.new_angle = 90
        elif (mouse_x - self.x) == 0 and (mouse_y < self.y):
            self.new_angle = -90
        else:
            self.new_angle = math.degrees(math.atan2((mouse_y - self.y), (mouse_x - self.x)))

    def check_bounds(self):
        # The keep the player in the bounds of the screen
        min_x = 0 + self.sprite.image.width / 2
        min_y = 0 + self.sprite.image.height / 2
        max_x = 1920 - self.sprite.image.width / 2
        max_y = 1080 - self.sprite.image.height / 2
        if self.x < min_x:
            self.x = min_x
        elif self.x > max_x:
            self.x = max_x
        if self.y < min_y:
            self.y = min_y
        elif self.y > max_y:
            self.y = max_y

    def check_collision(self, enemy_list):
        for enemy in enemy_list[1:]:
            x_distance = enemy.x - self.x
            y_distance = enemy.y - self.y
            distance = math.hypot(x_distance, y_distance)
            if distance < 75 and enemy.type == "enemy":
                self.lives -= 1
                enemy.alive = False

    def draw(self):
        # Draw the sprite to the screen
        self.sprite.draw()

    def update(self, dt, game_objects):
        # Reset velocity
        self.velocity_x = 0
        self.velocity_y = 0

        # Change velocity based on keys pressed
        if self.keys['left']:
            self.velocity_x -=  self.speed
        if self.keys['right']:
            self.velocity_x += self.speed
        if self.keys['up']:
            self.velocity_y +=  self.speed
        if self.keys['down']:
            self.velocity_y -= self.speed

        # Update position according to velocity and time
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        # Keep within screen bounds
        self.check_bounds()

        # See if the player collided with an enemy
        self.check_collision(game_objects)

        # Die if no lives
        if self.lives <= 0:
            self.alive = False

        # Update sprite with correct location and rotation
        self.sprite.x = self.x
        self.sprite.y = self.y
        self.sprite.rotation = -self.new_angle
