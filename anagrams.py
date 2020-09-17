""" This script finds anagrams within a word list """
import sys
from collections import Counter

def load_file_as_list(path, lowercase=True, uppercase=False, remove_alphabet=True):
    """
        This function takes in a path, checks locally if it exists,
        then loads it as a list.
        Takes in default parameters that assist with cleansing file data.
    """
    try:
        with open(path) as in_file:
             #do something...
            text = in_file.read().strip().split('\n')
            if lowercase:
                text = [x.lower() for x in text]
            elif uppercase:
                text = [x.upper() for x in text]
            if remove_alphabet:
                text = list(filter( lambda x: len(x) > 1, text))
            return text
    except IOError as error:
        print("Error opening %s\n Terminating program." % (path), file=sys.stderr)
        print("Error: %s" % (error), file=sys.stderr)

    sys.exit(1)


def find_anagrams(key, words):
    """
        Finds anagrams by sorting input, iterating words, and sorting each
        individual word to use the == comparison operator
    """
    anagrams = []
    key = sorted(key.lower())
    for word in words:
        if key == sorted(word.lower()):
            anagrams.append(word)

    return anagrams


def find_anagrams_with_dicts(key, words):
    """
        Finds anagrams by converting strings to Counter dictionaries, then
        comparing the two.
    """
    anagrams = []
    key_dict = Counter(key.lower())
    for word in words:
        if key_dict == Counter(word.lower()):
            anagrams.append(word)
    return anagrams



def find_anagrams_from_phrase(phrase_dict, words):
    """
        Finds sub-anagrams in whole phrases by eliminating spaces in phrase, then
        finding groups of words that could be used for a whole anagram
    """
    sub_anagrams = []

    for word in words:
        word_dict = Counter(word.lower())
        if phrase_dict & word_dict == word_dict:
            sub_anagrams.append(word)
    return sub_anagrams






def main():
    """ Makes calls to local functions to load a word list and find anagrams"""
    words = load_file_as_list("./resources/words.txt")
    phrase = input("Enter a phrase to check for anagrams: ")

    # words = ["forest", "fern", "nerd", "fortes", "forts", "rafts", "foster", "softer"]
    # phrase = "soft forest"

    words.extend(['a', 'i'])

    limit = len(phrase)
    current_phrase = ""
    leftovers =  Counter(phrase.lower().replace(" ", ""))

    while len(current_phrase) < limit:

        current_fitting_words = find_anagrams_from_phrase(leftovers, words)
        if len(current_fitting_words) == 0:
            print("\nSorry there are no anagrams available for the current",
            " phrase: %s" %(current_phrase))
            sys.exit(0)
        print("Original phrase: %s" % (phrase))
        print("Current phrase: %s" % (current_phrase))
        print("Left over letters: %s" % (leftovers))
        print("Select one of these words: ")
        print(current_fitting_words)
        print('\n\n')

        user_input = input("Enter one of the words above or anything else to quit: ")
        if not user_input in current_fitting_words:
            print("exiting....")
            sys.exit(0)
        else:
            current_phrase += user_input+ ' '
            leftovers -= Counter(user_input)


    print("Original phrase: %s" % (phrase))
    print("Final phrase: %s" % (current_phrase))




if __name__ == "__main__":
    main()
