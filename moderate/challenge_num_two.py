'''
Codeeval 2 (Moderate)

Write a program to read a multiple line text file and write the 'N' longest lines to stdout. Where the file to be read is specified on the command line.
Input sample:

Your program should read an input file (the first argument to your program will be a path to a filename).
The first line contains the value of the number 'N' followed by multiple lines. You may assume that the input file is
formatted correctly and the number on the first line i.e. 'N' is a valid positive integer.
E.g.

2
Hello World
CodeEval
Quick Fox
A
San Francisco

Output sample:

The 'N' longest lines, newline delimited. Ignore all empty lines in the input. Ensure that there are no trailing empty spaces on each line you print.
Also ensure that the lines are printed out in decreasing order of length i.e. the output should be sorted based on their length.
E.g.

San Francisco
Hello World

'''

import sys


def n_longest_lines(line):
    n_lines = int(line[0])
    line = line[1:]
    return sorted(line, key=lambda x: len(x), reverse=True)[:n_lines]


def main():
    input_file = open(sys.argv[1], 'r')
    input_as_list = []
    for line in input_file:
        if line.rstrip():
            input_as_list.append(line.rstrip())

    for line in n_longest_lines(input_as_list):
        print(line)

    input_file.close()

if __name__ == '__main__':
    main()