# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import pandas as pd
import numpy as np

def myFunction

np.sqrt(a)
np.exp(a)
np.floor(a)
np.sin(7.3)
np.ceil(7.3)
np.maximum(5.1,6.4)
np.minimun(5.1,6.4)

a = np.arange(15).reshape(3,5)
a.sum()
a.sum(axis=0)
a.sum(axis=1)

b=(a%3 ==0)

a.mean(axis=0)
a.mean(axis=1)
a.std(axis=1)
a.std(axis=0)
x=np.arange(50)*2*np.pi/50

np.pi

import matplotlib as mpl
mpl.pyplot.plot(y)
mpl.pyplot.xlabel('index')

x = np.random.rand(200)
y = np.random.rand(200)
size = np.random.rand(200)*30
color = np.random.rand(200)
mpl.pyplot.scatter(x, y, size, color) 
colorbar()

x = np.arange(50)*2*np.pi/50

#Pandas
import pandas as pd
#time series auto regression: Yu=a+bYt-1+e (vertical)
#cross sesstion data: Yi = a+bXi+ei (horizontal)
#panel data: 3 dimentional data: Yit=a+bXit+e
#df = dataframe
df = pd.read_csv("http://rcs.bu.edu/examples/python/data_analysis/Salaries.csv")
#show first 7 observation
df.head(7)
#check the type of data
df['salary'].dtype
df.dtypes
df['salary'].head()
list(df)
len(list(df))
df.columns
df.axis

#slide 88
#number of data
len(df)
#number of columns
len(list(df))
df.dtypes
df.tail()

#slide 89
df.describe()
df.sample

#slide 90
df.describe
df.std()
df.head(50).mean()

#slide 91: df['sex'] = df.sex
#slide 92
df.salary.describe()

df_rank = df.groupby(['rank'])
df_rank = df.groupby(['rank']).mean()

df.groupby('rank')[['salary']].mean()
#                  salary
#rank                    
#AssocProf   91786.230769
#AsstProf    81362.789474
#Prof       123624.804348
df.groupby(['rank','salary']).mean()
#show all the salary of people with separared by rank
df.groupby(['rank'], sort=False)[['salary']].mean()
#sorting is a default of groupby
#                  salary
#rank                    
#Prof       123624.804348
#AssocProf   91786.230769
#AsstProf    81362.789474

#filter
df[df['rank'] == 'AsstProf']
df[(df['rank'] == 'AsstProf') & (df['phd'] >=10) & (df['salary']>10000)]
df[(df['rank'] == 'AsstProf') & ((df['salary']>=90000) | (df['salary']<=80000))]

#slicing
df['salary']
df[['rank','salary','sex']]
df[df['rank'] == 'AsstProf'][df['service']>5]
df['ToPromote'] = (df['rank'] == 'AssProf')

#add new column
df['NewSalary'] = df['salary']/1000

#loc = locate
df.loc[10:20,['rank','sex','salary']]
df.loc[11]
df_sub = df[10:20]
#iloc select row by their row number
df_sub.iloc[8]
df_sub.iloc[[8],[0,3,4,5]]
#    rank  service   sex  salary
#18  Prof        7  Male  107300
df_sub.iloc[6:8,[0,3,4,5]]
#        rank  service   sex  salary
#16  AsstProf        3  Male   75044
#17  AsstProf        0  Male   92000
df.ix[13]