import sys
import pandas as pd

# C:\Users\prath\PycharmProjects\IT414\Lab2\dataset.csv
# C:\Users\prath\PycharmProjects\IT414\Lab4\201IT243_PrathamPatel_Dataset.csv
# C:\Users\prath\PycharmProjects\IT414\Lab5\dataset.csv

# n_args = len(sys.argv)
paths = ['C:\\Users\\prath\\PycharmProjects\\IT414\\Lab2\\dataset.csv', 'C:\\Users\\prath\\PycharmProjects\\IT414'
                                                                        '\\Lab4\\201IT243_PrathamPatel_Dataset.csv',
         'C:\\Users\\prath\\PycharmProjects\\IT414\\Lab5\\dataset.csv']
dfs = []

for i in range(len(paths)):
    df = pd.read_csv(paths[i])
    dfs.append(df)
    # print(f"Arg {i + 1} : {sys.argv[i + 1]}")

for i in range(len(dfs)):
    # sys.stdout.write("Hello")
    print(dfs[i].head())
