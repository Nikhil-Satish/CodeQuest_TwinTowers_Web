import typer
from csv_test import filtering

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
    # print(filename)
    # print(conditions)
    df = filtering(filename, conditions)
    print(df)

    
if __name__ == "__main__":
    app()