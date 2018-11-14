# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import pandas as pd
import numpy as np

#https://pandas.pydata.org/pandas-docs/stable/merging.html

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'], 'B': ['B0', 'B1', 'B2', 'B3'], 'C': ['C0', 'C1', 'C2', 'C3'], 'D': ['D0', 'D1', 'D2', 'D3']}, index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'], 'B': ['B4', 'B5', 'B6', 'B7'], 'C': ['C4', 'C5', 'C6', 'C7'], 'D': ['D4', 'D5', 'D6', 'D7']}, index=[4, 5, 6, 7])
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'], 'B': ['B8', 'B9', 'B10', 'B11'], 'C': ['C8', 'C9', 'C10', 'C11'], 'D': ['D8', 'D9', 'D10', 'D11']}, index=[8, 9, 10, 11])
pd.concat([df1,df2,df3])
    
df4 = pd.DataFrame({'B': ['B2', 'B3', 'B6', 'B7'], 'D': ['D2', 'D3', 'D6', 'D7'], 'F': ['F2', 'F3', 'F6', 'F7']}, index=[2, 3, 6, 7])
pd.concat([df1,df4], axis=1, sort =False)
#     A    B    C    D    B    D    F
#0   A0   B0   C0   D0  NaN  NaN  NaN
#1   A1   B1   C1   D1  NaN  NaN  NaN
#2   A2   B2   C2   D2   B2   D2   F2
#3   A3   B3   C3   D3   B3   D3   F3
#6  NaN  NaN  NaN  NaN   B6   D6   F6
#7  NaN  NaN  NaN  NaN   B7   D7   F7
#if number only appear in one dataframe instead of both, it will show as NaN
#concat is not merge, it just combined

##MERGE
#pd.merge(df1,df4,how ='inner',on =['B','D'])
#how: default is inner
#left= first dataframe to use
#right = second dataframe
#on: what identifiers to use
#df1
#    A   B   C   D
#0  A0  B0  C0  D0
#1  A1  B1  C1  D1
#2  A2  B2  C2  D2
#3  A3  B3  C3  D3

#df4
#    B   D   F
#2  B2  D2  F2
#3  B3  D3  F3
#6  B6  D6  F6
#7  B7  D7  F7

pd.merge(df1,df4,how ='outer',on =['B','D'])
#     A   B    C   D    F
#0   A0  B0   C0  D0  NaN
#1   A1  B1   C1  D1  NaN
#2   A2  B2   C2  D2   F2
#3   A3  B3   C3  D3   F3
#4  NaN  B6  NaN  D6   F6
#5  NaN  B7  NaN  D7   F7

pd.merge(df1,df4,how ='inner',on =['B','D'])
#    A   B   C   D   F
#0  A2  B2  C2  D2  F2
#1  A3  B3  C3  D3  F3
#show row which there are all 

#base is df1-->how: left
pd.merge(df1,df4,how ='left',on =['B','D'])
#    A   B   C   D    F
#0  A0  B0  C0  D0  NaN
#1  A1  B1  C1  D1  NaN
#2  A2  B2  C2  D2   F2
#3  A3  B3  C3  D3   F3

#base is df4-->how: right
pd.merge(df1,df4,how ='right',on =['B','D'])
#     A   B    C   D   F
#0   A2  B2   C2  D2  F2
#1   A3  B3   C3  D3  F3
#2  NaN  B6  NaN  D6  F6
#3  NaN  B7  NaN  D7  F7

#merge datasets to be panel data using key: pd.merge(left, right, on='key')
#pd.merge(left, right, on=['key1', 'key2'])
#how = inner: when merge, only choose obers with all variables with no missing value
#use outer as it include more data so that we can trim later

#combine_first
#df1.combine_first(df2)
#only Nan number will be updated when another dataframe is added into the base one

#combine_first VS update
#df1.update(df2)
#it will also replace 2nd database number into 1st if there are both numbers in 1st and 2nd

#171
#by = groupby function
#on = base on identifier
#if there is no data, it will look for the before data instead of being Nan
#tolerance = most time accept for delay



