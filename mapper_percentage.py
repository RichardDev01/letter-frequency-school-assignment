import sys

sum_percentage = []

data = sys.stdin.readlines()

for line in data:
    input_string = line.split("\n")[0].split(" ")

    sum_percentage.append(int(input_string[1]))

# total values
total_count = sum(sum_percentage)

for inp in data:
    keys_val = inp.split(" ")
    keys = keys_val[0].split("-")
    sys.stdout.write(f"{keys[0]},{keys[1]}={int(keys_val[1]) / total_count *100}\n")
