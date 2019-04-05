import arcade
import enum

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class GameStates(enum.Enum):
    GAME_OVER = 0
    RUNNING = 1


class Typo(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, title="Typo Game")
        self.state = GameStates.RUNNING
        arcade.set_background_color((5, 2, 27))
        self.screen_width = width
        self.screen_height = height
        # self.high_score = int()
        self.score = int()
        self.lives = int()
        self.focus_word = None  # The word that is currently being typed.
        self.word_list = set()

    def setup(self):
        self.score = 0
        self.lives = 3  # edit the lives maybe 4
        self.focus_word = None  # The word that is currently being typed.
        self.word_list = set()

    def show_word(self):
        for word in self.word_list:
            word.draw()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def main():
    game = Typo(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
