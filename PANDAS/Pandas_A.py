import pandas as pd

"""
---------------------------Data Frame
"""

lst = ['hello', 'my', 'name', 'is', 'pandas']
df = pd.DataFrame(lst)
print(df)
print("\n\n <-------------------------------> \n\n")

## 2) From Dictionaries

dct = {'Name': ['A', 'B', 'C', 'D'], 
       'Age' : [20, 21, 22, 23]}
df = pd.DataFrame(dct)
print(df)
print("\n\n <-------------------------------> \n\n")

## 3) Accessing columns


dct = {'Name': ['A', 'B', 'C', 'D'], 
       'Age' : [20, 21, 22, 23],
       'Marks': [11, 12, 13, 14]}
df = pd.DataFrame(dct)
print(df)
print(df[['Name', 'Marks']])
print("\n\n <-------------------------------> \n\n")


## 4) Selecting the rows

dct = {'Name': ['A', 'B', 'C', 'D'], 
       'Age' : [20, 21, 22, 23],
       'Marks': [11, 12, 13, 14]}
df = pd.DataFrame(dct)
first = df.loc[df['Name']=='A']
second = df.loc[df['Name']=='D']
print(first, "\n", second)
print()

dct = {'Name': ['A', 'B', 'C', 'D'], 
       'Age' : [20, 21, 22, 23],
       'Marks': [11, 12, 13, 14]}
df = pd.DataFrame(dct)

r1 = df.loc[1]
print(r1)                           ##Using loc
print()

r2 = df.iloc[1]
print(r2)                           ##Using iloc
print("\n\n <-------------------------------> \n\n")



"""
---------------------------------Missing Data

1) isnull()
2) notnull()
"""

import numpy as np

dct = {'Name': ['A', 'B',np.nan , 'D'], 
       'Age' : [20, np.nan, 22, 23],
       'Marks': [np.nan, 12, 13, 14]}
df = pd.DataFrame(dct)
print(df)
print()

print(df.isnull())                      ##isnull()
print()
print(df.notnull())                     ##notnull()
print("\n\n <-------------------------------> \n\n")


"""
--------Filling Missing Values

1) fillna
2) replace()
3) interpolate
"""


dct = {'Name': ['A', 'B',np.nan , 'D'], 
       'Age' : [20, np.nan, 22, 23],
       'Marks': [np.nan, 12, 13, 14]}
df = pd.DataFrame(dct)

print(df.fillna(0))                     ##Using fillna
print(df.fillna(df.mean()))
df = df.replace(np.nan, 'unknown')      ##Using replace
print(df)

print("\n\n <-------------------------------> \n\n")

"""
------------Dropping Missing values

1) dropna()
"""
dct = {'Name': ['A', 'B',np.nan , 'D', 'E'], 
       'Age' : [20, np.nan, 22, 23, 24],
       'Marks': [np.nan, 12, 13, 14, 15]}
df = pd.DataFrame(dct)

print("Rows without the missing values:\n")
df = df.dropna()
print(df)
print("\n\n <-------------------------------> \n\n")

"""
----------------------------Iterating Over Rows and Columns

"""
dct = {'Name': ['A', 'B',np.nan , 'D', 'E'], 
       'Age' : [20, np.nan, 22, 23, 24],
       'Marks': [np.nan, 12, 13, 14, 15]}
df = pd.DataFrame(dct)

#1
for i in range(4):
    print(df.iloc[i], "\n")
print("\n-------------\n")

#2
for i, j in df.iterrows():
    print(i, j, "\n")
print("\n-------------\n")
for i in df:
    print(df[i])