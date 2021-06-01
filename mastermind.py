#!/opt/mastermind/venv/bin/python

import random

import colorama
from termcolor import colored

colorama.init()

BIG_DOT = "\u2B24"
LIL_DOT = "\u25CF"

W = colored(BIG_DOT, "white")
B = colored(BIG_DOT, "blue")
P = colored(BIG_DOT, "magenta")
Y = colored(BIG_DOT, "yellow")
R = colored(BIG_DOT, "red")
G = colored(BIG_DOT, "green")

BP = colored(LIL_DOT, "green")
WP = colored(LIL_DOT, "yellow")

COLOR_MAP = {"w": W, "b": B, "p": P, "y": Y, "r": R, "g": G, "bp": BP, "wp": WP}


def display_dots(sequence: list) -> str:
    return " ".join([COLOR_MAP[x] for x in sequence])


def create_sequence(sequence_length: int) -> list:
    choices = ["w", "b", "p", "y", "r", "g"]
    return [random.choice(choices) for _ in range(0, sequence_length)]


def enter_color() -> str:
    color = input(f"Enter a color {W} w  {B} b  {P} p  {Y} y  {R} r  {G} g: ")
    if color not in COLOR_MAP:
        print(f"{color} is not a valid color!")
        return enter_color()
    return color


def guess_sequence(sequence_length: int) -> list:
    guess = [enter_color() for _ in range(0, sequence_length)]
    confirm = input(f"\nConfirm guess of {display_dots(guess)} (y or n): ")
    if confirm == "y":
        return guess

    print(f"\nPlease reenter your sequence.\n")
    return guess_sequence()


def score_guess(guess: list, answer: list) -> list:
    ans = answer.copy()
    ges = guess.copy()

    score = []
    for i, color in enumerate(ges):
        if color == ans[i]:
            score.append("bp")
            ans[i] = "*"
            ges[i] = "-"

    for i, color in enumerate(ges):
        if color in ans:
            score.append("wp")
            ans[ans.index(color)] = "*"
            ges[i] = "-"

    return sorted(score)


def is_winner(score: list, sequence_length: int) -> bool:
    if score == ["bp"] * sequence_length:
        return True
    return False


def get_user_input(question: str) -> int:
    number = input(f"\n{question}")
    try:
        return int(number)
    except ValueError:
        print(f"{number} is not valid. Please input an integer.")


def print_star_wrap(message: str, color: str, n: int = 30):
    stars = colored("*" * n, color)
    print(f"\n\n{stars}\n\n{message}\n\n{stars}\n\n")


def main(preamble=True):
    if preamble:
        readme = "https://github.com/dansahagian/mastermind/blob/main/README.md"
        message = f"If you've never played mastermind, you can read about it at {readme}"
        print_star_wrap(message, "white")

    sequence_length = get_user_input("How long should the sequence be? ")
    number_of_guesses = get_user_input("How many guesses should you get? ")
    print()

    answer = create_sequence(sequence_length)
    guesses = []
    scores = []

    for i in range(1, number_of_guesses + 1):
        guess = guess_sequence(sequence_length)
        score = score_guess(guess, answer)

        guesses.append(guess)
        scores.append(score)

        if is_winner(score, sequence_length):
            text = "guesses" if i > 1 else "guess"
            print_star_wrap(f"You Won in {i} {text}!", "green")
            return True

        print()
        for j, guess in enumerate(guesses):
            guess_output = display_dots(guess)
            score_output = display_dots(scores[j])
            spaces = " " * (10 - len(scores[j]))
            print(f"{j+1:02}: {guess_output}  Score: {score_output}{spaces}")
        print()

    print_star_wrap(f"You Lost! Sequence: {display_dots(answer)}", "red")
    print()

    play_again = input("Would you like to play again (y/n)")
    if str(play_again.strip()) == "y":
        return main(preamble=False)

    return


if __name__ == "__main__":
    main()
