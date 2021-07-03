import pytest

from homework2.task1 import *


def test_work_longest_diverse_words_func():
    assert get_longest_diverse_words("homework2/data.txt", encoding="unicode-escape")


def test_work_rarest_char_func():
    assert get_rarest_char("homework2/data.txt", encoding="unicode-escape")


def test_work_count_punctuation_chars_func():
    assert count_punctuation_chars("homework2/data.txt", encoding="unicode-escape")


def test_work_count_non_ascii_chars():
    assert count_non_ascii_chars("homework2/data.txt", encoding="unicode-escape")


def test_work_most_common_non_ascii_char():
    assert get_most_common_non_ascii_char(
        "homework2/data.txt", encoding="unicode-escape"
    )
