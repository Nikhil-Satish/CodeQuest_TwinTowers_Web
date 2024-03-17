# import sys
import pandas as pd
import csv


def formatting(path, col):
    delim = None
    with open(path, newline='') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        delim = dialect.delimiter
    df = pd.read_csv(path, sep=delim)
    if col not in df:
        print("Specified column not present in specified CSV")
        return 0
    if df.dtypes[col] != 'int64':
        print("Specified column does not have the supported data type : int64")
        return 0
    try:
        df[col] = pd.to_datetime(df[col], unit='ms')
    except ValueError as e:
        print(f"Error converting '{col}' to datetime: {e}")
        return 0
    # df[col] = pd.to_datetime(df[col], unit='ms')
    # df[col] = df[col].apply(lambda x: datetime.datetime.fromtimestamp(x//1000).strftime('%Y-%m-%d %H:%M:%S'))
    return df


def joining(path, col):
    if len(path) < 2:
        print("Minimum 2 CSV file-paths required for join operation.")
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
    try:
        # Perform inner join on column 'A'
        ndf = pd.merge(df1, df2, on=col, how='inner')
    except Exception as e:
        print(f"Error during inner join: {e}")
        return 0
    # ndf = pd.merge(df1, df2, on=col, how='inner')
    for i in range(2, len(path)):
        df3 = pd.read_csv(path[i], sep=delim)
        if col not in df3:
            print("Join column not found in one of the CSVs")
            return 0
        try:
            # Perform inner join on column 'A'
            ndf = pd.merge(df3, ndf, on=col, how='inner')
        except Exception as e:
            print(f"Error during inner join: {e}")
            return 0
        # ndf = pd.merge(ndf, df3, on=col, how='inner')
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
    val = ['==', "!=", ">=", "<=", ">", "<"]
    for con in b:
        col = ''
        op = ''
        mode = 'lhs'
        o_ind = len(con)
        for o in operators:
            if o in con:
                o_ind = con.index(o)
                break
        if o_ind == len(con):
            print('No valid operators found. Valid operators : ==, !=, >, >=, <, <=')
            return 0
        terms = con.split(' ')
        t_ind = len(terms)
        for t in terms:
            if t in val:
                t_ind = terms.index(t)
                # print(f'here {t}, {t_ind}')
                break
        alt_col = ' '.join(terms[:t_ind])
        alt_op = ' '.join(terms[t_ind+1:])
        # print(fin, o_ind, len(con), terms[:o_ind])
        print(col, op)
        for c in con:
            if c not in operators:
                if c != ' ' and mode == 'lhs':
                    col += c
                if c != ' ' and mode == 'rhs':
                    op += c
            else:
                mode = 'rhs'
                continue
        if col not in curr:
            col = alt_col
        if col not in curr:
            print("Specified column not present in specified CSV")
            return 0
            # print(con, col, op)
        if curr.dtypes[col] == 'int64':
            try:
                op = int(op)
            except ValueError:
                print('Incompatible operand with column data type int64')
                return 0
        if curr.dtypes[col] == 'float64':
            try:
                op = float(op)
            except ValueError:
                print('Incompatible operand with column data type float64')
                return 0
        if '==' in con:
            # print('here')
            if curr.dtypes[col] == 'object':
                # curr[col] = pd.to_datetime(curr[col])
                # nd = pd.Timestamp(op)
                # ndf = curr.loc[curr[col] == nd]
                ndf = curr.loc[curr[col] == op]
            elif curr.dtypes[col] == 'int64':
                ndf = curr.loc[curr[col] == int(op)]
            elif curr.dtypes[col] == 'float64':
                ndf = curr.loc[curr[col] == float(op)]

        elif '!=' in con:
            if curr.dtypes[col] == 'object':
                # curr[col] = pd.to_datetime(curr[col])
                # nd = pd.Timestamp(op)
                # ndf = curr.loc[curr[col] != nd]
                ndf = curr.loc[curr[col] != op]
            elif curr.dtypes[col] == 'int64':
                ndf = curr.loc[curr[col] != int(op)]
            elif curr.dtypes[col] == 'float64':
                ndf = curr.loc[curr[col] != float(op)]

        elif '>' in con:
            # ndf = df
            if curr[col].dtypes == 'object':
                try:
                    curr[col] = pd.to_datetime(curr[col])
                except ValueError as e:
                    print(f"Error converting '{col}' to datetime: {e}")
                    return 0
                try:
                    nd = pd.Timestamp(op)
                except ValueError as e:
                    print(f"Error converting '{op}' to datetime: {e}")
                    return 0

            if '>=' in con:
                if curr.dtypes[col] == 'object':
                    # curr[col] = pd.to_datetime(curr[col])
                    # nd = pd.Timestamp(op)
                    ndf = curr.loc[curr[col] >= nd]
                    # print('Cannot perform ">=" operation for non numeric data type')
                elif curr.dtypes[col] == 'int64':
                    ndf = curr.loc[curr[col] >= int(op)]
                elif curr.dtypes[col] == 'float64':
                    ndf = curr.loc[curr[col] >= float(op)]
            else:
                if curr.dtypes[col] == 'object':
                    curr[col] = pd.to_datetime(curr[col])
                    nd = pd.Timestamp(op)
                    ndf = curr.loc[curr[col] > nd]
                    # print('Cannot perform ">" operation for non numeric data type')
                elif curr.dtypes[col] == 'int64':
                    ndf = curr.loc[curr[col] > int(op)]
                elif curr.dtypes[col] == 'float64':
                    ndf = curr.loc[curr[col] > float(op)]

        elif '<' in con:
            if curr[col].dtypes == 'object':
                try:
                    curr[col] = pd.to_datetime(curr[col])
                except ValueError as e:
                    print(f"Error converting '{col}' to datetime: {e}")
                    return 0
                try:
                    nd = pd.Timestamp(op)
                except ValueError as e:
                    print(f"Error converting '{op}' to datetime: {e}")
                    return 0
            if '<=' in con:
                if curr.dtypes[col] == 'object':
                    curr[col] = pd.to_datetime(curr[col])
                    nd = pd.Timestamp(op)
                    ndf = curr.loc[curr[col] <= nd]
                    # print('Cannot perform "<=" operation for non numeric data type')
                elif curr.dtypes[col] == 'int64':
                    ndf = curr.loc[curr[col] <= int(op)]
                elif df.dtypes[col] == 'float64':
                    ndf = curr.loc[curr[col] <= float(op)]

            else:
                if curr.dtypes[col] == 'object':
                    curr[col] = pd.to_datetime(curr[col])
                    nd = pd.Timestamp(op)
                    ndf = curr.loc[curr[col] < nd]
                    # print('Cannot perform "<" operation for non numeric data type')
                elif curr.dtypes[col] == 'int64':
                    ndf = curr.loc[curr[col] < int(op)]
                elif curr.dtypes[col] == 'float64':
                    ndf = curr.loc[curr[col] < float(op)]
        else:
            print('No valid operator found. Valid operators : ==, !=, >, >=, <, <=')
            return 0
        curr = ndf
    return ndf


