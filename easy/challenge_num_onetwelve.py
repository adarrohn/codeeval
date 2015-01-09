'''
Codeeval #112 (Easy)

You are given a list of numbers which is supplemented with positions that have to be swapped.
Input sample:

Your program should accept as its first argument a path to a filename. Input example is the following

1 2 3 4 5 6 7 8 9 : 0-8
1 2 3 4 5 6 7 8 9 10 : 0-1, 1-3

As you can see a colon separates numbers with positions.
Positions start with 0.
You have to process positions left to right. In the example above (2nd line) first you process 0-1, then 1-3.

'''

import sys


def swap_elements(line):
    elem_list, swaps = line.strip().split(' : ')
    elem_list = [int(val) for val in elem_list.split(' ')]
    swaps = swaps.split(', ')

    for swap in swaps:
        pos1, pos2 = swap.split('-')
        pos1, pos2 = int(pos1), int(pos2)
        elem_list[pos1], elem_list[pos2] = elem_list[pos2], elem_list[pos1]

    return ' '.join((str(elem) for elem in elem_list))


def main():
    with open(sys.argv[1], 'r') as input_file:
        for line in input_file:
            print(swap_elements(line))


if __name__ == '__main__':
    main()