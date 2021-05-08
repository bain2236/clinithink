import sys
import itertools

def read_words(filename):
    words = []
    try:
        with open(filename, "r") as f:
            for line in f:
                words.extend(line.split())
    except:
        print('Error reading file')
    return words

def anagram_solver(words):
    output = []
    # would turn this into a generator for better performance if the file size is very large
    for word in words:
        # itertools.permutations can return duplicates so create a dict and cast that into a list 
        permutations = list(dict.fromkeys(["".join(perm) for perm in itertools.permutations(word)]))
        # first permutation is just the original word so pop it before searching for anagrams otherwise the word itself gets found which isn't an anagram
        permutations.pop(0)
        for permutation in permutations:
            if permutation in words:
                output.append(permutation)
    # make the anagram list into an ordered set 
    print('anagrams found {0}'.format(set(dict.fromkeys(output))))
    return set(dict.fromkeys(output)) 
    
    

if __name__ == '__main__':
    words = read_words(sys.argv[1])
    if len(words) > 0:
        anagrams = anagram_solver(words)
        
        if len(anagrams) > 0:
            print(anagrams)
        else:
            print("no anagram found")  