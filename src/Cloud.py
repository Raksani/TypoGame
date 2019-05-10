import random
import arcade


class Cloud:
    def __init__(self, screen_width, screen_height):
        # to make it move it different dimension from the words
        # in the little right side
        self.x = random.randrange(screen_width + 200)
        self.y = random.randrange(screen_height)
        self.size = random.randrange(10)
        self.speed = random.randrange(20, 40)
        self.color = random.choice([arcade.color.WHITE, arcade.color.GRAY])

    def draw_cloud(self):
        arcade.draw_circle_filled(self.x, self.y, self.size, self.color)

    def reset_position(self, screen_width, screen_height):
        self.x = random.randrange(screen_width, screen_width + 100)
        self.y = random.randrange(screen_height)
