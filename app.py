from flask import Flask, render_template, request
from wumpus import HuntTheWumpus
from NumberGuessingGame import NumberGuessingGame

wumpus_game = HuntTheWumpus()
guessing_game = NumberGuessingGame()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wumpus', methods=['POST', 'GET'])
def wumpus():
    if request.method == 'POST':
        message = wumpus_game.play(request.form)
    else:
        message = wumpus_game.new_game()
    return render_template('wumpus.html', message=message, game=wumpus_game)

@app.route('/guess', methods=['POST', 'GET'])
def guess():
    if request.method == 'POST':
        message = guessing_game.play_turn(request.form)
    else:
        message = guessing_game.new_game()
    return render_template('NumberGuessingGame.html', message=message, game=guessing_game)

if __name__ == "__main__":
    app.run()