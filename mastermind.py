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

BB = colored(LIL_DOT, "grey")
WW = colored(LIL_DOT, "white")

COLOR_MAP = {"w": W, "b": B, "p": P, "y": Y, "r": R, "g": G, "bb": BB, "ww": WW}


def display_dots(sequence: list) -> str:
    return " ".join([COLOR_MAP[x] for x in sequence])


def create_sequence() -> list:
    choices = ["w", "b", "p", "y", "r", "g"]
    return [random.choice(choices) for _ in range(0, 4)]


def enter_color() -> str:
    color = input(f"Enter a color ({W} w  {B} b  {P} p  {Y} y  {R} r  {G} g): ")
    if color not in COLOR_MAP:
        print(f"{color} is not a valid color!")
        return enter_color()
    return color


def guess_sequence() -> list:
    guess = [enter_color() for _ in range(0, 4)]
    confirm = input("\nConfirm guess of {} (y or n): ".format(display_dots(guess)))

    if confirm == "y":
        return guess

    print("\nPlease reenter your sequence.\n")
    return guess_sequence()


def score_guess(guess: list, answer: list) -> list:
    ans = answer.copy()
    ges = guess.copy()

    score = []
    for i, color in enumerate(ges):
        if color == ans[i]:
            score.append("bb")
            ans[i] = "*"
            ges[i] = "-"

    for i, color in enumerate(ges):
        if color in ans:
            score.append("ww")
            ans[ans.index(color)] = "*"
            ges[i] = "-"

    return sorted(score)


def winner(score: list) -> bool:
    if score == ["bb", "bb", "bb", "bb"]:
        return True
    return False


def main():
    answer = create_sequence()
    print()

    guesses = []
    scores = []

    for i in range(1, 11):
        guess = guess_sequence()
        score = score_guess(guess, answer)

        guesses.append(guess)
        scores.append(score)

        if winner(score):
            text = "guesses" if i > 1 else "guess"
            print(f"You Won in {i} {text}! The sequence was {display_dots(answer)}\n")
            return True

        for j, guess in enumerate(guesses):
            guess_output = display_dots(guess)
            score_output = display_dots(scores[j])
            print(f"{j+1:02}: {guess_output} - Score: {score_output}")
        print()

    print(f"You Lost! The sequence was {display_dots(answer)}\n")


if __name__ == "__main__":
    main()
