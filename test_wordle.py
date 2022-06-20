from wordle import *
import pytest
from unittest.mock import patch

def test_random_word():
    word = random_word()
    assert isinstance(word, str)

@patch("wordle.WORD_LIST", "crane")
def test_check_input():
    assert check_input("crane") == True

def test_check_input_invalid():
    with pytest.raises(TypeError):
        check_input(420.69)
    with pytest.raises(ValueError):
        check_input("four")

def test_check_position():
    position_list = check_position("crane", "crane")
    assert position_list == [True, True, True, True, True]
    position_list = check_position("crane", "brain")
    assert position_list == [False, True, True, False, False]

def test_check_position_invalid():
    with pytest.raises(TypeError):
        check_position(420, 69)

def test_check_letter():
    letter_list = check_letter("crane", "crane")
    assert letter_list == [True, True, True, True, True]
    letter_list = check_letter("crane", "penis")
    assert letter_list == [False, True, True, False, False]

