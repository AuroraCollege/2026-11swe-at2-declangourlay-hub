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