def aggregating(path, column):
    delim = None
    with open(path, newline='') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        delim = dialect.delimiter
    df = pd.read_csv(path, sep=delim)
    if column not in df:
        print("Specified column not present in specified CSV")
        return 0
    try:
        # Attempt to calculate the sum of each column
        total = df[column].sum()
        average = df[column].mean()
        mini = df[column].min()
        maxi = df[column].max()
    except Exception as e:
        print(f"Unsupported datatypes for arithmetic operation: Error during calculation for {column}: {e}")

    print("Sum:", total, "\tAverage", average, "\tMinimum", mini, "\tMaximum ", maxi)

# pd1 = [[1, "pratham", 21], [2, "nikhil", 22], [3, "adarsh", 22], [4, "satyam", 23]]
# pd2 = [[1, 6.2], [2, 5.7], [3, 5.7], [4, 5.8]]
# pd3 = [[1, 75], [2, 64], [3, 72], [4, 70]]
# d1 = pd.DataFrame(pd1, columns=['ID', 'Name', 'Age'])
# d2 = pd.DataFrame(pd1, columns=['ID', 'Height'])
# d3 = pd.DataFrame(pd1, columns=['ID', 'Weight'])


# paths = ['Testing/join1.csv', 'Testing/join2.csv', 'Testing/Join3.csv', 'Testing/time.csv']
# odf = formatting(paths[-1], 'Name')
# print(odf)
# temp = odf['Open Time']
# temp.to_csv('Testing/formatted.csv')
# nd = pd.Timestamp('2021-01-03')
# ndf = temp.loc[temp < nd]
# print(ndf)
# path = 'Testing/formatted.csv'
# bo = ['Open Time <= 2021']
# odf = filtering(path, bo)
# print(odf)
