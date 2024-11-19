import pytest

from mastermind import Mastermind


class TestMastermind(object):
    @pytest.fixture
    def secret_code(self):
        return ["b", "r", "p", "b"]

    @pytest.mark.parametrize(
        "guess,expected_score",
        [
            (["b", "w", "w", "w"], ["bp"]),
            (["b", "b", "b", "b"], ["bp", "bp"]),
            (["b", "r", "p", "w"], ["bp", "bp", "bp"]),
            (["b", "r", "p", "b"], ["bp", "bp", "bp", "bp"]),
            (["w", "b", "w", "w"], ["wp"]),
            (["w", "b", "r", "w"], ["wp", "wp"]),
            (["w", "b", "r", "p"], ["wp", "wp", "wp"]),
            (["r", "b", "b", "p"], ["wp", "wp", "wp", "wp"]),
            (["b", "p", "r", "b"], ["bp", "bp", "wp", "wp"]),
        ],
    )
    def test_score_guess(self, secret_code, guess, expected_score):
        mm = Mastermind()
        mm.secret_code = secret_code

        mm.guesses.append(guess)
        mm._score_last_guess()

        assert mm.scores[-1] == expected_score
