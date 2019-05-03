import arcade
# from Typo import Typo
WORD_LIST = [
    "software", "computer", "java", "python", "arcade", "game", "laptop", "www",
    "https", "glasses"
]
class Words:
    def __init__(self, words, row, screen_width, screen_height):
        self.words = words
        self.row = row
        self.x = screen_width
        self.y = screen_height - 40
        self.in_focus = False
        self.color = arcade.color.WHITE

    def change_color(self):
        if self.in_focus:
            self.color = arcade.color.RED
        else:
            self.color = arcade.color.WHITE

    def draw(self):
        arcade.draw_text(self.words, self.x, self.y, self.color, 14)

    # decrease the word 1 by 1 by typing.
    def encounter(self):
        self.words = self.words[1:]

