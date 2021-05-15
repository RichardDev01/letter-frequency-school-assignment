"""Transforms incoming data to matrix"""
import sys
import pandas as pd

if len(sys.argv) < 2:
    raise Exception("Not enough arguamnts")

# Save file location
save_file = sys.argv[1]

df = pd.DataFrame()

dct = {}

alphabet = 'abcdefghijklmnopqrstuvwxyz#_'
# Create a dictionary of 28*28
for item in alphabet:
    dct[item] = {}
    for iter2 in alphabet:
        dct[item][iter2] = 0

# File dictionary
for line in sys.stdin:
    line = line.strip()
    line = line.split('=')
    line = [line[0].split(","),line[1]]

    dct[line[0][0]][line[0][1]] = float(line[1])

# Dictionary to dataframe and fill empty spaces with 0
df = pd.DataFrame(dct).T.fillna(0)

# Save dataframe to file
df.to_csv(save_file)
