"""mapper.py"""

import sys

for line in sys.stdin:
    alfa = 'abcdefghijklmnopqrstuvwxyz '

    line = line.strip()

    for index, word in enumerate(line[:-1]):
        # special characters are _
        if line[index].lower() not in alfa:
            l1 = '_'
        else:
            l1 = line[index].lower()
        if line[index + 1].lower() not in alfa:
            l2 = '_'
        else:
            l2 = line[index + 1].lower()

        # spaces are #
        if l1 == ' ':
            l1 = '#'
        if l2 == ' ':
            l2 = '#'
        sys.stdout.write(f'{l1}-{l2}\t{1}\n')