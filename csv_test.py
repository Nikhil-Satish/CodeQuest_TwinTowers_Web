# import sys
import pandas as pd
import csv


def filtering(path, b):
    delim = None
    with open(path, newline='') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        delim = dialect.delimiter
    df = pd.read_csv(path, sep=delim)
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

def aggregating(path, column):
    if path[len(path) - 3:] == 'csv':
        df = pd.read_csv(path)
    else:
        df = pd.read_csv(path, sep='\t')
    # df = pd.read_csv(path)
    total = df[column].sum()
    average = df[column].mean()
    mini = df[column].min()
    mini = df[column].max()
    print("Sum:", total, "\tAveage", average,"\tMinimum", mini)

path = 'data.tsv'
bo = ['numVotes > 1000', 'averageRating >= 9.0']
odf = filtering(path, bo)
print(odf)
