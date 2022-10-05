from terminal_service import TerminalService
from puzzle import Puzzle
from jumper import Jumper


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        draw jumper character, put in puzzle, check if player is still able to play (win/lose), prompt player for letter guess.
        is_playing (boolean): Whether or not to keep playing.
        jumper(Jumper) : The game's scoring method
        puzzle(Puzzle) : The game's playing board
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        # self._puzzle = Puzzle()
        self._is_playing = True
        self._jumper = Jumper()
        self._puzzle = Puzzle(self._jumper.secret_length)
        self._terminal_service = TerminalService()

    def _reset(self):
        self._jumper.reset()
        self._puzzle.reset(self._jumper.secret_length)

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._show_puzzle()
            letter_guess = self._get_inputs()
            self._do_updates(letter_guess)
            self._check_win_loss()

    def _show_puzzle(self):
        self._terminal_service.draw_jumper(self._jumper.lives)
        self._puzzle.print_answer()

    def _get_inputs(self) -> int:
        """changes underscore to letter on correct guesses.

        Args:
            self (Director): An instance of Director.
        """
        return self._terminal_service.read_text(
            "\nEnter a letter: ")

    def _do_updates(self, letter_guess):
        """allows player to guess letters until they either win the game or lose.

        Args:
            self (Director): An instance of Director.
        """
        letter_indices = self._jumper.check_guess(letter_guess)
        self._puzzle.update_answer(letter_guess, letter_indices)

    def _new_game(self):
        self._is_playing = self._terminal_service.read_text(
            "do you want to play again? [y/n]") == 'y'
        if(self._is_playing):
            self._reset()

    def _check_win_loss(self):
        self._terminal_service.change_head(self._jumper.lives)

        if self._puzzle.check_complete() and self._jumper.lives > 0:
            self._terminal_service.write_text(
                "Way to go! You survived this jump")
            self._new_game()
        elif self._jumper.lives < 1:
            self._terminal_service.write_text(
                f"you're dead. The word was {self._jumper.reveal_secret()}")
            self._terminal_service.draw_jumper(self._jumper.lives)
            self._new_game()

        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        #hint = self._puzzle.get_hint()
        # self._terminal_service.write_text(hint)
        # if self._hider.is_found():
        #    self._is_playing = False
