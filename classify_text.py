import pandas as pd
import numpy as np
import sys
from sklearn.metrics import mean_squared_error

data_input = pd.read_csv(sys.stdin.readline())
data_input = np.array(data_input.drop(data_input.columns[0], axis=1).stack().tolist())
# print(data)

df_engels = pd.read_csv("tekst/engels_model.csv")
df_engels = np.array(df_engels.drop(df_engels.columns[0], axis=1).stack().tolist())
df_nederlands = pd.read_csv("tekst/nederland_model.csv")
df_nederlands = np.array(df_nederlands.drop(df_nederlands.columns[0], axis=1).stack().tolist())
# dfne = np.array(pd.read_csv("nederland_model.csv").drop(columns="", axis=1).stack().tolist())


# print(data)
#
# print(dfne.shape)
# print(dfen.shape)
# print(data.shape)

nederlands_result = abs(data_input - df_nederlands)
engels_result = abs(data_input - df_engels)

print(mean_squared_error(df_nederlands, data_input))
print(mean_squared_error(df_engels, data_input))

# print(f"{nederlands_result=}\n{engels_result=}\n")

# print(f"{nederlands_result.sum()=}\n{engels_result.sum()=}\n")
#
#
#
# if (nederlands_result.sum() < engels_result.sum()):
#     print(f"nederlands_result is closer")
# elif(nederlands_result.sum() == engels_result.sum()):
#     print(f"100% gelijk")
# else:
#     print(f"engels_result is closer")