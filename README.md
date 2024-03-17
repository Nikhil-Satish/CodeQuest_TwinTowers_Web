# Welcome to our CSV Transformation CLI Tool
This is a CLI tool that performs these 4 transformations : Filtering, Joining, Aggregation and Formatting.
> [!NOTE]
> Our tool supports the use of CSV files with different delimiters such as ',', '\t', '\n' etc.
> Our tool stores the transformed CSV as a new CSV file which is stored in the present working directory.

For details regarding all the functionalities provided and general usage of arguments, users can use this:
```console
python script.py --help
```

Our tool expects the file path of the CSV files to be passed as arguments in command. This tools provides users with feaure of specifying their preference for delimiter and quotation style for the output transformed CSV file. These are passed as optional command line arguments when applying the transformation. 
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

## 1. Filtering
This funtion is used for selecting and retreiving rows based on column values. For this transformation, multiple conditions such as "City = Mangalore" and "DOB < 2002-03-01" can be passed in a single command execution to make it scalable and faster to use. 
An example of its use as follows:
```console
python script.py filter ../Input.csv "COLUMN1 = Value1" "COLUMN2 = Value2" "COLUMN3 = Value3"
```
## 2. Joining
This funtion is used for performing inner join (only common entries of the chosen column will be selected) on the specified CSVs. For making its usage efficient, multiple CSVs can be input along with a common column on which they will be joined and returned.   
An example of its use as follows:
```console
python script.py join "COLUMN" ../Input1.csv ../Input2.csv ../Input3.csv ../Input4.csv 
```

## 3. Aggregator
Aggregator is meant to be used for perfroming arithmetic analysis on the selected columns. This function will return the sum, average, maximum and minimum of all the specified columns hence maximising the analysis done in single command.
An example of its use as follows:
```console
python script.py aggregate ../Input.csv "COLUMN1" "COLUMN2" "COLUMN3" "COLUMN4"
```
> [!WARNING]
> Aggretor only works for numeric data in CSV otherwise it will throw an error. 
> Formatting expects UNIX timestamps, incompatible data entries will led to an error

# 4. Formatting
Formatting is designed for converting unreadable UNIX timestamps into human-interpretable time and date. This function expects a/multiple columns containg UXIX timestamps and output is the original CSV with only the specified columns transformed.
An example of its use as follows:
```console
python script.py format ../Input.csv "COLUMN1" "COLUMN2" "COLUMN3" "COLUMN4"
```

# Video Demonstration of the Work Done
[Google Drive link](https://drive.google.com/file/d/1KCdpTNKVG2sxT6YHjBS-m6vJPqfIPlyi/view?usp=sharing)
[YouTube link](https://youtu.be/yMwKCvsjLeY)


