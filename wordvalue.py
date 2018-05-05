from data import DICTIONARY, LETTER_SCORES
from itertools import permutations


def find_optimal(string):
    maxword = max_word_value(combinations(string))
    return maxword, calc_word_value(maxword)

def combinations(input):
    words = load_words() ## Loads the words
    ans=[]
    for n in range(1, len(input)+1): ## Gives all the possible combinations (subsets)
        for perm in permutations(input, n):
            if "".join(perm) in words: ## If this string is a real words, adds it to ans
                ans.append("".join(perm))
    return list(set(ans)) ## Returns no duplicates of the list

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as file:
        return file.read().splitlines()

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    sum = 0
    for c in word:
        sum += LETTER_SCORES.get(c.upper(), 0)
    return sum

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words()
    return max(words, key=calc_word_value)

if __name__ == "__main__":
    pass # run unittests to validate
