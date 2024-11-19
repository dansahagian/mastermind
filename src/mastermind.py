import random


class Mastermind:
    def __init__(self):
        self.guesses: list = []
        self.scores: list = []
        self.secret_map: dict = {
            "w": "⚪️",
            "b": "🔵",
            "p": "🟣",
            "y": "🟡",
            "r": "🔴",
            "g": "🟢",
        }
        self.scoring_map: dict = {
            "bp": "✅",
            "wp": "⚠️",
        }

        self.secret_code_length: int = 0
        self.max_guesses: int = 0
        self.secret_code: list = []

        self.show_preamble = True

    def _create_secret_code(self) -> None:
        self.secret_code = [
            random.choice(list(self.secret_map.keys()))
            for _ in range(0, self.secret_code_length)
        ]

    def _get_user_guess(self) -> None:
        guess = [self._enter_color() for _ in range(0, self.secret_code_length)]
        confirm = input(f"\nConfirm guess of {self._display_guess(guess)} (y or n): ")
        if confirm == "y":
            return self.guesses.append(guess)

        print("\nPlease reenter your sequence.\n")
        return self._get_user_guess()

    def _score_last_guess(self) -> None:
        ans: list = self.secret_code.copy()
        ges: list = self.guesses[-1].copy()

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

        return self.scores.append(sorted(score))

    def _get_user_input(self, question: str) -> int:
        number = input(f"\n{question}")
        try:
            return int(number)
        except ValueError:
            print(f"{number} is not valid. Please input an integer.")
            return self._get_user_input(question)

    def _enter_color(self) -> str:
        colors = "  ".join([f"{self.secret_map[k]} {k}" for k in self.secret_map])
        color = input(f"Enter a color {colors}: ")
        if color not in self.secret_map:
            print(f"{color} is not a valid color!")
            return self._enter_color()
        return color

    def _display_guess(self, guess: list) -> str:
        return " ".join([self.secret_map[x] for x in guess])

    def _display_score(self, score: list) -> str:
        return " ".join([self.scoring_map[x] for x in score])

    def _is_winner(self) -> bool:
        return self.scores[-1] == ["bp"] * self.secret_code_length

    @staticmethod
    def _print_star_wrap(message: str, n: int = 30) -> None:
        stars = "*" * n
        print(f"\n\n{stars}\n\n{message}\n\n{stars}\n\n")

    def play(self) -> None:
        if self.show_preamble:
            readme = "https://github.com/dansahagian/mastermind/blob/main/README.md"
            message = f"If you've never played mastermind, you can read about it at:\n{readme}"
            self._print_star_wrap(message)

        self.secret_code_length = self._get_user_input(
            "How long should the secret code be? "
        )
        self.max_guesses = self._get_user_input("How many guesses should you get? ")
        self._create_secret_code()

        while len(self.guesses) < self.max_guesses:
            self._get_user_guess()
            self._score_last_guess()

            if self._is_winner():
                n = len(self.guesses)
                t = "guesses" if n > 1 else "guess"
                self._print_star_wrap(f"Congratulations! You won in {n} {t}!")
                return

            print()
            for i, guess in enumerate(self.guesses):
                guess_output = self._display_guess(guess)
                score_output = self._display_score(self.scores[i])
                spaces = " " * (self.secret_code_length - len(self.scores[i]))
                row = f"Guess {i + 1:02} / {self.max_guesses:02}:"
                print(f"{row} {guess_output}  Score: {score_output}{spaces}")
            print()

        self._print_star_wrap(
            f"You Lost! Sequence: {self._display_guess(self.secret_code)}"
        )


if __name__ == "__main__":
    mm = Mastermind()
    mm.play()
