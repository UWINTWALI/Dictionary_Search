# Dictionary Search Project

This project is a Python-based dictionary program that allows users to search for word definitions from a JSON data source. The program includes features such as case-insensitive search, suggestions for misspelled words, and handling multiple definitions.

## Features

- **Search for Word Definitions:** Enter any word, and the program will return its definition.
- **Case Insensitivity:** Supports words entered in any case (e.g., `RAIN`, `rain`, `RaIn`).
- **Misspelling Suggestions:** If a word is not found, the program suggests a close match using the `difflib` library.
- **Multiple Definitions:** For words with multiple meanings, all definitions are displayed in a clean format.


## Installation

Clone this repository or download the project files.


## How to Run

1. Download or create a JSON file named `dictionary.json` in the same directory as the script. The JSON file should contain word definitions in the format:

    ```json
    {
      "rain": ["Water that falls from the sky in droplets."],
      "hello": ["Expression of greeting used by two or more people who meet each other."]
    }
    ```

2. Run the Python script:

    ```bash
    python dictionary_search.py
    ```

3. Enter a word to search for its definition, or type `exit` to quit the program.

## Example Usage

```bash
Enter a word to search (or type 'exit' to leave): rainn
Did you mean 'rain'? (y/n): y

Definition:
Water that falls from the sky in droplets.

Enter a word to search (or type 'exit' to leave): exit
