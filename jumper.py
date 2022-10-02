# TODO: Implement the Seeker class as follows...
from operator import contains
import random

# 1) Add the class declaration. Use the following class comment.


class Jumper:

    """
    The responsibility of The Jumper is to draw the character with a parachute, eliminate parts of parachute.
    loses parachute pieces on wrong guesses.


    """
    _inital_lives = 5
    _secret_words = [
        "Python",
        "airplane",
        "church",
        "military",
    ]


# 2) Create the class constructor. Use the following method comment.


    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._set_secret()
        self.lives = self._inital_lives
        self.secret_length = len(self._secret)

    def _set_secret(self) -> None:
        self._secret = random.choices(self._secret_words)[0]

    def check_guess(self, letter) -> list[int]:
        if contains(self._secret, letter):
            return [i for i, ltr in enumerate(self._secret) if ltr.lower() == letter.lower()]
        self.lives -= 1
        return []

    def reveal_secret(self):
        return self._secret
