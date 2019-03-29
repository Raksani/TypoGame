import arcade
import enum
class GameStates(enum.Enum):
    GAME_OVER = 0
    RUNNING = 1

class Typo(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, title="Typo Game")
        arcade.set_background_color((5, 2, 27))
        self.screen_width = width
        self.screen_height = height
        # self.high_score = int()
        self.score = int()
        self.lives = int()
        self.focus_word = None  #The word that is currently being typed.
        self.word_list = set()

    def setup(self):
        self.score = 0
        self.lives = 3 # edit the lives maybe 4
        self.state = GameStates.RUNNING
        self.focus_word = None #The word that is currently being typed.
        self.word_list = set()


    def draw_game(self):
        for word in self.word_list:
            word.draw()

        arcade.draw_text(f"Score : {self.score}", 15, 15, arcade.color.WHITE, 15)
        arcade.draw_text(f"Lives : {self.lives}", self.screen_width - 15, 15, arcade.color.WHITE, 14, align="right",
                         anchor_x="right", anchor_y="baseline")

    def on_key_press(self, symbol: int, modifiers: int):


