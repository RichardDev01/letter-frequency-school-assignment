import sys

"""
This function reduces the predicted languages
"""

current_language = None
current_count = 0
word = None

for line in sys.stdin:

    line = line.strip()
    language, count = line.split('\t', 1)

    count = int(count)

    if current_language == language:
        current_count += count
    else:
        if current_language:
            sys.stdout.write('%s %s\n' % (current_language, current_count))
        current_count = count
        current_language = language

if current_language == language:
    sys.stdout.write('%s %s' % (current_language, current_count))
