[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Mastermind

### How to run the game:
* `pipenv install`
* `pipenv run python mastermind.py`


### Rules of mastermind:
* A sequence of 4 colors will be generated
* Your goal is to guess the sequence in 10 guesses or less
* The game will ask you for 4 colors per guess
* It will ask you to confirm your guess before scoring it

### Scoring:
* A green peg means you have the correct color in the correct position
* A white peg means you have the correct color in the wrong position
* Green and white scoring pegs are sorted. They don't correlate to the position of your colors.

    #### Examples:
    * 4 white pegs means you have all the colors, but in the wrong positions
    * 2 green and 2 white pegs means you have all the colors right, but two are in the wrong position
