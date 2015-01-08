'''
Codeeval #174 (Easy)

Long serious texts are boring. Write a program that will make texts more informal: replace every other end punctuation
mark (period '.', exclamation mark '!', or question mark '?') with one of the following slang phrases, selecting them
one after another:

', yeah!',
', this is crazy, I tell ya.',
', can U believe this?',
', eh?',
', aw yea.',
', yo.',
'? No way!',
'. Awesome!'


'''

import sys


slang_position = 0
punctuation_found = 0


def replace_with_slang(line):
    global slang_position
    global punctuation_found
    slang = (', yeah!',
             ', this is crazy, I tell ya.',
             ', can U believe this?',
             ', eh?',
             ', aw yea.',
             ', yo.',
             '? No way!',
             '. Awesome!')
    punctuation = '.!?'

    modified_line = []

    for char in line:
        if any(punct in char for punct in punctuation):
            if punctuation_found % 2:
                modified_line.append(slang[slang_position])
                slang_position = (slang_position + 1) % len(slang)
            else:
                modified_line.append(char)
            punctuation_found += 1
        else:
            modified_line.append(char)

    return ''.join(modified_line)


def main():
    with open(sys.argv[1], 'r') as input_file:
        for line in input_file:
            print(replace_with_slang(line))

if __name__ == '__main__':
    main()