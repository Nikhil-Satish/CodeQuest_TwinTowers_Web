import typer
from util import filtering, aggregating, joining, formatting
import pandas as pd
import csv

helper_str = """
    This is a command line tool for applying transformations to csv files. 4 transformation functionalities are provided as mentioned in under Commands.\n 
    Take a look at the list and find their usage using --help for each command.
    The tool supports autocompletion. 
    """
app = typer.Typer(help=helper_str)

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
    """
    Filter the input csv file based on the conditions entered as arguments
    """
    if filename == '':
        print("No file has been chosen")
        return
    extension = filename[-4:]
    if extension != ".csv" and extension != ".tsv":
        print("Incorrect file format specified, please add a pandas/csv supported file")
        return
    
    df = filtering(filename, conditions)
    print(df)
    df = pd.DataFrame(df)
    delim = format_delim(delim)

    df.to_csv('output.csv', sep=delim, quoting=quoting)

@app.command()
def aggregate(filepath:str, column:str, delim:str=',', quoting:int=0):
    """
    Perform aggregation operations such as SUM, AVERAGE, MINIMUM, MAXIMUM for a particular column
    """
    if filepath == '':
        print("No file has been chosen")
        return
    extension = filepath[-4:]
    if extension != ".csv" and extension != ".tsv":
        print("Incorrect file format specified, please add a pandas/csv supported file")
        return

    df = aggregating(filepath, column)
    df = pd.DataFrame(df)
    delim = format_delim(delim)

    df.to_csv('output.csv', sep=delim, quoting=quoting)
    

@app.command()
def format(filepath:str, column:str, delim:str=',', quoting:int=0):
    """
    Formats the data-time column to the standard UTC format
    """
    if filepath == '':
        print("No file has been chosen")
        return
    extension = filepath[-4:]
    if extension != ".csv" and extension != ".tsv":
        print("Incorrect file format specified, please add a pandas/csv supported file")
        return
    
    df = formatting(filepath, column)
    print(df)
    df = pd.DataFrame(df)
    delim = format_delim(delim)

    df.to_csv('output.csv', sep=delim, quoting=quoting)

@app.command()
def join(column:str, paths:list[str], delim:str=',', quoting:int=0):
    """
    Join 2 or more csv files having a common column
    """
    if len(paths) == 0:
        print("No file path specified")
        return
    for path in paths:
        extension = path[-4:]
        if extension != ".csv" and extension != ".tsv":
            print("Incorrect file format specified, please add a pandas/csv supported file")
            return

    df = joining(paths, column)
    if type(df) == type(0):
        return
    print(df)
    df = pd.DataFrame(df)
    delim = format_delim(delim)
    df.to_csv('output.csv', sep=delim, quoting=quoting)


if __name__ == "__main__":
    """
    Take a look at the list of commands and and find their usage using --help for each command
    """
    app()