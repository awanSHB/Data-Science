import pandas as pd
import numpy as np

'''
--------------------------Creating Series
'''

s1 = pd.Series(['a', 'b', 'c', 'd', 'f'])
print(s1)

l1 = ['a', 'b', 'c', 'd']
s1 = pd.Series(l1)
print(s1)

print("\n\n------------------------------\n\n")

'''
-------------------------Accessing The Elements Of Series
'''

s1 = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
s2 = pd.Series(s1)
print(s2)
print(s2[2:])

print("\n\n------------------------------\n\n")


'''
-------------------------Reading csv
1) .head(n)
'''


df = pd.read_csv("D:\PROGRAMMING\R\DATASETS\salaries.csv")
print(df.head(10))

s1 = df['work_year']
s2 = s1.head(10)
print(s2)
s3 = s1.notnull()
print(s3)
print("\n\n------------------------------\n\n")


'''
-----------------------Binary Operations

1) add
2) sub
'''

s1 = pd.Series([2, 3, 5, 7], index=['a', 'b', 'c', 'd'])
print(s1)

s2 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
print(s2)

##It will add the two series
s3 = s1.add(s2, fill_value=0)
print(s3)

##It will subtract the data
s4 = s1.sub(s2, fill_value=0)
print(s4)

print("\n\n------------------------------\n\n")


df = pd.read_csv("D:\PROGRAMMING\R\DATASETS\salaries.csv")
df.dropna(inplace=True)
print(df)

