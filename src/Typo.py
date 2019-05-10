import random
import arcade
import enum
import src.Words
import src.Cloud
import pygame

pygame.mixer.init()

# Sound effect initialise
hit = pygame.mixer.Sound('.././soundEffect/hit.wav')

music = pygame.mixer.music.load('.././soundEffect/backgroundmusic.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class GameStates(enum.Enum):
    GAME_OVER = 0
    RUNNING = 1


class Typo(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, title="Typo Game")

        # file_path = os.path.dirname(os.path.abspath(__file__))
        # os.chdir(file_path)

        self.screen_width = width
        self.screen_height = height
        self.score = int()
        self.lives = int()
        self.focus_word = None  # The word that is currently being typed.
        self.word_list = set()
        self.state = None
        self.background = None
        # set of cloud list
        self.cloud_list = set()

    def setup(self):
        self.score = 0
        self.lives = 4  # edit the lives maybe 5
        self.focus_word = None  # The word that is currently being typed.
        self.word_list = set()
        self.state = GameStates.RUNNING
        self.background = arcade.load_texture(".././images/background1.png")
        # set of cloud list
        self.cloud_list = set()

        for i in range(5):
            self.show_word()

        # for in range to show the clouds
        for i in range(40):
            self.show_cloud()



    def start_game(self):
        for word in self.word_list:
            word.draw()

        arcade.draw_text(f"Score(s): {self.score}", 15, 15, arcade.color.RADICAL_RED, 15)
        arcade.draw_text(f"Live(s): {self.lives}", self.screen_width - 15, 15,
                         arcade.color.RADICAL_RED, 15, align="right", anchor_x="right", anchor_y="baseline")

    def end_game(self):
        arcade.draw_text("GAME OVER",
                         self.screen_width / 2, (self.screen_height / 2) + 60,
                         arcade.color.WHITE, 54,
                         align="center", anchor_x="center", anchor_y="center"
                         )

        arcade.draw_text("Press SPACE BAR to restart",
                         self.screen_width / 2, (self.screen_height / 2),
                         arcade.color.WHITE, 24,
                         align="center", anchor_x="center", anchor_y="center"
                         )

        arcade.draw_text(f"Current score : {self.score}", 15, 15, arcade.color.WHITE, 14, )

    def on_draw(self):
        arcade.start_render()

        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        # for cloud in cloud list to draw the cloud
        for cloud in self.cloud_list:
            cloud.draw_cloud()


        if self.state == GameStates.RUNNING:
            self.start_game()
        else:
            self.end_game()

    # def to show all the cloud by adding to the list as same as show word
    def show_cloud(self):
        self.cloud_list.add(src.Cloud.Cloud(self.screen_width, self.screen_height))

    def show_word(self):

        # Find a row that's currently not occupied by another word.
        # to prevent showing every word in the same row which maybe cause overlapping.
        randrow = int()
        used_row = set()
        while True:
            randrow = random.randrange(20)
            for word in self.word_list:
                used_row.add(word.row)

            # The row I want should be unused
            if randrow not in used_row:
                break

        # Find the word which has different in the first character with another word.
        used_char = set()
        for word in self.word_list:
            used_char.add(word.words[0])

        randword = str()

        while True:
            randword = random.choice(src.Words.WORD_LIST)
            # The word I want should not have the same first character as another word.
            if randword[0] not in used_char:
                break
        self.word_list.add(src.Words.Words(randword, randrow, self.screen_width, self.screen_height))

    def update(self, delta_time):

        # to move the cloud
        # for cloud in cloud list then move x as same as the word but use cloud speed instead of 1
        # if x<0; reset the cloud pos.
        for cloud in self.cloud_list:
            cloud.x -= cloud.speed * delta_time
            if cloud.x < 0:
                cloud.reset_position(self.screen_width, self.screen_height)

        if self.state == GameStates.RUNNING:
            for word in self.word_list:

                # to decrease the x-range makes the word looks like moving to the left.
                word.x -= 1.25

                # in case of the word has been left the window.
                if word.x < 0:

                    # loss the word, loss 1 life.
                    self.lives -= 1

                    # reset the focus word
                    if self.focus_word == word:
                        self.focus_word = None

                    # remove that word from word list to prevent duplication when it picks the same word to show again.
                    self.word_list.discard(word)

                    # continue
                    self.show_word()

            # died
            if self.lives <= 0:
                self.state = GameStates.GAME_OVER

    def on_key_press(self, key, modifiers):
        # other keys
        if key > 127:
            return
        hit.play()
        # if game over and player presses space bar.
        if self.state == GameStates.GAME_OVER and key == 32:
            self.setup()
            self.state = GameStates.RUNNING

        # start with no focus word (didn't type any keys yet)
        if self.focus_word is None:

            # loop the word out
            for w in self.word_list:

                # the first character of the word = key
                if w.words[0] == chr(key):
                    # change color
                    self.focus_word = w

                    # remove that letter
                    w.encounter()

                    w.in_focus = True
                    break
        else:
            # in case of the first character of focused word = key
            if self.focus_word.words[0] == chr(key):

                # remove that one
                self.focus_word.encounter()

                # in case of no more letters in focused word left
                if self.focus_word.words == "":
                    # remove that word from the list
                    # (It won't show the same word player has played)
                    self.word_list.discard(self.focus_word)

                    # reset focus_word
                    self.focus_word = None

                    # increase score by 1
                    self.score += 10

                    # continue
                    self.show_word()


def main():
    game = Typo(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
