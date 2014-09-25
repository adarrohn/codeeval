'''
Codeeval 93 (Easy)

 Write a program which capitalizes the first letter of each word in a sentence.
Input sample:

Your program should accept as its first argument a path to a filename. Input example is the following
Output sample:

Hello world
javaScript language
a letter
1st thing

Print capitalized words in the following way.

Hello World
JavaScript Language
A Letter
1st Thing

'''

import sys


def capitalize_words(line):
    capitalized_list = [''.join([word[0].upper(),
                                word[1:]]) for word in line.split(' ')]
    return ' '.join(capitalized_list)


def main():
    input_file = open(sys.argv[1], 'r')
    for line in input_file:
        print(capitalize_words(line.rstrip()))

    input_file.close()

if __name__ == '__main__':
    main()