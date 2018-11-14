# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import pandas as pd
import numpy as np

df = pd.read_csv("http://rcs.bu.edu/examples/python/data_analysis/Salaries.csv")
df.sort_values(by = 'service')
df.sort_values(by = ['service','salary'])
df.sort_values(by = ['service','salary'], ascending = [False, False])
df.sort_values(by = ['service','salary'], ascending = [True, False])

#dropna (VERY IMPORTANT?)
flights = pd.read_csv ("http://rcs.bu.edu/examples/python/data_analysis/flights.csv")
flights[flights.isnull().any(axis=1)].head()
flights[flights.isnull().any(axis=1)]
#axis =1 means work on rows, =0 means column
flights.dropna()
flights
#wont save?
flights.dropna(thresh = 14).dropna(axis=1,how='all')
#e.g. ask how many rows left
#test: merge 2 data set in one sentence
#calculate mean/ sd
df = flights.fillna(0)
df.mean()
df['dep_time'].std()
#112
flights.dropna(how = 'any')
len(flights)
#subset will be a list
#default axis = 0
#113
df = pd.DataFrame([[np.nan, 2 , np.nan, 0], [3, 4, np.nan, 1], [np.nan, np.nan, np.nan, 5]], columns= list( 'ABCD' )) 
df.dropna(axis=1, how= 'all')
#drop the column only if all column values are NaN
df.dropna(axis=1, how='any' ) 
#drop the column if at Lease one NaN cell, so only the Last column remains 
#   D
#0  0
#1  1
#2  5
df.dropna(thresh= 2) 
#Keep only the rows with at Least 2 non-na values
#     A    B   C  D
#0  NaN  2.0 NaN  0
#1  3.0  4.0 NaN  1
list('ABCD')
flights['dep_time']
len(flights['dep_time'])
len(flights['dep_time'].dropna())
#drop if dep time is nan
len(flights.dropna())
#drop if any row or colume is nan
flights[flights.isnull().any(axis=1)]

#115
from pandas import Series 
import numpy as np 
s1 = Series([1, 2, np.NaN]) 
#create series
s = s1.dropna(axis=0, inplace=False) 
#Remove null values from series 
s1 = Series([1, 2, np.NaN,3,4,5,6,np.nan]) 
s1.dropna()

#116
s1.sum()
#will ignore nan
s1.cumsum()
#cumulative sum

#119
flights[['dep_delay','arr_delay']].agg(['min','mean','max'])

#121
df=pd.DataFrame({'A':[1,1,1,2,3,3,4,5],'B':[1,1,1,3,4,4,5,5,],'C':[1,1,1,1,1,2,3,4],'D':[5,6,7,8,9,1,1,1]})
df.groupby(['A','B']).aggregate(['min','max'])
#      C       D    
#    min max min max
#A B                
#1 1   1   1   5   7
#2 3   1   1   8   8
#3 4   1   2   1   9
#4 5   3   3   1   1
#5 5   4   4   1   1

#125
df = pd.DataFrame([[np.nan, 2, np.nan, 0], [3, 4, np.nan, 1],[np.nan, np.nan, np.nan, 5], [np.nan, 3, np.nan, 4]], columns=list('ABCD'))
df. fillna (0) 
#change nan into 0
df.fillna(method='ffill') 
#propagate non-null values forward 
#fill the nan number with previous number 

#126
values = {'A':0,'B':1,'C':2,'D':3}
df.fillna(value=values)
#Replace all NaN elements in column 'A '. 'B'. 'C' and 'D' with 0, 1, 20, and 3 respectiveLy
#     A    B    C  D
#0  0.0  2.0  2.0  0
#1  3.0  4.0  2.0  1
#2  0.0  1.0  2.0  5
#3  0.0  3.0  2.0  4
df.fillna(value=values, limit=1) 
#0nly replace the first NaN element 
#     A    B    C  D
#0  0.0  2.0  2.0  0
#1  3.0  4.0  NaN  1
#2  NaN  1.0  NaN  5
#3  NaN  3.0  NaN  4
#test: replace limit 2 and then calculate sd
df.fillna(value=values, limit=2).std()

