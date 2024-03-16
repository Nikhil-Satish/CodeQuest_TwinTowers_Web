# import sys
import pandas as pd

# C:\Users\prath\PycharmProjects\IT414\Lab2\dataset.csv
# C:\Users\prath\PycharmProjects\IT414\Lab4\201IT243_PrathamPatel_Dataset.csv
# C:\Users\prath\PycharmProjects\IT414\Lab5\dataset.csv

# n_args = len(sys.argv)
paths = ['C:\\Users\\prath\\PycharmProjects\\IT414\\Lab2\\dataset.csv', 'C:\\Users\\prath\\PycharmProjects\\IT414'
                                                                        '\\Lab4\\201IT243_PrathamPatel_Dataset.csv',
         'C:\\Users\\prath\\PycharmProjects\\IT414\\Lab5\\dataset.csv', 'C:\\Users\\prath\\PycharmProjects\\Hackathon'
                                                                        '\\data.tsv']
dfs = []

for ind in range(len(paths)):
    tdf = pd.read_csv(paths[ind])
    dfs.append(tdf)
    # print(f"Arg {i + 1} : {sys.argv[i + 1]}")

# for i in range(len(dfs)):
#     # sys.stdout.write("Hello")
#     print(dfs[i].head())


def filtering(path, b):
    if path[len(path) - 3:] == 'csv':
        df = pd.read_csv(path)
    else:
        df = pd.read_csv(path, sep='\t')
    curr = df
    ndf = curr
    operators = ['=', "!", ">", "<"]

    for con in b:
        col = ''
        op = ''
        mode = 'lhs'
        for c in con:
            if c not in operators:
                if c != ' ' and mode == 'lhs':
                    col += c
                if c != ' ' and mode == 'rhs':
                    op += c
            else:
                mode = 'rhs'
                continue
        # print(con, col, op)
        if '==' in con:
            # print('here')
            if curr.dtypes[col] == 'object':
                ndf = curr.loc[curr[col] == op]
            elif df.dtypes[col] == 'int64':
                ndf = curr.loc[curr[col] == int(op)]
            elif df.dtypes[col] == 'float64':
                ndf = curr.loc[curr[col] == float(op)]
        elif '!=' in con:
            if curr.dtypes[col] == 'object':
                ndf = curr.loc[curr[col] != op]
            elif curr.dtypes[col] == 'int64':
                ndf = curr.loc[curr[col] != int(op)]
            elif curr.dtypes[col] == 'float64':
                ndf = curr.loc[curr[col] != float(op)]
        elif '>' in con:
            # ndf = df
            if '>=' in con:
                if curr.dtypes[col] == 'object':
                    print('Cannot perform ">=" operation for non numeric data type')
                elif curr.dtypes[col] == 'int64':
                    ndf = curr.loc[curr[col] >= int(op)]
                elif curr.dtypes[col] == 'float64':
                    ndf = curr.loc[curr[col] >= float(op)]
            else:
                if curr.dtypes[col] == 'object':
                    print('Cannot perform ">" operation for non numeric data type')
                elif curr.dtypes[col] == 'int64':
                    ndf = curr.loc[curr[col] > int(op)]
                elif curr.dtypes[col] == 'float64':
                    ndf = curr.loc[curr[col] > float(op)]
        elif '<' in con:
            if '<=' in con:
                if curr.dtypes[col] == 'object':
                    print('Cannot perform "<=" operation for non numeric data type')
                elif curr.dtypes[col] == 'int64':
                    ndf = curr.loc[curr[col] <= int(op)]
                elif df.dtypes[col] == 'float64':
                    ndf = curr.loc[curr[col] <= float(op)]
            else:
                if curr.dtypes[col] == 'object':
                    print('Cannot perform "<" operation for non numeric data type')
                elif curr.dtypes[col] == 'int64':
                    ndf = curr.loc[curr[col] < int(op)]
                elif curr.dtypes[col] == 'float64':
                    ndf = curr.loc[curr[col] < float(op)]
        else:
            'No valid operator found. Valid operators : ==, !=, >, >=, <, <='
            return 0
        curr = ndf
    return ndf


bo = ['numVotes > 100', 'averageRating >= 9.0']
odf = filtering(paths[-1], bo)
print(odf)
