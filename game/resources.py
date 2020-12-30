import pyglet
from . import Player, Enemy, Bullet


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

def createHarderBackground():
    """Creates the sprite for the background"""
    background_image = pyglet.resource.image("Backgrounds/Nebula Aqua-Pink.png")
    background_sprite = pyglet.sprite.Sprite(img=background_image, x=0, y=0)
    return background_sprite;

def createHellBackground():
    """Creates the sprite for the background"""
    background_image = pyglet.resource.image("Backgrounds/Nebula Red.png")
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
    """Creates the sprite for the enemy"""
    enemy_image = pyglet.resource.image("Sprites/Enemy.png")
    centerImage(enemy_image)
    enemy_sprite = pyglet.sprite.Sprite(img=enemy_image, x=1920 // 2, y=1080 // 2)
    enemy_sprite.scale = 1
    return enemy_sprite;

def createBullet():
    """Creates the sprite for the bullet"""
    bullet_image = pyglet.resource.image("Sprites/Bullet.png")
    centerImage(bullet_image)
    bullet_sprite = pyglet.sprite.Sprite(img=bullet_image, x=1920 // 2, y=1080 // 2)
    bullet_sprite.scale = 1
    return bullet_sprite


# Class for storing game resources
class Game():
    def __init__(self):
        # Labels
        self.score_label = pyglet.text.Label(text="Score: 0", x=1920 // 2, y=1080 - 32)
        self.round_label = pyglet.text.Label(text="Round: 1", x=32, y=32)
        self.life_label = pyglet.text.Label(text="Lives: 3", x=32, y=64)
        self.kills_label = pyglet.text.Label(text="Kills: 0", x=32, y=96)

        # Sprites
        self.background_sprite = createBackground()
        self.player = Player.Player()

        # Lists of stuff
        self.enemy_list = []
        self.enemy_count = 0
        self.bullet_list = []
        self.bullet_count = 0
        self.objects = [self.player] + self.enemy_list + self.bullet_list

        # Other game stuff
        self.counter = 0
        self.spawnRate = 1
        self.difficulty = 1
        self.stage = 1
        self.score = 0

        # Audio stuff
        self.music = pyglet.resource.media('Sounds/Never Run.mp3')
        self.gunshot = pyglet.media.StaticSource(pyglet.media.load('Assets/Sounds/Gunshot.wav'))
        self.new_stage = pyglet.media.StaticSource(pyglet.media.load('Assets/Sounds/Guitar Riff.wav'))

    def spawnEnemy(self, difficulty):
        self.enemy = Enemy.Enemy(difficulty)
        self.enemy_list.append(self.enemy)

    def killEnemy(self, enemy):
        self.enemy_index = self.objects.index(enemy) - 1
        self.enemy_list.pop(self.enemy_index)
        self.player.kills += 1
        self.score += 100 * self.difficulty

    def fireBullet(self):
        self.gunshot.play()
        self.bullet = Bullet.Bullet(self.player.sprite.rotation, self.player.sprite.x, self.player.sprite.y)
        self.bullet_list.append(self.bullet)

    def killBullet(self, bullet):
        self.bullet_index = self.objects.index(bullet) - self.enemy_count - 1
        self.bullet_list.pop(self.bullet_index)

    def update(self, dt):
        # Update the background if the difficulty gets high enough
        if (self.difficulty > 10) and (self.stage != 2 or self.stage != 2):
            if self.difficulty > 30 and self.stage != 3:
                self.new_stage.play()
                self.stage = 3
                self.background_sprite = createHellBackground()
            elif self.difficulty < 30 and self.new_stage != 2:
                self.new_stage.play()
                self.stage = 2
                self.background_sprite = createHarderBackground()


        # See if we need to spawn in an enemy
        self.spawnRate = (1000/(self.score + 1))**(1/5)
        self.counter += dt
        if self.player.alive:
            if self.counter > self.spawnRate:
                self.spawnEnemy(self.difficulty)
                self.counter = 0
                self.difficulty += 1

        # Update game objects list and counts
        self.objects = [self.player] + self.enemy_list + self.bullet_list
        self.enemy_count = len(self.enemy_list)
        self.bullet_count = len(self.bullet_list)

        # Update each object
        for obj in self.objects:
            # If the object is 'alive', update it normally
            if obj.alive:
                obj.update(dt, self.objects)
            else:
                # Get rid of bullets that aren't 'alive'
                if obj.type == "bullet":
                    self.killBullet(obj)
                # Get rid of enemies that aren't 'alive
                elif obj.type == "enemy":
                    self.killEnemy(obj)

        # Update labels
        self.score_label.text = "Score: " + str(self.score)
        self.life_label.text = "Lives: " + str(self.player.lives)
        self.kills_label.text = "Kills: " + str(self.player.kills)

