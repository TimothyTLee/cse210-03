from terminal_service import TerminalService


class Puzzle:
    """    
    The responsibility of the puzzle is to hold the words, select random words, process players guesses.

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

    def update_answer(self, letter, letter_indices):
        if len(letter_indices) != 0:
            for i in letter_indices:
                self._answer[i] = letter
            self._terminal_service.write_text(
                f"There were {len(letter_indices)} {letter}'s")
        else:
            self._terminal_service.write_text(f"There are no {letter}'s")

    def check_complete(self):
        return '_' not in self._answer
