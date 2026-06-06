class Game:
    def __init__(self):
        self.game_on = True

    def play_turn(self, form):
        raise NotImplementedError("Subclasses must implement play_turn().")
