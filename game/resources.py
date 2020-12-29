import pyglet


pyglet.resource.path = ['./Assets']
pyglet.resource.reindex()

def centerImage(image):
    """Sets and image's anchor point to its center"""
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

def createBackground():
    """Creates the sprite for the background"""
    background_image = pyglet.resource.image("Backgrounds/Nebula Blue.png")
    background_sprite = pyglet.sprite.Sprite(img=background_image, x=0, y=0)
    return background_sprite;

def createPlayer():
    """Creates the sprite for the player"""
    player_image = pyglet.resource.image("Sprites/Player.png")
    centerImage(player_image)
    player_sprite = pyglet.sprite.Sprite(img=player_image, x=1920 // 2, y=1080 // 2)
    player_sprite.scale = 1
    return player_sprite;

def createEnemy():
    """Creates the sprite for the player"""
    enemy_image = pyglet.resource.image("Sprites/Enemy.png")
    centerImage(enemy_image)
    enemy_sprite = pyglet.sprite.Sprite(img=enemy_image, x=1920 // 2, y=1080 // 2)
    enemy_sprite.scale = 1
    return enemy_sprite;


# Sprites
background_sprite = createBackground()

# Labels
score_label = pyglet.text.Label(text="Score: 0", x = 1920//2, y = 1080 - 32)
round_label = pyglet.text.Label(text="Round 1", x = 32, y = 32)
