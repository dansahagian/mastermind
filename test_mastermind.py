import pytest

from mastermind import create_sequence, score_guess, winner


class TestMastermind(object):
    @pytest.fixture
    def answer(self):
        return ["b", "r", "p", "b"]

    def test_sequence_length(self):
        assert len(create_sequence()) == 4

    @pytest.mark.parametrize(
        "guess,expected",
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
        ]
    )
    def test_score_guess(self, answer, guess, expected):
        assert score_guess(guess, answer) == expected
