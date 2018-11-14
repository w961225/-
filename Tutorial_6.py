# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:20:41 2018

@author: frank
"""

#url: https://jakevdp.github.io/PythonDataScienceHandbook/03.06-concat-and-append.html
#url: https://jakevdp.github.io/PythonDataScienceHandbook/03.07-merge-and-join.html

import pandas as pd

def make_df(cols, ind):
    #Quickly make a DataFrame
    data = {c: [str(c) + str(i) for i in ind]
            for c in cols}
    return pd.DataFrame(data, ind)


def display(*args):
    #print objects with two newlines separating two objects
    print(*args, sep='\n\n', end='\n\n')
    
# example DataFrame
make_df('ABC', range(3))
        
# Simple Concatenation with pd.concat
ser1 = pd.Series(['A', 'B', 'C'], index=[1, 2, 3])
ser2 = pd.Series(['D', 'E', 'F'], index=[4, 5, 6])
display(ser1,ser2,pd.concat([ser1,ser2]))

#Concatenate dataframes
df1 = make_df('AB', [1, 2])
df2 = make_df('AB', [3, 4])
display(df1,df2,pd.concat([df1,df2]))

#dataframes concatenated along columns 
df3 = make_df('AB', [0, 1])
df4 = make_df('CD', [0, 1])
display(df3,df4,pd.concat([df3,df4],axis=1))

x = make_df('AB', [0, 1])
y = make_df('AB', [2, 3])
y.index = x.index  # make duplicate indices!
#By default, index is not rearranged for pd.concat 
display(x,y,pd.concat([x,y]))


#Rearrange index in concatenated dataframe
display(x,y,pd.concat([x,y],ignore_index=True))

df5 = make_df('ABC', [1, 2])
df6 = make_df('BCD', [3, 4])

display(df5,df6,pd.concat([df5,df6],sort=False)) #join='outer', columns not sorted

display(df5,df6,pd.concat([df5,df6],sort=True)) #columns sorted

display(df5,df6,pd.concat([df5,df6],join='inner')) #Only shows columns that are intersection of both input dataframes

display(df5,df6,pd.concat([df5, df6],join_axes=[df5.columns])) #shows columns in df5

#Append method having less words to write function
display(df1,df2,df1.append(df2))

#Concat is more efficient then append in Pandas

df7 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df8 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
                    'hire_date': [2004, 2008, 2012, 2014]})
display(df7, df8, pd.merge(df7,df8))

df9 = pd.merge(df7,df8)
df10 = pd.DataFrame({'group': ['Accounting', 'Engineering', 'HR'],
                    'supervisor': ['Carly', 'Guido', 'Steve']})
display(df9, df10, pd.merge(df9, df10)) #Many to one joins

display(df7, df8, pd.merge(df7, df8, on='employee'))