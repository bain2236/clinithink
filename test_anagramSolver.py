
import pytest
from anagramSolver import anagramSolver

@pytest.mark.parametrize("words", 
[
    ["the", "quick", "brown", "fox"],
    ["do", "or", "door"],
])
def test_no_anagram(words):
    anagrams = anagramSolver(words)
    assert len(anagrams) == 0

@pytest.mark.parametrize("words", 
[
    ["this", "that","the"],
    ["on", "more","things"],
])
def test_no_anagram(words):
    anagrams = anagramSolver(words)
    assert len(anagrams) == 0


