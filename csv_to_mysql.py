# import sys
# import pandas as pd
import csv
import pandas as pd
from sqlalchemy import create_engine, types

engine = create_engine('mysql://root:rootpass@localhost/codequest') # enter your password and database names here

df = pd.read_csv("output.csv") # Replace Excel_file_name with your excel sheet name
df.to_sql('Info', con=engine, index=False, if_exists='append')
