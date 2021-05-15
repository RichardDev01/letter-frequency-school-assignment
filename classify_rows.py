"""Classify input text file to Dutch or English language"""
import sys
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error


def mapper_lf(row: list) -> str:
    """
    Map the inputs with 1 and replaces spaces with ' ' and special chars with '_'

    :param row: list of string, each element contains a sentence
    :return: string like mapper structure compared to mapper_lf.py
    """
    output_string = ""

    # Als we dit niet gebruiken neemt hij 'bijzondere' letters mee die we als speciaal teken willen zien.
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for index, char in enumerate(row[:-1]):
        combination = [row[index], row[index+1]]
        for combination_index in range(len(combination)):
            if str(combination[combination_index]).lower() in alphabet:
                combination[combination_index] = str(combination[combination_index]).lower()
            elif combination[combination_index] == ' ':
                combination[combination_index] = '#'
            else:
                combination[combination_index] = '_'

        output_string += f'{combination[0]}-{combination[1]}\t{1}\n'

    return output_string

def sort_lf(input_str: str) -> str:
    """
    Sort the input

    :param input_str: input strings is equal to what you can expect from a reduce/mapper structure like hadoop
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

    :param input_str: input strings is equal to what you can expect from a reduce/mapper structure like hadoop
    :return: string like reduce structure compared to reduce_lf.py
    """
    output_string = ""
    current_word = None
    current_count = 0
    word = None
    input_str = input_str.split("\n")

    for line in input_str:
        line = line.strip()
        word, count = line.split('\t', 1)
        count = int(count)

        if current_word == word:
            current_count += count
        else:
            if current_word:
                output_string += '%s %s\n' % (current_word, current_count)

            current_count = count
            current_word = word

    if current_word == word:
        output_string += '%s %s' % (current_word, current_count)

    return output_string


def mapper_percentage(input_str: str) -> str:
    """
    Map the inputs with percentage from the sum of the matrix

    :param input_str: input strings is equal to what you can expect from a reduce/mapper structure like hadoop
    :return: string like mapper structure compared to mapper_percentage.py
    """
    output_string = ""
    sum_percentage = []

    input_list = input_str.split("\n")

    # Get sum of total combinations
    for line in input_list:
        value_string = line.split("\n")[0].split(" ")
        sum_percentage.append(int(value_string[1]))

    # Total values
    total_count = sum(sum_percentage)

    # Map keys with percentage value
    for inp in input_list:
        keys_val = inp.split(" ")
        keys = keys_val[0].split("-")
        output_string += f"{keys[0]},{keys[1]}={int(keys_val[1]) / total_count * 100}\n"
    return output_string[:-1]


def data_to_matrix(input_str: str) -> pd.DataFrame:
    """
    Transforms the data to a matrics

    :param input_str: input strings is equal to what you can expect from a reduce/mapper structure like hadoop
    :return: panda dataframe with percentages
    """
    input_list = input_str.split("\n")
    dct = {}

    alphabet = 'abcdefghijklmnopqrstuvwxyz#_'
    # Create a dictionary of 28*28
    for item in alphabet:
        dct[item] = {}
        for iter2 in alphabet:
            dct[item][iter2] = 0

    # File dictionary
    for line in input_list:
        line = line.strip()
        line = line.split('=')
        line = [line[0].split(","), line[1]]

        dct[line[0][0]][line[0][1]] = float(line[1])

    # Dictionary to dataframe and fill empty spaces with 0
    df = pd.DataFrame(dct).T.fillna(0)
    return df

def get_result(nederlands_model: pd.DataFrame, engels_model: pd.DataFrame, input_data: list):
    """
    Compares the input data with the models and determine the language and maps it

    :param nederlands_model:
    :param engels_model:
    :param input_data: list of strings, each element contains a sentence
    """
    for index, row in enumerate(input_data):
        # Empty row / sentence
        if row == '':
            continue

        # Mapper/reduce structure
        row_result = data_to_matrix(mapper_percentage(reduce_lf(sort_lf(mapper_lf(row))))).reset_index()

        # Convert outcome to a list
        row_result = np.array(row_result.drop(row_result.columns[0], axis=1).stack().tolist())

        nederlands_result = abs(row_result - nederlands_model).sum()
        engels_result = abs(row_result - engels_model).sum()

        # nederlands_result = mean_squared_error(nederlands_model, row_result)
        # engels_result = mean_squared_error(engels_model, row_result)

        if nederlands_result < engels_result:
            sys.stdout.write('NL\t1\n')
        else:
            sys.stdout.write('EN\t1\n')


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

get_result(df_dutch, df_english, data_input)
