""" Converts input to pig latin using command line argument"""
import sys

VOWELS = ['a', 'e', 'i', 'o', 'u']

def convert_word(word):
    """ Converts a word into pig latin """

    if word[:1].lower() in VOWELS:
        #starts with a vowel
        word += "way"
    else:
        #starts with a consonant
        first_letter = word[:1]
        word = word[1:] + first_letter
        word += "ay"

    return word

def main():
    """ gathers input from command line"""

    if len(sys.argv) != 2:
        print("ERROR: Incorrect arguments....")
        print("Usage: pig_latin.py \"<YOUR INPUT STRING>\"")
    else:
        input_string = sys.argv[1]

        words = input_string.replace(',', '').replace('.', '').split(' ')
        output = ""
        for word in words:
            output += convert_word(word)
        print("original: %s" % (input_string))
        print("pig latin: %s" % (output))


if __name__ == "__main__":
    main()
