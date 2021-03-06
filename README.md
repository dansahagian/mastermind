[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Mastermind

This game looks best on a dark terminal background, but should work on lighter ones with minimum modification.

### How to run the game:
* `pipenv install`
* `pipenv run python mastermind.py`

### Rules of mastermind:
* You will be asked for a sequence length and how many guesses
* The standard board game uses a 4 color sequence and 10 guesses
* Your goal is to guess the computer generated sequence before you run out of guesses
* It will ask you to confirm your guess before scoring it

### Scoring:
* A green peg means you have the correct color in the correct position
* A yellow peg means you have the correct color in the wrong position
* Green and yellow scoring pegs are sorted. They don't correlate to the position of your colors.

    #### Examples:
    * 4 yellow pegs means you have all the colors, but in the wrong positions
    * 2 green and 2 yellow pegs means you have all the colors right, but two are in the wrong position
