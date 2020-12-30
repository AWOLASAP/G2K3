"""
  ____ ____  _  _______
 / ___|___ \| |/ |___ /
| |  _  __) | ' /  |_ \
| |_| |/ __/| . \ ___) |
 \____|_____|_|\_|____/

 This is the main file for all the main file stuff.
"""
import pyglet
#from game import resources, Player, Enemy, Bullet
from game import resources

# Window class for stuff
game_window = pyglet.window.Window(1920, 1080)

# Game class, with all game stuff inside
game = resources.Game()

@game_window.event
def on_draw():
    # Clear the game window
    game_window.clear()

    # Draw background
    game.background_sprite.draw()

    # Draw game objects
    for obj in game.objects:
        obj.draw()

    # Draw score elements
    game.score_label.draw()
    game.round_label.draw()
    game.life_label.draw()
    game.kills_label.draw()


# Whenever a key is pressed this funciton is called
@game_window.event()
def on_key_press(key, modifiers):
    # Tell the player what keys were pressed
    game.player.on_key_press(key, modifiers)

# Whenever a key is released this funciton is called
@game_window.event()
def on_key_release(key, modifiers):
    # Tell the player what keys were released
    game.player.on_key_release(key, modifiers)

# Whenever the mouse is moved, this function is called
@game_window.event()
def on_mouse_motion(x, y, dx, dy):
    # Update player with the correct mouse location
    game.player.on_mouse_motion(x, y)

# Whenever the mouse is pressed, this function is called
@game_window.event()
def on_mouse_press(x, y, button, modifiers):
    # "Fire" the gun
    game.fireBullet()

if __name__ == '__main__':
    # Call the update function every udpate tick (double max framerate)
    pyglet.clock.schedule_interval(game.update, 1 / 288.0)

    # Run
    game.music.play()
    pyglet.app.run()
