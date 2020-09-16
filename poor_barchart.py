"""
    A script for a poor man's bar chart.
    Prints out # of times a character appears in a string similar to a barchart
"""
import string
import sys


def main():
    """
        Setup the alphabet dictionary with inital value 0, get cmd line inputs,
        iterate over input, output data.
    """

    if len(sys.argv) != 2:
        print("Error Incorrect arguments")
        print("Usage: poor_barchart.py \"Your input here...\" ")
    else:

        alphabet = list(string.ascii_lowercase)
        alpha_dict = dict.fromkeys(alphabet, 0)

        for letter in sys.argv[1].lower().replace(' ', ''):
            if alpha_dict.get(letter) is not None:
                alpha_dict[letter] += 1

        lines = []
        for key in alpha_dict:
            line = key + ' : ['
            for i in range(0, alpha_dict[key]):
                line += key + ' '
            line += ']'
            lines.append(line)

        print("Input string: %s" % (sys.argv[1]))
        for line in lines:
            print(line)


if __name__ == "__main__":
    main()
