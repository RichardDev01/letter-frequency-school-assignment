"""mapper.py"""

import sys

for row in sys.stdin:
    row = row.strip()

    alphabet = 'abcdefghijklmnopqrstuvwxyz'  # Als we dit niet gebruiken neemt hij 'bijzondere' letters mee die we als speciaal teken willen zien.
    for index, char in enumerate(row[:-1]):
        combination = [row[index], row[index+1]]
        for combination_index in range(len(combination)):
            if str(combination[combination_index]).lower() in alphabet:
                combination[combination_index] = str(combination[combination_index]).lower()
            elif combination[combination_index] == ' ':
                combination[combination_index] = '#'
            else:
                combination[combination_index] = '_'

        sys.stdout.write(f'{combination[0]}-{combination[1]}\t{1}\n')
