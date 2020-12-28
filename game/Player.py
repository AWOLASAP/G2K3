import math
from pyglet.window import key
from . import resources


class Player():
    """Physical object that responds to user input"""

    def __init__(self, *args, **kwargs):

        # Base stuff for a sprite
        self.sprite = resources.create_player()
        self.x, self.y = 1920/2, 1080/2
        self.velocity_x, self.velocity_y = 0, 0

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

    def check_bounds(self):
        # The keep the player in the bounds of the screen
        min_x = 0 + self.sprite.image.width / 4
        min_y = 0
        max_x = 1920 - self.sprite.image.width / 4
        max_y = 1080 - self.sprite.image.height / 2
        if self.x < min_x:
            self.x = min_x
        elif self.x > max_x:
            self.x = max_x
        if self.y < min_y:
            self.y = min_y
        elif self.y > max_y:
            self.y = max_y

    def draw(self):
        # Draw the sprite to the screen
        self.sprite.draw()

    def update(self, dt):
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

        # Keep within scree bounds
        self.check_bounds()

        # Update sprite with correct location
        self.sprite.x = self.x
        self.sprite.y = self.y