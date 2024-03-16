import typer
from csv_test import filtering, aggregating, joining

app = typer.Typer()

@app.command()
def hello(name: str, age:int, display_age:bool=True):
    print(f"Hello {name}")
    if display_age:
        print(f"Age {age}")
    # print(f"Age {age}")

@app.command()
def goodbye():
    print("Goodbye")

@app.command()
def filter(filename:str, conditions:list[str]):
    df = filtering(filename, conditions)
    print(df)

@app.command()
def aggregate(filepath:str, column:str):
    aggregating(filepath, column)

@app.command()
def join(filepath1:str, filepath2:str, column:str):
    # aggregating(filepath1, column)
    paths = [filepath1, filepath2]
    df = joining(paths, column)
    print(df)

if __name__ == "__main__":
    app()