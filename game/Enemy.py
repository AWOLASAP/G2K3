import math
import random
from pyglet.window import key
from . import resources


class Enemy():
    """Class for all things the enemy needs"""

    def __init__(self):

        # Base stuff for a sprite
        self.type = "enemy"
        self.alive = True
        self.sprite = resources.createEnemy()
        self.x, self.y = random.randint(0, 1920), random.randint(0, 1080)
        self.velocity_x, self.velocity_y = 0, 0

        # Tweakable constants
        self.speed = 100.0

    def check_bounds(self):
        # The keep the enemy in the bounds of the screen
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

    def draw(self):
        # Draw the sprite to the screen
        self.sprite.draw()

    def update(self, dt, game_objects):
        # Reset velocity
        self.velocity_x = 0
        self.velocity_y = 0

        # Update position according to velocity and time
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        # Keep within screen bounds
        self.check_bounds()

        # Update sprite with correct location
        self.sprite.x = self.x
        self.sprite.y = self.y
