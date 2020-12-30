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
        self.type = "bullet"
        self.alive = True
        self.angle = angle
        self.x, self.y = x, y
        self.sprite = resources.createBullet()
        self.sprite.rotation = self.angle
        self.velocity_x = math.cos(math.radians(-self.angle)) * self.speed
        self.velocity_y = math.sin(math.radians(-self.angle)) * self.speed

    def check_bounds(self):
        # If the bullet goes out of bounds, kill it
        min_x = 0 + self.sprite.image.width / 2
        min_y = 0 - self.sprite.image.height / 2
        max_x = 1920 - self.sprite.image.width / 2
        max_y = 1080 - self.sprite.image.height / 2
        if self.x < min_x:
            self.alive = False
        elif self.x > max_x:
            self.alive = False
        elif self.y < min_y:
            self.alive = False
        elif self.y > max_y:
            self.alive = False

    def check_collision(self, game_objects):
        # Go through all the game objects, excluding the first (the player)
        for obj in game_objects[1:]:
            # Don't check for collision with self
            if ( (obj.x - obj.sprite.width/2) < (self.x - self.sprite.width/2) and
                    (obj.x + obj.sprite.width/2) > (self.x + self.sprite.width/2) and
                    (obj.y - obj.sprite.height/2) < (self.y - self.sprite.height/2) and
                    (obj.y + obj.sprite.height/2) > (self.y + self.sprite.height/2) ):
                self.alive = False
                obj.alive = False

    def draw(self):
        # Draw the sprite to the screen
        self.sprite.draw()

    def update(self, dt, game_objects):
        # Update position according to velocity and time
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

        # Kill if out of bounds
        self.check_bounds()

        # See if the bullet has collided with an enemy
        self.check_collision(game_objects)

        # Update sprite with correct location
        self.sprite.x = self.x
        self.sprite.y = self.y
