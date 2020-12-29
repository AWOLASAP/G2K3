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
from game import resources, Player, Enemy, Bullet

# Window class for stuff
game_window = pyglet.window.Window(1920, 1080)

# Game Objects, stuff like the players and enemies go in here
player = Player.Player()
enemy_list = []
bullet_list = []
global game_objects
game_objects = [player] + enemy_list + bullet_list

def spawnEnemy():
    enemy = Enemy.Enemy()
    enemy_list.append(enemy)

def killEnemy(enemyIndex):
    enemy_list.pop(enemyIndex)

@game_window.event
def on_draw():
    # Clear the game window
    game_window.clear()

    # Draw background
    resources.background_sprite.draw()

    # Draw game objects
    for obj in game_objects:
        obj.draw()

    # Draw score elements
    resources.score_label.draw()
    resources.round_label.draw()


# Whenever a key is pressed this funciton is called
@game_window.event()
def on_key_press(key, modifiers):
    # Tell the player what keys were pressed
    player.on_key_press(key, modifiers)

    # Debugging tool. Create enemy when 'e' is pressed
    # Oldest enemy is killed when 'k' is pressed
    if key == pyglet.window.key.E:
        spawnEnemy()
    if key == pyglet.window.key.K:
        killEnemy(0)


# Whenever a key is released this funciton is called
@game_window.event()
def on_key_release(key, modifiers):
    # Tell the player what keys were released
    player.on_key_release(key, modifiers)

# Whenever the mouse is moved, this function is called
@game_window.event()
def on_mouse_motion(x, y, dx, dy):
    # Update player with the correct mouse location
    player.on_mouse_motion(x, y)

# Whenever the mouse is pressed, this function is called
@game_window.event()
def on_mouse_press(x, y, button, modifiers):
    # "Fire" the gun
    bullet = Bullet.Bullet(player.sprite.rotation, player.sprite.x, player.sprite.y)
    bullet_list.append(bullet)

# Update loop called every update tick
def update(dt):
    # Update game objects list
    global game_objects
    game_objects = [player] + enemy_list + bullet_list

    # Update each object
    for obj in game_objects:
        obj.update(dt)

if __name__ == '__main__':
    # Call the update function every udpate tick (double max framerate)
    pyglet.clock.schedule_interval(update, 1 / 288.0)

    # Run
    pyglet.app.run()
