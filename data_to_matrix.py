import sys
import pandas as pd

if len(sys.argv) < 2:
    raise Exception("Not eneugh arguamnts")

save_file = sys.argv[1]

df = pd.DataFrame()

lst = []
dct = {}

alfaPlus = 'abcdefghijklmnopqrstuvwxyz#_'
for item in alfaPlus:
    dct[item] = {}
    for iter2 in alfaPlus:
        dct[item][iter2] = 0

for line in sys.stdin:
    line = line.strip()
    line = line.split('=')
    line = [line[0].split(","),line[1]]

    dct[line[0][0]][line[0][1]] = float(line[1])


df = pd.DataFrame(dct).T.fillna(0)

sys.stdout.write(save_file)

df.to_csv(save_file)
