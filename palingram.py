""" This script finds palindromes and palingrams """
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


def find_palindromes(word_list):
    """
        For ever word in a list, checks if a word is longer than 1 character &
        equal forward as back
    """
    palindromes = []

    for word in word_list:
        if len(word) > 1 and word == word[::-1]:
            palindromes.append(word)
    return palindromes

def find_palingrams(word_list):
    """
        Finds palingrams in given word_list.
        Finds palindromic sequences, then checks if other fraction of word is a
        real word.
        If so, its a palindrome, if not move on.
    """
    palingrams = []
    for word in word_list:
        end = len(word)
        reversed_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == reversed_word[:end-i] and reversed_word[end-i:] in word_list:
                    palingrams.append((word, reversed_word[end-i:]))
                if word[:i] == reversed_word[end-i:] and reversed_word[:end-i] in word_list:
                    palingrams.append((reversed_word[:end-i], word))

    return palingrams

def efficient_palingrams(word_list):
    """
        switched out lists for sets to speed up membership checking, and thus
        speed up the entire function or any program that uses this function
    """
    palingrams = []
    words = set(word_list)
    for word in words:
        end = len(word)
        reversed_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == reversed_word[:end-i] and reversed_word[end-i:] in words:
                    palingrams.append((word, reversed_word[end-i:]))
                if word[:i] == reversed_word[end-i:] and reversed_word[:end-i] in words:
                    palingrams.append((reversed_word[:end-i], word))

    return palingrams


def main():
    """ Makes calls to local functions to find palindromes & palingrams """
    words = load_file_as_list("./resources/words.txt")
    palindromes = find_palindromes(words)
    print(palindromes)

    #palingrams = find_palingrams(words)
    palingrams = efficient_palingrams(words)
    print(palingrams)



if __name__ == "__main__":
    main()
