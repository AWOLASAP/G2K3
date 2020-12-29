import math
import random
from pyglet.window import key
from . import resources


class Bullet():
    """Class for all things bullets need"""

    def __init__(self, angle, x, y):
        # Tweakable constants
        self.speed = 3000.0

        # Base stuff for a sprite
        self.player = False
        self.alive = True
        self.angle = angle
        self.x, self.y = x, y
        self.sprite = resources.createBullet()
        self.sprite.rotation = self.angle
        self.velocity_x = math.cos(math.radians(-self.angle)) * self.speed
        self.velocity_y = math.sin(math.radians(-self.angle)) * self.speed

    def check_bounds(self):
        # The keep the bullet in the bounds of the screen
        min_x = 0 + self.sprite.image.width / 2
        min_y = 0 - self.sprite.image.height / 6
        max_x = 1920 - self.sprite.image.width / 2
        max_y = 1080 - self.sprite.image.height
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
        # Update position according to velocity and time
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        # Keep within screen bounds
        self.check_bounds()

        # Update sprite with correct location
        self.sprite.x = self.x
        self.sprite.y = self.y
