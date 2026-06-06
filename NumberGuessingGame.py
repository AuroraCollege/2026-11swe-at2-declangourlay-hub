import random

class Game:
    def __init__(self):
        self.game_on = True

    def play_turn(self, form):
        raise NotImplementedError("Subclasses must implement play_turn().")

class NumberGuessingGame(Game):
    def __init__(self):
        super().__init__()
        self.__target = None
        self.attempts = 0
        self.new_game()

    def set_target(self, value):
        if 1 <= value <= 50:
            self.__target = value
        else:
            raise ValueError("Target must be between 1 and 50.")

    def new_game(self):
        self.set_target(random.randint(1, 50))
        self.attempts = 0
        self.game_on = True
        return "New game started! Guess a number between 1 and 50."

    def guess(self, number):
        if not self.game_on:
            return "Game over! Start a new game."

        self.attempts += 1

        if number == self.__target:
            self.game_on = False
            return f"Correct! The number was {self.__target}. You guessed it in {self.attempts} attempts."
        elif number < self.__target:
            return "Too low! Try again."
        else:
            return "Too high! Try again."

    def play_turn(self, form):
        if form.get("number"):
            return self.guess(int(form["number"]))
        return "Please enter a number."
    
    
