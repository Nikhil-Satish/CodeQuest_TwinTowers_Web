# import sys
import pandas as pd
import csv
import datetime


def formatting(path, col):
    delim = None
    with open(path, newline='') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        delim = dialect.delimiter
    df = pd.read_csv(path, sep=delim)
    if df.dtypes[col] != 'int64':
        print("Specified column does not have the supported data type : int64")
        return 0
    df[col] = pd.to_datetime(df[col], unit='ms')
    # df[col] = df[col].apply(lambda x: datetime.datetime.fromtimestamp(x//1000).strftime('%Y-%m-%d %H:%M:%S'))
    return df

def joining(path, col):
    if len(path) < 2:
        print("Minimum 2 CSV file-paths required.")
        return 0
    delim = None
    with open(path[0], newline='') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        delim = dialect.delimiter
    df1 = pd.read_csv(path[0], sep=delim)
    df2 = pd.read_csv(path[1], sep=delim)
    if col not in df1 or col not in df2:
        print("Join column not found in one of the CSVs")
        return 0
    ndf = pd.merge(df1, df2, on=col, how='inner')
    for i in range(2, len(path)):
        df3 = pd.read_csv(path[i], sep=delim)
        if col not in df3:
            print("Join column not found in one of the CSVs")
            return 0
        ndf = pd.merge(ndf, df3, on=col, how='inner')
    return ndf


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
            elif 'datetime64' in df.dtypes[col]:
                curr[col] = pd.to_datetime(curr[col])
                nd = pd.Timestamp(op)
                ndf = curr.loc[curr[col] == nd]
        elif '!=' in con:
            if curr.dtypes[col] == 'object':
                ndf = curr.loc[curr[col] != op]
            elif curr.dtypes[col] == 'int64':
                ndf = curr.loc[curr[col] != int(op)]
            elif curr.dtypes[col] == 'float64':
                ndf = curr.loc[curr[col] != float(op)]
            elif 'datetime64' in df.dtypes[col]:
                curr[col] = pd.to_datetime(curr[col])
                nd = pd.Timestamp(op)
                ndf = curr.loc[curr[col] != nd]
        elif '>' in con:
            # ndf = df
            if '>=' in con:
                if curr.dtypes[col] == 'object':
                    print('Cannot perform ">=" operation for non numeric data type')
                elif curr.dtypes[col] == 'int64':
                    ndf = curr.loc[curr[col] >= int(op)]
                elif curr.dtypes[col] == 'float64':
                    ndf = curr.loc[curr[col] >= float(op)]
                elif 'datetime64' in df.dtypes[col]:
                    curr[col] = pd.to_datetime(curr[col])
                    nd = pd.Timestamp(op)
                    ndf = curr.loc[curr[col] >= nd]
            else:
                if curr.dtypes[col] == 'object':
                    print('Cannot perform ">" operation for non numeric data type')
                elif curr.dtypes[col] == 'int64':
                    ndf = curr.loc[curr[col] > int(op)]
                elif curr.dtypes[col] == 'float64':
                    ndf = curr.loc[curr[col] > float(op)]
                elif 'datetime64' in df.dtypes[col]:
                    curr[col] = pd.to_datetime(curr[col])
                    nd = pd.Timestamp(op)
                    ndf = curr.loc[curr[col] > nd]
        elif '<' in con:
            if '<=' in con:
                if curr.dtypes[col] == 'object':
                    print('Cannot perform "<=" operation for non numeric data type')
                elif curr.dtypes[col] == 'int64':
                    ndf = curr.loc[curr[col] <= int(op)]
                elif df.dtypes[col] == 'float64':
                    ndf = curr.loc[curr[col] <= float(op)]
                elif 'datetime64' in df.dtypes[col]:
                    curr[col] = pd.to_datetime(curr[col])
                    nd = pd.Timestamp(op)
                    ndf = curr.loc[curr[col] <= nd]
            else:
                if curr.dtypes[col] == 'object':
                    print('Cannot perform "<" operation for non numeric data type')
                elif curr.dtypes[col] == 'int64':
                    ndf = curr.loc[curr[col] < int(op)]
                elif curr.dtypes[col] == 'float64':
                    ndf = curr.loc[curr[col] < float(op)]
                elif 'datetime64' in df.dtypes[col]:
                    curr[col] = pd.to_datetime(curr[col])
                    nd = pd.Timestamp(op)
                    ndf = curr.loc[curr[col] < nd]
        else:
            'No valid operator found. Valid operators : ==, !=, >, >=, <, <='
            return 0
        curr = ndf
    return ndf


def aggregating(path, column):
    delim = None
    with open(path, newline='') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        delim = dialect.delimiter
    df = pd.read_csv(path, sep=delim)
    total = df[column].sum()
    average = df[column].mean()
    mini = df[column].min()
    maxi = df[column].max()
    print("Sum:", total, "\tAverage", average,"\tMinimum", mini, "\tMaximum ",maxi)

# pd1 = [[1, "pratham", 21], [2, "nikhil", 22], [3, "adarsh", 22], [4, "satyam", 23]]
# pd2 = [[1, 6.2], [2, 5.7], [3, 5.7], [4, 5.8]]
# pd3 = [[1, 75], [2, 64], [3, 72], [4, 70]]
# d1 = pd.DataFrame(pd1, columns=['ID', 'Name', 'Age'])
# d2 = pd.DataFrame(pd1, columns=['ID', 'Height'])
# d3 = pd.DataFrame(pd1, columns=['ID', 'Weight'])


# paths = ['Testing/join1.csv', 'Testing/join2.csv', 'Testing/Join3.csv', 'Testing/time.csv']
# odf = formatting(paths[-1], 'Open Time')
# temp = odf['Open Time']
# nd = pd.Timestamp('2021-01-03')
# ndf = temp.loc[temp < nd]
# print(ndf)
# path = 'Testing/data.tsv'
# bo = ['numVotes > 1000', 'averageRating >= 9.0']
# odf = filtering(path, bo)
# print(odf)
