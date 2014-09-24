'''
Codeeval 10 (Moderate)
Write a program to determine the Mth to last element of a list.
Input sample:

The first argument will be a path to a filename containing a series of space delimited characters followed by an integer representing a index into the list (1 based), one per line. E.g.

a b c d 4
e f g h 2

Output sample:

Print to stdout, the Mth element from the end of the list, one per line. If the index is larger than the list size, ignore that input. E.g.

a
g

'''

import sys


def mth_last(line):
    line_list = line.rstrip().split(' ')
    mth_element = int(line_list.pop())

    if mth_element > len(line_list):
        return
    else:
        return line_list[-mth_element]


def main():
    input_file = open(sys.argv[1], 'r')
    for line in input_file:
        mth_element = mth_last(line)
        if mth_element:
            print(mth_element)

    input_file.close()

if __name__ == '__main__':
    main()