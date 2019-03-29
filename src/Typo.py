import arcade
class Typo(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, title="Typo Game")
        arcade.set_background_color((5, 2, 27))
        self.screen_width = width
        self.screen_height = height
        # self.high_score = int()
        self.score = int()
        self.lives = int()
        self.state = None
        self.focus_word = None  #The word that is currently being typed.
        self.word_list = set()
        self.star_list = set()