from collections import Counter
from functools import lru_cache, reduce


@lru_cache(typed=True)
def fact(number: int) -> int:
    """Factorial function

    Args:
        number (int): number of fact

    Returns:
        _type_: result factorial
    """

    if number in (0, 1):
        return 1

    return fact(number - 1) * number


def word_combination(word: str) -> int:
    """
    Full anagrams, not depends on alphabetical position

    Args:
        word (str): random word

    Returns:
        int: combination count
    """

    total_combination = fact(len(word))
    chars_counter = Counter(word)
    chars_combinaion = reduce(lambda x, y: x * y, (fact(v) for v in chars_counter.values()))

    return int(total_combination // chars_combinaion)


def list_position(word: str) -> int:
    """
    Return the anagram list position of the word

    """

    combination = 1

    for index_outer, start in enumerate(word):
        loop_cache: set[str] = set()

        for index_inner in range(index_outer + 1, len(word)):
            end = word[index_inner]

            if start > end and end not in loop_cache:
                combination += word_combination(word[index_outer:index_inner] + word[index_inner + 1 :])
                loop_cache.update(end)

    return combination
