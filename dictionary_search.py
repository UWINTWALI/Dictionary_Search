import json
import difflib

# Load the dictionary data from the JSON file
with open('dictionary.json', 'r') as file:
    data = json.load(file)

# Function to get the definition of a word
def get_definition(word):
    word = word.lower()  # Normalize word to lower case for case insensitivity
    if word in data:
        definition = data[word]
        if isinstance(definition, list):
            return "\n".join(definition)  # Join list elements if definition is a list
        else:
            return definition
    else:
        # Suggest a closer match if the word is not found
        suggestion = difflib.get_close_matches(word, data.keys(), n=1)
        if suggestion:
            user_response = input(f"Did you mean '{suggestion[0]}'? (y/n): ").strip().lower()
            if user_response == 'y':
                definition = data[suggestion[0]]
                if isinstance(definition, list):
                    return "\n".join(definition)  # Join if it's a list
                else:
                    return definition
            else:
                return "No word found."
        else:
            return "No such word found and no close matches."

# Function to run the dictionary program in a loop
def run_dictionary():
    while True:
        word = input("Enter a word to search (or type 'exit' to leave): ").strip()
        if word.lower() == "exit":
            break
        definition = get_definition(word)
        print(f"\nDefinition:\n{definition}\n")

# Run the dictionary program
run_dictionary()
