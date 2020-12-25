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

def centerImage(image):
    """Sets and image's anchor point to its center"""
    image.anchor_x = image.width // 2

# Sprites
background_image = pyglet.resource.image("Backgrounds/Nebula Blue.png")
background_sprite = pyglet.sprite.Sprite(img=background_image, x=0, y=0)

# Labels
score_label = pyglet.text.Label(text="Score: 0", x = game_window.width//2, y = game_window.height - 32)
round_label = pyglet.text.Label(text="Round 1", x = 32, y = 32)

@game_window.event
def on_draw():
    # draw things here
    game_window.clear()

    background_sprite.draw()
    score_label.draw()
    round_label.draw()

if __name__ == '__main__':
        pyglet.app.run()