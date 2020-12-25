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

pyglet.resource.path = ['./Assets']
pyglet.resource.reindex()
game_window = pyglet.window.Window(1920, 1080)

# Sprites
background_image = pyglet.resource.image("Backgrounds/Nebula Blue.png")

def centerImage(image):
    """Sets and image's anchor point to its center"""
    image.anchor_x = image.width // 2

if __name__ == '__main__':
    pyglet.app.run()