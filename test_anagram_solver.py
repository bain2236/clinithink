
import pytest
from anagram_solver import anagram_solver

@pytest.mark.parametrize("words, expected",[
    (["the", "quick", "brown", "fox"],[]),
    (["do", "or", "door"],[])
    ])
def test_no_anagram(words, expected):
    anagrams = anagram_solver(words)
    assert all([a == b for a, b in zip(anagrams, expected)])

# can't get this to work as there's an issue with ordering the anagrams
# this is possibly caused by the way itertools.permutations work
@pytest.mark.parametrize("words, expected",[
    (["eat", "tea"],["eat", "tea"]),
    (["pots", "stop", "pots", "spot", "stop"],["spot", "pots", "stop"])
    ])
def test_anagram(words, expected):
    anagrams = anagram_solver(words)
    console.log()
    assert all([a == b for a, b in zip(anagrams, expected)])
