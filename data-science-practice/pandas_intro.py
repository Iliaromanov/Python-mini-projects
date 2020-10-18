
import pandas as pd

google_play = "/Users/iliarom.BASE.000/Desktop/Data-Science/google-playstore-data.csv"

# read_csv can be used to read .csv files
df = pd.read_csv(google_play) # df stands for data frame

print(df) # prints out the data frame in data table format
print(len(df)) # prints the amount of rows in df (10841)
print(df.columns) # prints column headers in array format

# in pandas 'object' means string

# .info method provides useful info on data frame
print(df.info())

# .dtype provides a data table describing the dtype of each column
print(df.dtypes)

# -------------
# you can choose a specific column of the df to print
print(df['Rating'])
# or you can print multiple columns
print(df[['App', 'Rating']])


# -------------
# it is also possible to retrieve specific rows using the .loc method
print(df.loc[1:3]) # **end index is included in this case**


# -------------
# its possible to combine both of the previous functions
print(df[['App', 'Rating']][1:4]) # **end index not included**
