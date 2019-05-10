import arcade
# from Typo import Typo
WORD_LIST = ("pull", "record", "untidy", "tested", "ske", "software",
             "heartbreaking", "hurt", "assorted", "servant", "talk",
             "snake", "desk", "advertisement", "balance", "cut", "animated",
             "loaf", "reading", "massive", "pig",
             "ray", "wrestle", "upbeat", "person", "addition", "record", "left",
             "lively", "rain", "tick", "knot", "remarkable", "neat", "yam", "sea",
             "amuse", "whirl", "thoughtful", "milk",
             "female", "threatening", "marked", "linen", "rinse", "word",
             "perfect", "hallowed", "dangerous", "birth", "pumped", "available",
             "coherent", "early", "loss", "dam", "true", "berry",
             "unaccountable", "drop", "nest", "attack", "smoggy",
             "lettuce", "crib", "mighty", "ratty", "short", "tall", "thankful",
             "aunt", "haunt", "wild", "pull", "brave", "property", "vague", "stove",
             "glass", "floor", "cart", "blushing", "yellow",
             "can", "screw", "wonder", "minor", "rotten",
             "exultant", "fearless", "box", "action", "probable", "verdant",
             "warlike", "wrathful", "support", "cooing", "piquant", "instrument",
             "development", "fire", "late", "rainstorm", "sad", "trust", "perform",
             "press", "spotless", "lyrical", "yell", "finger", "load",
             "vivacious", "parsimonious", "quack", "bury", "hellish", "selective",
             "leather", "quilt", "deserve", "obsolete", "repeat", "prose", "real",
             "chief", "delicious", "saw", "fold", "move", "pump", "size", "tart",
             "cover", "pets", "wheel", "mate", "rate", "coach", "honorable", "shake",
             "picture", "sprout", "mother", "toes", "interfere", "skinny", "alarm",
             "authority", "questionable", "cub", "enthusiastic", "organic",
             "step", "behavior", "zonked", "dry", "alcoholic", "average", "stomach",
             "trade", "street", "creepy", "relieved", "use", "animal",
             "distance", "soggy", "part", "worthless", "ball", "precious", "quiet",
             "arithmetic", "excited", "festive", "unequaled", "sincere", "hissing",
             "bruise", "pin", "key", "modern", "pigs", "foregoing", "attempt", "continue",
             "horse", "beautiful", "miscreant", "boorish", "book", "dress", "grey",
             "children", "bustling", "super", "secret", "message", "lock", "giants",
             "squash", "funny", "classy", "mountain", "boil", "far",
             "hand", "curly", "hysterical", "thirsty", "attraction", "neighborly",
             "experience", "mellow", "knife", "woebegone", "rambunctious", "provide",
             "fragile", "power", "flag", "government",
             "unruly", "skip", "mess", "bucket", "bird", "desire",
             "nod", "shiny", "spotty", "care", "basin", "coat", "cave", "robin",
             "slippery", "mushy", "hand", "stormy", "fill", "phone", "scale", "unequal",
             "tightfisted", "attend", "nice", "lavish", "cough", "black", "request",
             "embarrassed", "absent", "kick", "tomatoes", "imaginary", "shirt",
             "blood", "misty", "shelf", "sulky", "onerous", "resolute", "salty", "sweater",
             "owe", "boring", "adjoining", "lacking", "separate", "shoes", "thread",
             "ritzy", "apparel", "matter", "existence", "educated", "shocking",
             "rough", "food", "prefer")
class Words:
    def __init__(self, words, row, screen_width, screen_height):
        self.words = words
        self.x = screen_width
        self.y = (int((screen_height - 50) / 20) * row) + 50
        self.in_focus = False
        self.color = arcade.color.WHITE
        self.row = row

    def change_color(self):
        if self.in_focus:
            return arcade.color.BLACK
        else:
            return arcade.color.WHITE

    def draw(self):
        arcade.draw_text(self.words, self.x, self.y, self.change_color(), 15)

    # decrease/remove a word 1 by 1 per 1 key pressed.
    def encounter(self):
        self.words = self.words[1:]

