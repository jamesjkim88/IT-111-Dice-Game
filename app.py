from flask import Flask, render_template, request
from games.dice_game import DiceGame
import random

app = Flask(__name__)

game = DiceGame()


@app.route("/", methods=["GET", "POST"])
def index():
    message = ""

    if request.method == "POST":

        if "new_game" in request.form:
            game.start_new_game()
            message = "Game started"

        elif "roll_manual" in request.form:
            roll_value = request.form.get("roll_value")
            message = game.play_turn(roll_value)

        elif "roll_random" in request.form:
            roll_value = random.randint(2, 12)
            message = game.play_turn(roll_value)

    return render_template(
        "dice.html",
        message=message,
        turn=game.turn,
        point=game.point,
        finished=game.finished
    )


if __name__ == "__main__":
    app.run(debug=True)
