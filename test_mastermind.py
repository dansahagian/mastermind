from mastermind import (
    create_sequence,
    is_game_over
)


def test_sequence_length():
    assert len(create_sequence()) == 4


def test_is_game_over_1st_guess():
    assert is_game_over(1, []) is False


def test_is_game_over_11th_guess():
    assert is_game_over(11, []) is True


def test_is_game_over_win():
    assert is_game_over(5, ["bb", "bb", "bb", "bb"]) is True