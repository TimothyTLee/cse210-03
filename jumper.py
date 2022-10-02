# TODO: Implement the Seeker class as follows...
from operator import contains
import random

# 1) Add the class declaration. Use the following class comment.


class Jumper:

    """
    The responsibility of The Jumper is to draw the character with a parachute, eliminate parts of parachute.

    Attributes:
    location (int): The location of the Seeker (1-1000).
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
        self._secret = random.choices (self._secret_words)[0]

    def check_guess(self, letter) -> list[int]:
        if contains(self._secret, letter):
            return  [i for i, ltr in enumerate(self._secret) if ltr.lower() == letter.lower()]
        self.lives -= 1
        return []

    def reveal_secret(self):
        return self._secret



    

    
    
























#     def _draw_character(self):

#         self._draw_character(self, print)  # character line by line use loop
#         # frtom line of parachute intil the 5th line, then change the O head to an X head

#     def _character(self):

#         self._character = list[]  # declared __init__

#     def _remove_next_part(self):

#         self._remove_next_part(self, pop)

#         #self._location = random.randint(1, 1000)
#     """Constructs a new Seeker.

    
#         Args:
#         self (Seeker): An instance of Seeker.
#         """


# # 3) Create the get_location(self) method. Use the following method comment.
#     def get_location(self) -> int:
#         return self._location

#     """Gets the current location.
        
#         Returns:
#             number: The current location,
#     """

# # 4) Create the move_location(self, location) method. Use the following method comment.
#     def move_location(self, int) -> None:
#         self._location = int
#     """Moves to the given location.

#         Args:
#             self (Jumper): An instance of Jumper.
#             location (int): The given location.
#         """
