"""Classify input text file to Dutch or English language"""
import sys
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error


def mapper_lf(row: list) -> str:
    """
    Map the inputs with 1

    :param row: list of string, each element contains a sentence
    :return: string like mapper structure compared to mapper_lf.py
    """
    output_string = ""
    alfa = 'abcdefghijklmnopqrstuvwxyz '

    for index, word in enumerate(row[:-1]):
        # special characters are _
        if row[index].lower() not in alfa:
            l1 = '_'
        else:
            l1 = row[index].lower()
        if row[index + 1].lower() not in alfa:
            l2 = '_'
        else:
            l2 = row[index + 1].lower()

        # spaces are #
        if l1 == ' ':
            l1 = '#'
        if l2 == ' ':
            l2 = '#'
        output_string += f'{l1}-{l2}\t{1}\n'
        # sys.stdout.write(f'{l1}-{l2}\t{1}\n')
    return output_string


def sort_lf(input_str: str) -> str:
    """
    Sort the input

    :param input_str:
    :return: string like sort structure compared to built in sort function from windows/linux
    """
    output_string = ""
    input_list = input_str.split("\n")
    input_list.sort()
    for item in input_list[1:]:
        output_string += item + "\n"
    return output_string[:-1]


def reduce_lf(input_str: str) -> str:
    """
    Reduce the inputs

    :param input_str:
    :return: string like reduce structure compared to reduce_lf.py
    """
    output_string = ""
    current_word = None
    current_count = 0
    word = None
    input_str = input_str.split("\n")
    # print(input_str)
    for line in input_str:
        # print(line)
        line = line.strip()
        word, count = line.split('\t', 1)

        try:
            count = int(count)
        except ValueError:
            continue

        if current_word == word:
            current_count += count
        else:
            if current_word:
                output_string += '%s %s\n' % (current_word, current_count)
                # sys.stdout.write('%s %s\n' % (current_word, current_count))
            current_count = count
            current_word = word

    if current_word == word:
        output_string += '%s %s' % (current_word, current_count)
        # sys.stdout.write('%s %s' % (current_word, current_count))
    return output_string


def mapper_percentage(input_str: str) -> str:
    """
    Map the inputs with percentage from the sum of the matrix

    :param input_str:
    :return: string like mapper structure compared to mapper_percentage.py
    """
    output_string = ""
    sum_percentage = []

    input_list = input_str.split("\n")

    for line in input_list:
        value_string = line.split("\n")[0].split(" ")

        sum_percentage.append(int(value_string[1]))

    # total values
    total_count = sum(sum_percentage)

    for inp in input_list:
        keys_val = inp.split(" ")
        keys = keys_val[0].split("-")
        output_string += f"{keys[0]},{keys[1]}={int(keys_val[1]) / total_count * 100}\n"
        # sys.stdout.write(f"{keys[0]},{keys[1]}={int(keys_val[1]) / total_count * 100}\n")
    return output_string[:-1]


def data_to_matrix(input_str: str) -> pd.DataFrame:
    """
    Transforms the data to a matrics

    :param input_str:
    :return: panda dataframe with percentages
    """
    input_list = input_str.split("\n")
    dct = {}

    alfaPlus = 'abcdefghijklmnopqrstuvwxyz#_'
    for item in alfaPlus:
        dct[item] = {}
        for iter2 in alfaPlus:
            dct[item][iter2] = 0

    for line in input_list:
        line = line.strip()
        line = line.split('=')
        line = [line[0].split(","), line[1]]

        dct[line[0][0]][line[0][1]] = float(line[1])

    df = pd.DataFrame(dct).T.fillna(0)
    return df


def compare_row(nederlands_model: pd.DataFrame, engels_model: pd.DataFrame, input_data: list) -> list:
    """
    Compares the input data with the models and determine the language

    :param nederlands_model:
    :param engels_model:
    :param input_data:
    :return:
    """
    predicted_lst = [0, 0]
    for index, row in enumerate(input_data):
        try:
            row_result = data_to_matrix(mapper_percentage(reduce_lf(sort_lf(mapper_lf(row))))).reset_index()
        except ValueError:
            print(f"this row has unknown value\t | rowID= {index} | {row} |")
            continue
        row_result = np.array(row_result.drop(row_result.columns[0], axis=1).stack().tolist())

        # nederlands_result = abs(row_result - nederlands_model).sum()
        # engels_result = abs(row_result - engels_model).sum()

        nederlands_result = mean_squared_error(nederlands_model, row_result)
        engels_result = mean_squared_error(engels_model, row_result)

        if nederlands_result < engels_result:
            predicted_lst[0] += 1
        else:
            predicted_lst[1] += 1
    return predicted_lst


# System arguments given for the python execution
dutch_model_path = save_file = sys.argv[1]
english_model_path = sys.argv[2]
input_text_path = sys.argv[3]

# Loading Dutch dataframe matrix
df_dutch = pd.read_csv(dutch_model_path)
df_dutch = np.array(df_dutch.drop(df_dutch.columns[0], axis=1).stack().tolist())

# Loading English dataframe matrix
df_english = pd.read_csv(english_model_path)
df_english = np.array(df_english.drop(df_english.columns[0], axis=1).stack().tolist())

# Loading input_data data from text file and remove new line chars
data_input = [line.rstrip('\n') for line in open(input_text_path, encoding="utf8").readlines()]

# Compare each row in given input_data file to the dutch and english dateframe matrix
outcome = compare_row(df_dutch, df_english, data_input)

# Display results
print(f"\nThe result of the given text file is:\n"
      f"Dutch sentences: {outcome[0]}\n"
      f"English sentences: {outcome[1]}")

"""
row_result = data_to_matrix(mapper_percentage(reduce_lf(sort_lf(mapper_lf(data_input[0]))))).reset_index()

row_result = np.array(row_result.drop(row_result.columns[0], axis=1).stack().tolist())

# nederlands_result = abs(row_result - df_dutch)
# engels_result = abs(row_result - df_english)
#
# print(mean_squared_error(df_dutch, row_result))
# print(mean_squared_error(df_english, row_result))
"""