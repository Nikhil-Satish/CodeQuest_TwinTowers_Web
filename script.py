import typer
from csv_test import filtering, aggregating, joining, formatting
import pandas as pd
import csv

app = typer.Typer()

def format_delim(delim):
    if len(delim) ==1 or len(delim) ==2:
        if len(delim) == 2:
            if delim[0] != "\\":
                print("Incorrect delimiter entered")
            else:
                if delim[1] == 't':
                    delim = '\t'
                elif delim[1] == 'n':
                    delim = '\n'
                else:
                    print("Invalid delimiter entered")
    else:
        print("Delimiter of incorrect length entered. Please enter a delimiter of length 1 or 2")
    return delim

@app.command()
def filter(filename:str, conditions:list[str], delim:str=',', quoting:int=0):
    df = filtering(filename, conditions)
    print(df)
    df = pd.DataFrame(df)
    delim = format_delim(delim)

    df.to_csv('output.csv', sep=delim, quoting=quoting)

@app.command()
def aggregate(filepath:str, column:str, delim:str=',', quoting:int=0):
    df = aggregating(filepath, column)
    df = pd.DataFrame(df)
    delim = format_delim(delim)

    df.to_csv('output.csv', sep=delim, quoting=quoting)
    

@app.command()
def format(filepath:str, column:str, delim:str=',', quoting:int=0):
    # aggregating(filepath, column)
    df = formatting(filepath, column)
    print(df)
    df = pd.DataFrame(df)
    delim = format_delim(delim)

    df.to_csv('output.csv', sep=delim, quoting=quoting)

@app.command()
def join(column:str, paths:list[str], delim:str=',', quoting:int=0):
    # aggregating(filepath1, column)
    # paths = [filepath1, filepath2]
    df = joining(paths, column)
    if type(df) == type(0):
        return
    print(df)
    df = pd.DataFrame(df)
    delim = format_delim(delim)
    df.to_csv('output.csv', sep=delim, quoting=quoting)


@app.command()
def hello(name: str, age:int, display_age:bool=True):
    print(f"Hello {name}")
    if display_age:
        print(f"Age {age}")
    # print(f"Age {age}")

@app.command()
def goodbye():
    print("Goodbye")

if __name__ == "__main__":
    app()