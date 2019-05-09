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

        # change background if have time.
        arcade.set_background_color(arcade.color.BLACK)
        self.screen_width = width
        self.screen_height = height
        self.score = int()
        self.lives = int()
        self.focus_word = None  # The word that is currently being typed.
        self.word_list = set()
        self.state = None
        self.word = src.Words

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


    def show_word(self):
        self.word_list.add(self.word.Words(random.choice(self.word.WORD_LIST), random.randrange(20)
                                           , self.screen_width, self.screen_height))
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

    def update(self, delta_time: float):
        if self.state == GameStates.RUNNING:
            for word in self.word_list:
                # to decrease the x-range makes the word looks like moving to the left.
                word.x -= 1
                #in case of the word has been left the window.
                if word.x < 0:
                    #loss the word, loss 1 life.
                    self.lives -= 1
                    #reset the focus word
                    if word == self.focus_word:
                        self.focus_word is None
                    #remove that word from word list to prevent duplication when it picks the same word to show again.
                    self.word_list.discard(word)
                    #continue
                    self.show_word()
            # died
            if self.lives <= 0:
                self.state = GameStates.GAME_OVER




    def on_key_press(self, key, modifiers):
        #start with no focus word (didn't type any keys yet)
        if self.focus_word is None:
            #loop the word out
            for word in self.word_list:
                # the first character of the word = key
                if word.words[0] == chr(key):
                    #change color
                    self.focus_word = word
                    #remove that letter
                    word.encounter()
                    word.in_focus = True
                    break
        else:
            #in case of the first character of focused word = key
            if self.focus_word.words[0] == chr(key):
                #remove that one
                self.focus_word.encounter()
                #in case of no more letters in focused word left
                if self.focus_word.words is None:
                    #remove that word from the list
                    # (It won't show the same word player has played)
                    self.word_list.discard(self.focus_word)
                    #reset focus_word
                    self.focus_word = None
                    #increase score by 1
                    self.score +=1
                    #continue
                    self.show_word()








def main():
    game = Typo(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
