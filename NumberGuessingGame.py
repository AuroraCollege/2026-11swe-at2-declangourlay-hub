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