values = {'A':df['A'].mean(),'B':df['B'].mean(),'C':df['C'].mean(),'D':df['D'].mean()}
df.fillna(value=values)
#replace NaN with mean of the column

#129 very offen to use
df = pd.DataFrame({ 'A' : [1,1,2,3,5,6,7,8], 'B' : [1,1,6,7,8,9,10,11]}) 
df.drop_duplicates() 
#Removed row 1 (duplicate) 
df2 = pd.DataFrame({ 'A' : [1,1,1,2,3,4,4,4,3], 'B' : [1,1,2,2,3,3,4,5,5], 'C' : [6,7,2,2,3,3,4,5,5]}) 
df2.drop_duplicates()
df2.drop_duplicates(subset = ['A','B'])
df2.drop_duplicates(subset = ['A','B'],keep = 'last')
#keep last row if duplicate
#   A  B  C
#1  1  1  7
#2  1  2  2
#3  2  2  2
#4  3  3  3
#5  4  3  3
#6  4  4  4
#7  4  5  5
#8  3  5  5
df2.drop_duplicates(subset = ['A','B'],keep = False)
#remove all row if duplicate
#   A  B  C
#2  1  2  2
#3  2  2  2
#4  3  3  3
#5  4  3  3
#6  4  4  4
#7  4  5  5
#8  3  5  5

#135
df = pd.DataFrame({ 'A' : [1, 3, 1, 4, 3],'B' : [3, 1, 4, 2, 2]})
#find unique values in column A 
pd. unique( df. A) 
#array([1, 3, 4])


#136
dt = ['2017-01-05 2:30:00 PM', 'Jan 5, 2017 14:30:00', '01/05/2016', '2017.01.05', '2017/01/05', '20170105'] 
#convert dt to datetime format 
pd. to_datetime ( dt) 
pd. to_datetime ( '10/11/12') 
pd. to_datetime ( '10/11/12', yearfirst=True)
#note that when yearfirst is set to true, the first number in the input is recognized as year
#custome datetime format of the input
pd.to_datetime('2017$01$05')
pd.to_datetime( '2017$01$05' , format='%Y$%m$%d' )
#Test will test the above one
pd.to_datetime( '2017/01/05' , infer_datetime_format=True)  
#handle invalid dates
pd.to_datetime( ['2017-01-05' , 'Jan 6, 2017,'abc'])  
pd.to_datetime( ['2017-01-05' , 'Jan 6, 2017,'abc'], errors = 'ignore')
#note that the input is returned as original
pd.to_datetime(['2017-01-05' , 'Jan 6, 2017' , 'abc' ], errors='coerce' ) 
#note that 1abc1 is returned as 'NaT'

#143 usually use how and on
#145 VERY IMPORTANT on PROJECTS
caller= pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'], 'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})
other =pd.DataFrame({'key': ['K0', 'K1', 'K2'], 'B': ['B0', 'B1', 'B2']})

caller.merge(other, left_on= 'key', right_on= 'key' , how='inner') 
#left_on and right_on: Field names to join 
#inner only keeps the intersection by 'key' 
#orig dataset is left
#inner: only retake if we have data on both key
#https://pandas.pydata.org/pandas-docs/stable/merging.html
#concat is merge vertically
#simple Concatenating code M1: result = pd.concat(frames)
#result = df1.append(df2)
df_combined =pd.DataFrame()
list_df =[]
for i in range(1,4):
    df_name = 'df' + str(i)
    list_df.append(df_name)

for i in range(100):
    df_add = pd.DataFrame('A':['A1','A2','A3','A4'],'B':['B1','B2','B3','B4'],'C':['C1','C2','C3','C4'],'D':['D1','D2','D3','D4'],columns=list('ABCD'))
    df_combined.append(df_add)
    
for i in range(1,4):
    df_name = globals()['df' + str(i)]
    df_combined = df_combined.append(df_name)
#convert string to variables

for i in range(1,4):
    df_name = eval('df' + str(i))
    df_combined = df_combined.append(df_name)
    