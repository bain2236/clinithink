
import pytest
from anagram_solver import anagram_solver

@pytest.mark.parametrize("words", 
[
    ["the", "quick", "brown", "fox"],
    ["do", "or", "door"],
])
def test_no_anagram(words):
    anagrams = anagram_solver(words)
    print('anagramts {0}'.format(anagrams))
    assert len(anagrams) == 0



@pytest.mark.parametrize("words, anagrams",[
    (["eat", "tea"],["eat", "tea"]),
    (["pots", "stop", "pots", "spot", "stop"],["pots", "stop", "spot"])
    ])
def test_anagram(words, anagrams):
    anagrams = anagram_solver(words)
    assert anagrams == anagrams


# 