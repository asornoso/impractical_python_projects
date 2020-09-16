""" This script finds anagrams within a word list """
import sys

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

def main():
    """ Makes calls to local functions to load a word list and find anagrams"""
    words = load_file_as_list("./resources/words.txt")

    user_input = input("Enter a word to check for anagrams: ")

    found = find_anagrams(user_input, words)
    if len(found) == 0:
        print("No results found for %s" % (user_input))
    else:
        print(found)


if __name__ == "__main__":
    main()
