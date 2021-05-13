import sys

sum_percentage = []

data = sys.stdin.readlines()

for line in data:

    # print(line)
    input_string = line.split("\n")[0].split(" ")
    # print(input_string)
    # for inp in input_string:
    #     print(inp)
        # keys_val = inp.split(" ")
    #     # keys_val = inp
    # keys_val = line
    # keys = keys_val[0].split("-")
    sum_percentage.append(int(input_string[1]))
        # sys.stdout.write(f"{keys[0]}<-->{keys[1]}={keys_val[1]}\n")
        # matrix_list.append([keys[0]],[keys[1]])
        # sys.stdout.write(f"{keys_val}")

    # total values
    total_count = sum(sum_percentage)
# print(total_count)

for inp in data:
    # print(inp)
    keys_val = inp.split(" ")
    keys = keys_val[0].split("-")
    # print(keys_val)
    sys.stdout.write(f"{keys[0]},{keys[1]}={int(keys_val[1]) / total_count *100}\n")
