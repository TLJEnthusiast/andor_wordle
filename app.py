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
            
            if input == current_chosen_character:
                print(f"{current_chosen_character} was guessed correctly!")
    return render_template("andor_wordle.html", WORDLE_DATA=WORDLE_DATA, entered_data=entered_data)

def choose_random_character():
    '''Chooses a random character from the wordle data and returns it.'''
    return random.choice(list(WORDLE_DATA.keys()))

if __name__ == "__main__":
    
    # Load wordle data
    json_data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "andor_wordle", "andor_wordle_data.json")
    with open(json_data_path, "r", encoding="utf-8") as data: 
        WORDLE_DATA: dict = json.load(data)
    entered_data: dict = {}
    
    # Choose random character 
    current_chosen_character = choose_random_character()
        
    app.run(debug=True)