import sys
import itertools

def readWords(filename):
    words = []
    try:
        with open(filename, "r") as f:
            for line in f:
                words.extend(line.split())
    except:
        print('Error reading file')
    return words

def anagramSolver(words):
    output = []
    # would turn this into a generator for better performance if the file size is very large
    for word in words:
        # itertools.permutations can return duplicates so create a dict and cast that into a list 
        permutations = list(dict.fromkeys(["".join(perm) for perm in itertools.permutations(word)]))
        # first permutation is just the word so pop it before searching for anagrams
        permutations.pop(0)
        for permutation in permutations:
            if permutation in words:
                output.append(permutation)
    return output

if __name__ == '__main__':
    words = readWords(sys.argv[1])
    if len(words) > 0:
        anagrams = anagramSolver(words)
        if len(anagrams) > 0:
            print(list(dict.fromkeys(anagrams)))
        else:
            print("no anagram found")