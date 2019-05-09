import random

import arcade
import enum

import src.Words

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


class GameStates(enum.Enum):
    GAME_OVER = 0
    RUNNING = 1


class Typo(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, title="Typo Game")
        self.state = GameStates.RUNNING

        # change background if have time.
        arcade.set_background_color(arcade.color.BLACK)

        self.screen_width = width
        self.screen_height = height

        self.score = int()
        self.lives = int()
        self.focus_word = None  # The word that is currently being typed.
        self.word_list = set()
        self.state = None

    def setup(self):
        self.score = 0
        self.lives = 3  # edit the lives maybe 4
        self.focus_word = None  # The word that is currently being typed.
        self.word_list = set()
        self.state = GameStates.RUNNING

        for i in range(3):
            self.show_word()

    def start_game(self):
        for word in self.word_list:
            word.draw()

        arcade.draw_text(f"Score(s): {self.score}", 15, 15, arcade.color.RADICAL_RED,15)
        arcade.draw_text(f"Live(s): {self.lives}", self.screen_width - 15, 15,
                         arcade.color.RADICAL_RED, 15, align = "right", anchor_x="right",anchor_y="baseline")

    def on_draw(self):
        arcade.start_render()
        if self.state == GameStates.RUNNING:
            self.start_game()

        # #Find a row that's currently not occupied by another word.
        # def new_row(self):
        #     row2 = set()
        #     while True:
        #         # margin between each row. span to fit the window
        #         row = random.randrange(5)
        #         for word in self.word_list:
        #             row2.add(word.row)
        #         if row not in row2:
        #             break

        # Find the word which has different in first letter with another word.

    def show_word(self):
        self.word_list.add(src.Words.Words(random.choice(src.Words.WORD_LIST), random.randrange(20)
                                           , self.screen_width, self.screen_height))

    def update(self, delta_time: float):
        for word in self.word_list:
            # to decrease the x-range makes the word looks like moving to the left.
            word.x -= 1


def main():
    game = Typo(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
