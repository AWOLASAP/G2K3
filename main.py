"""
  ____ ____  _  _______
 / ___|___ \| |/ |___ /
| |  _  __) | ' /  |_ \
| |_| |/ __/| . \ ___) |
 \____|_____|_|\_|____/

 This is the main file for all the main file stuff.
 Don't use non main file stuff in this file
"""
import pyglet
from game import resources, Player, Enemy

# Window class for stuff
game_window = pyglet.window.Window(1920, 1080)

# Game Objects, stuff like the players and enemies go in here
player = Player.Player()
enemy = Enemy.Enemy()
game_objects = [player, enemy]

@game_window.event
def on_draw():
    # Clear the game window
    game_window.clear()

    # Draw various game objects
    resources.background_sprite.draw()
    resources.score_label.draw()
    resources.round_label.draw()

    # Draw the player
    player.draw()
    enemy.draw()

# Whenever a key is pressed this funciton is called
@game_window.event()
def on_key_press(key, modifiers):
    # Tell the player what keys were pressed
    player.on_key_press(key, modifiers)

# Whenever a key is released this funciton is called
@game_window.event()
def on_key_release(key, modifiers):
    # Tell the player what keys were released
    player.on_key_release(key, modifiers)

# Update loop called every update tick
def update(dt):
    for obj in game_objects:
        obj.update(dt)

if __name__ == '__main__':
    # Call the update function every udpate tick (double max framerate)
    pyglet.clock.schedule_interval(update, 1 / 288.0)

    # Run
    pyglet.app.run()
