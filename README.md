[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Mastermind

This game looks best on a dark terminal background, but should work on lighter ones with minimum modification.

### How to run the game:
* Clone the repo
* `cd mastermind`
* `python3.9 -m venv ./venv`
* `source venv/bin/activate`
* `pip install -r requirements/base.txt`
* `python mastermind.py`

### How to run the tests:
* `source venv/bin/activate`
* `pip install -r requirements/dev.txt`
* `pytest .`

### Rules of mastermind:
* You'll be asked how long of a sequence to generate.
  * The standard game is 4.
* You'll be asked how many guesses you should be allowed.
  * The standard game is 10.
* Your goal is to guess the sequence in that number of guesses.
* The game will ask you for your color sequence one at a time.
* It will ask you to confirm your guess before scoring it.

### Scoring:
* A green peg means you have the correct color in the correct position.
* A yellow peg means you have the correct color in the wrong position.
* The scoring pegs are sorted. They don't correlate to the position of your colors.

    #### Examples:
    In a 4 sequence game:
    * 4 yellow pegs means you have all the colors, but in the wrong positions.
    * 2 green and 2 yellow pegs means you have all the colors right, but two are in the wrong position.
