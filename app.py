import os
import json
import random 
import time
from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = b"wX=a+`#3fK^;CjU~8(:JL'"

@app.route("/", methods=["GET", "POST"])
def wordle():
    print(WORDLE_DATA)
    if request.method == "POST":
        input: str = request.form["wordle_input"].strip()
        if input in WORDLE_DATA:
            entered_data.append(input) if input not in entered_data else None
            if input == current_chosen_character:
                print(f"{current_chosen_character} was guessed correctly!")
    return render_template("andor_wordle.html", WORDLE_DATA=WORDLE_DATA, entered_data=entered_data)

def choose_random_character() -> str:
    '''Chooses a random character from the wordle data and returns it.'''
    return random.choice(list(WORDLE_DATA.keys()))

if __name__ == "__main__":
    
    # Load wordle data
    json_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "andor_wordle", "andor_wordle_data.json")
    with open(json_data_path, "r", encoding="utf-8") as data: 
        WORDLE_DATA: dict = json.load(data)

        # Format data, converts the list of episodes into booleans
        for key, value in WORDLE_DATA.items():
            if not isinstance(value[-1], list):
                continue
            temporary_list = []
            temporary_list: list = value.pop()
            for episode in range(1, 13):
                value.append(episode in temporary_list)
            entered_data: list = []
    
    # Choose random character 
    current_chosen_character: str = choose_random_character()
    
    # Run app
    app.run(debug=True)