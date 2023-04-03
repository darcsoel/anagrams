# pylint:disable=missing-function-docstring, invalid-name
"""
Unit tests
"""

from main import fact, list_position, word_combination


def test_fact_1() -> None:
    assert fact(1) == 1


def test_fact_2() -> None:
    assert fact(2) == 2


def test_fact_5() -> None:
    assert fact(5) == 120


def test_ABAB() -> None:
    assert word_combination("ABAB") == 6
    assert list_position("ABAB") == 2


def test_AAAB() -> None:
    assert list_position("AAAB") == 1


def test_QUESTION() -> None:
    assert list_position("QUESTION") == 24572


def test_BOOKKEEPER() -> None:
    assert list_position("BOOKKEEPER") == 10743
