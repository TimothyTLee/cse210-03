from game.terminal_service import TerminalService


class Puzzle:
    """    
    The responsibility of the puzzle is to hold the words, select random words, process players guesses.

    Attributes:
        _location (int): The location of the hider (1-1000).
        _distance (List[int]): The distance from the seeker.
    """

    def __init__(self, answer_length):
        self._terminal_service = TerminalService()
        self._answer = ['_' for i in range(answer_length)]

    def reset(self, answer_length):
        self._answer = ['_' for i in range(answer_length)]
    
    def print_answer(self):
        printable_answer = ''
        for i in range(len(self._answer)):
            printable_answer += f"{self._answer[i]} "
        self._terminal_service.draw_answer(printable_answer)

    def update_answer (self,letter, letter_indices):
        if len (letter_indices) != 0:
            for i in letter_indices:
                self._answer[i] = letter
            self._terminal_service.write_text(f"There were {len(letter_indices)} {letter}'s")
        else:
            self._terminal_service.write_text(f"There are no {letter}'s")

    def check_complete(self):
        return '_' not in self._answer




        
        """Constructs a new Hider.

        Args:
            self (Puzzle): An instance of Puzzle.
        """
    #     self._words = []
    #     self._random_word = string()
    #     # underscore to match number of letters, changes to letters on correct guesses.
    #     self._puzzle_letters = string()
    #     self._rand_word(self)
    #     self._create_list_words(self)  # optional if defined in __init__(self)
    #     # check for correct letter guess, re-write underscore word
    #     self._check_guess(self, player_guess)
    #     # check to see if player has solved the puzzle.
    #     self._puzzzle_solved(self)

    #     #self._location = random.randint(1, 1000)
    #     # self._distance = [0, 0] # start with two so get_hint always works

    # # def get_hint(self):
    #     """Gets a hint for the seeker.

    #     Args:
    #         self (Puzzle): An instance of Puzzle.
        
    #     Returns:
    #         string: A hint for the seeker.
    #     """
    #     #hint = "(-.-) Nap time."
    #     # if self._distance[-1] == 0:
    #     #    hint = "(;.;) You found me!"
    #     # elif self._distance[-1] > self._distance[-2]:
    #     #    hint = "(^.^) Getting colder! "
    #     # elif self._distance[-1] < self._distance[-2]:
    #     #    hint = "(>.<) Getting warmer!"
    #     # return hint

    # def is_found(self):
    #     """Whether or not the hider has been found.

    #     Args:
    #         self (Hider): An instance of Hider.

    #     Returns:
    #         boolean: True if the hider was found; false if otherwise.
    #     """
    #     return (self._distance[-1] == 0)

    # def watch_puzzle(self, seeker):
    #     """Watches the seeker by keeping track of how far away it is.

    #     Args:
    #         self (Hider): An instance of Hider.
    #     """
    #     #distance = abs(self._location - seeker.get_location())
    #     # self._distance.append(distance)
