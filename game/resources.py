import pyglet


pyglet.resource.path = ['./Assets']
pyglet.resource.reindex()

def centerImage(image):
    """Sets and image's anchor point to its center"""
    image.anchor_x = image.width // 2

def create_background():
    """Creates the sprite for the background"""
    background_image = pyglet.resource.image("Backgrounds/Nebula Blue.png")
    background_sprite = pyglet.sprite.Sprite(img=background_image, x=0, y=0)
    return background_sprite;

def create_player():
    """Creates the sprite for the player"""
    player_image = pyglet.resource.image("Sprites/Player.png")
    centerImage(player_image)
    player_sprite = pyglet.sprite.Sprite(img=player_image, x=1920 // 2, y=1080 // 2)
    player_sprite.scale = 1
    return player_sprite;

# Sprites
background_sprite = create_background()

# Labels
score_label = pyglet.text.Label(text="Score: 0", x = 1920//2, y = 1080 - 32)
round_label = pyglet.text.Label(text="Round 1", x = 32, y = 32)
