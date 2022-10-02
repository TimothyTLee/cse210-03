class TerminalService:
    """A service that handles terminal operations.
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """
     
    def read_text(self, prompt):
        """Gets text input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    def read_number(self, prompt):
        """Gets numerical input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            float: The user's input as a number.
        """
        return float(input(prompt))
        
    def write_text(self, text):
        """Displays the given text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            text (string): The text to display.
        """
        print(text)

    def draw_jumper(self, lives):
        jumper_lives = [
            "  _",
            "/   \\",
            "-----",
            "\\   /",
            " \\ /", 
        ]

        starting_index = len(jumper_lives) - lives
        for i in range(starting_index, len(jumper_lives)):
            print(jumper_lives[i])
        
        jumper = [
            '  0',
            ' /|\\',
            ' / \\'
        ]

        for i in range(len(jumper)):
            print (jumper[i])

    def draw_answer(self, answer):
        print(answer)
 