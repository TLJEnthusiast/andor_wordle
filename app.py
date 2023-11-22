import os
import json
import random 
import time
from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = b"wX=a+`#3fK^;CjU~8(:JL'"

@app.route("/", methods=["GET", "POST"])
def wordle():
    if request.method == "POST":
        input: str = request.form["wordle_input"].strip()
        if input in WORDLE_DATA:
            entered_data.append(input) if input not in entered_data else None
            if input == current_chosen_character:
                print(f"{current_chosen_character} was guessed correctly!")
    return render_template("andor_wordle.html", WORDLE_DATA=WORDLE_DATA, entered_data=entered_data, current_chosen_character=current_chosen_character)


def choose_random_character() -> str:
    '''Chooses a random character from the wordle data and returns it. Additionally, it formats the WORDLE_DATA to include a boolean for every entry whether or not it's the same as corresponding value for the chosen character.'''
    global WORDLE_DATA
    choice = random.choice(list(WORDLE_DATA.keys())[1::])

    #format 
    result_dict = {}
    for character, char_list in WORDLE_DATA.items():
        # Compare each element in the lists and create a new list
        new_list = [(value, value == correct_value) for value, correct_value in zip(char_list, WORDLE_DATA[choice])]
        result_dict[character] = new_list
    WORDLE_DATA = result_dict
    
    return choice 


if __name__ == "__main__":
    
    # Load wordle data
    json_data_path: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "andor_wordle", "andor_wordle_data.json")
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