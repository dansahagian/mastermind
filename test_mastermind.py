import pytest

from mastermind import create_sequence, score_guess, winner


class TestMastermind(object):
    @pytest.fixture
    def answer(self):
        return ["b", "r", "p", "b"]

    def test_sequence_length(self):
        assert len(create_sequence()) == 4

    def test_score_guess_one_match(self, answer):
        guess = ["b", "w", "w", "w"]
        assert score_guess(guess, answer) == ["cp"]

    def test_score_guess_two_match(self, answer):
        guess = ["b", "b", "b", "b"]
        assert score_guess(guess, answer) == ["cp", "cp"]

    def test_score_guess_three_match(self, answer):
        guess = ["b", "r", "p", "w"]
        assert score_guess(guess, answer) == ["cp", "cp", "cp"]

    def test_score_guess_four_match(self, answer):
        guess = ["b", "r", "p", "b"]
        assert score_guess(guess, answer) == ["cp", "cp", "cp", "cp"]

    def test_score_guess_one_color_correct(self, answer):
        guess = ["w", "b", "w", "w"]
        assert score_guess(guess, answer) == ["wp"]

    def test_score_guess_two_color_correct(self, answer):
        guess = ["w", "b", "r", "w"]
        assert score_guess(guess, answer) == ["wp", "wp"]

    def test_score_guess_three_color_correct(self, answer):
        guess = ["w", "b", "r", "p"]
        assert score_guess(guess, answer) == ["wp", "wp", "wp"]

    def test_score_guess_four_color_correct(self, answer):
        guess = ["r", "b", "b", "p"]
        assert score_guess(guess, answer) == ["wp", "wp", "wp", "wp"]

    def test_score_two_and_two(self, answer):
        guess = ["b", "p", "r", "b"]
        assert score_guess(guess, answer) == ["cp", "cp", "wp", "wp"]
