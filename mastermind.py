import random

from termcolor import colored

BIG_DOT = "\u2B24"
LIL_DOT = "\u25CF"

W = colored(BIG_DOT, "white")
B = colored(BIG_DOT, "blue")
P = colored(BIG_DOT, "magenta")
Y = colored(BIG_DOT, "yellow")
R = colored(BIG_DOT, "red")
G = colored(BIG_DOT, "green")

CP = colored(LIL_DOT, "grey")
WP = colored(LIL_DOT, "white")

COLOR_MAP = {"w": W, "b": B, "p": P, "y": Y, "r": R, "g": G, "cp": CP, "wp": WP}


def display_dots(sequence: list) -> str:
    return " ".join([COLOR_MAP[x] for x in sequence])


def create_sequence() -> list:
    choices = ["w", "b", "p", "y", "r", "g"]
    return [random.choice(choices) for _ in range(0, 4)]


def enter_color() -> str:
    color = input(f"Enter a color {W} w  {B} b  {P} p  {Y} y  {R} r  {G} g: ")
    if color not in COLOR_MAP:
        print(f"{color} is not a valid color!")
        return enter_color()
    return color


def guess_sequence() -> list:
    guess = [enter_color() for _ in range(0, 4)]
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
            score.append("cp")
            ans[i] = "*"
            ges[i] = "-"

    for i, color in enumerate(ges):
        if color in ans:
            score.append("wp")
            ans[ans.index(color)] = "*"
            ges[i] = "-"

    return sorted(score)


def winner(score: list) -> bool:
    if score == ["cp", "cp", "cp", "cp"]:
        return True
    return False


def main():
    print()
    answer = create_sequence()
    guesses = []
    scores = []

    for i in range(1, 11):
        guess = guess_sequence()
        score = score_guess(guess, answer)

        guesses.append(guess)
        scores.append(score)

        if winner(score):
            text = "guesses" if i > 1 else "guess"
            print(f"You Won in {i} {text}! Sequence: {display_dots(answer)}  ")
            print()
            return True

        for j, guess in enumerate(guesses):
            guess_output = display_dots(guess)
            score_output = display_dots(scores[j])
            spaces = " " * (10 - len(scores[j]))
            print(f"{j+1:02}: {guess_output}  Score: {score_output}{spaces}")
        print()

    print(f"You Lost! Sequence: {display_dots(answer)}\n")
    print()


if __name__ == "__main__":
    main()
