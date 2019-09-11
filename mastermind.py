import random

from sty import bg, fg

BIG_DOT = "\u2B24"
LIL_DOT = "\u25CF"

WHITE = fg(255, 255, 255)
BLUE = fg(86, 180, 223)
PURPLE = fg(204, 121, 167)
YELLOW = fg(240, 228, 66)
RED = fg(213, 94, 0)
GREEN = fg(0, 158, 115)

W = f"{WHITE}{BIG_DOT}{WHITE}"
B = f"{fg(86, 180, 223)}{BIG_DOT}{WHITE}"
P = f"{fg(204, 121, 167)}{BIG_DOT}{WHITE}"
Y = f"{fg(240, 228, 66)}{BIG_DOT}{WHITE}"
R = f"{fg(213, 94, 0)}{BIG_DOT}{WHITE}"
G = f"{fg(0, 158, 115)}{BIG_DOT}{WHITE}"

CP = f"{GREEN}{LIL_DOT}{WHITE}"
WP = f"{WHITE}{LIL_DOT}{WHITE}"

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
    answer = create_sequence()

    print(f"{bg(0, 0, 0)}{fg(255, 255, 255)}")

    guesses = []
    scores = []

    for i in range(1, 11):
        guess = guess_sequence()
        score = score_guess(guess, answer)

        guesses.append(guess)
        scores.append(score)

        if winner(score):
            text = "guesses" if i > 1 else "guess"
            print(f"You Won in {i} {text}! Sequence: {display_dots(answer)}\n")
            return True

        for j, guess in enumerate(guesses):
            guess_output = display_dots(guess)
            score_output = display_dots(scores[j])
            print(f"{j+1:02}: {guess_output}  Score: {score_output}")
        print()

    print(f"You Lost! Sequence: {display_dots(answer)}\n")
    print()


if __name__ == "__main__":
    main()
