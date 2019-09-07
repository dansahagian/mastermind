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

COLOR_MAP = {"w": W, "b": B, "p": P, "y": Y, "r": R, "g": G}
SCORE_MAP = {"bb": BB, "ww": WW}


def create_sequence():
    return [random.choice(list(COLOR_MAP.keys())) for _ in range(0, 4)]


def enter_color():
    color = input(f"Enter a color ({W} w  {B} b  {P} p  {Y} y  {R} r  {G} g): ")
    if color not in COLOR_MAP:
        print("{} is not a valid color!".format(color))
        return enter_color()

    return color


def display_guess(guess):
    return " ".join([COLOR_MAP[x] for x in guess])


def display_score(score):
    return " ".join([SCORE_MAP[x] for x in score])


def guess_sequence():
    guess = [enter_color() for _ in range(0, 4)]
    confirm = input("\nConfirm guess of {} (y or n): ".format(display_guess(guess)))

    if confirm == "y":
        return guess

    print("\nPlease reenter your sequence.\n")
    return guess_sequence()


def score_guess(guess, answer):
    ans = list(answer)
    ges = list(guess)

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


def is_game_over(guess_num, score):
    if score == ["bb", "bb", "bb", "bb"]:
        print("You won!")
        return True

    if guess_num > 10:
        print("You used all your turns. You lose!")
        return True

    return False


def main():
    answer = create_sequence()
    print()

    guesses = []
    scores = []

    i = 1
    score = ["", "", "", ""]

    while not is_game_over(i, score):
        guess = guess_sequence()
        guesses.append(guess)

        score = score_guess(guess, answer)
        scores.append(score)

        for j, guess in enumerate(guesses):
            print(
                f"{j+1:02}: {display_guess(guess)} - Score: {display_score(scores[j])}"
            )
        print()

        i += 1

    print(f"The sequence was {display_guess(answer)}\n")


if __name__ == "__main__":
    main()
