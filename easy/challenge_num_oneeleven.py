'''
Codeeval #111 (Easy)

In this challenge you need to find the longest word in a sentence.
If the sentence has more than one word of the same length you should pick the first one.
'''

import sys


def return_longest_word(line):
    sorted_line = sorted(line.strip().split(' '), key=lambda x: len(x))
    if len(line) == 1:
        return sorted_line.pop()
    else:
        longest = sorted_line.pop()
        while sorted_line and len(longest) == len(sorted_line[-1]):
            longest = sorted_line.pop()
        return longest



def main():
    with open(sys.argv[1], 'r') as input_file:
        for line in input_file:
            print(return_longest_word(line))


if __name__ == '__main__':
    main()