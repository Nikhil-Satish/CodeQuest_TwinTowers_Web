# Welcome to our CSV Transformation CLI Tool
This is a CLI tool that performs these 4 transformations : Filtering, Joining, Aggregation and Formatting.
> [!NOTE]
> Our tool supports the use of CSV files with different delimiters such as ',', '\t', '\n' etc.
> Our tool stores the transformed CSV as a new CSV file which is stored in the present working directory.

For details regarding all the functionalities provided and general usage of arguments, users can use this:
```console
python script.py --help
```

This tools provides users with feaure of specifying their preference for delimiter and quotation style for the output transformed CSV file. These are passed as optional command line arguments when applying the transformation.
For more details regarding command style of each function, users can use this:
```console
python script.py "Transformation Name" --help
```

For all the 4 transformations, our CLI tool follows a common command style that is:
```console
python script.py "Transformation Name" "Function-specific Agruments" "Optional Arguments"
```

> [!CAUTION]
> Please make sure you have installed all the required libraries which can be installed using "pip install requirements.txt"


