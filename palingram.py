""" This script finds palindromes and palingrams """
import sys

def loadFileAsList(path, lowercase=True, uppercase=False):
    """
        This function takes in a path, checks locally if it exists,
        then loads it as a list.
    """
    try:
        with open(path) as in_file:
            #do something...
            text = in_file.read().strip().split('\n')
            if lowercase:
                text = [x.lower() for x in text]
            elif uppercase:
                text = [x.upper() for x in text]
            return text
    except IOError as e:
        print("Error opening %s\n Terminating program." % (path), file=sys.stderr)
        print("Error: %s" % (e), file=sys.stderr)

    sys.exit(1)


def findPalindromes(list):
    """
        For ever word in a list, checks if a word is longer than 1 character &
        equal forward as back
    """
    palindromes = []

    for word in list:
        if len(word) > 1 and word == word[::-1]:
            palindromes.append(word)
    return palindromes

def findPalingrams(list):
    palingrams = []
    for word in list:
        end = len(word)
        reversed = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == reversed[:end-i] and reversed[end-i:] in list:
                    palingrams.append((word, reversed[end-i]))
                if word[:i] == reversed[end-i:] and reversed[:end-i] in list:
                    palingrams.append((reversed[:end-i], word))

    return palingrams

def main():

    words = loadFileAsList("./resources/words.txt")
    palindromes = findPalindromes(words)
    print(palindromes)

    palingrams = findPalingrams(words)
    print(palingrams)



if __name__ == "__main__":
    main()
