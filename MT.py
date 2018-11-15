#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 23:21:38 2018

@author: olivia
"""

# Python list and dictionary
# Python lambda functions
# Numpy mathematical functions 
# Pandas dataframe
df = pd.DataFrame([[np.nan, 2, np.nan, 0], [3,4, np.nan, 1], [np.nan, np.nan, np.nan, 5]], columns=list('ABCD'))
     A    B   C  D
0  NaN  2.0 NaN  0
1  3.0  4.0 NaN  1
2  NaN  NaN NaN  5
# Pandas concat
    #https://pandas.pydata.org/pandas-docs/stable/generated/pandas.concat.html
s1 = pd.Series(['a','b'])
s2 = pd.Series(['c','d'])

pd.concat([s1,s2])
Out[38]: 
0    a
1    b
0    c
1    d
dtype: object

pd.concat([s1,s2], axis = 1)
Out[39]: 
   0  1
0  a  c
1  b  d

pd.concat([s1,s2], ignore_index = True) # assign new index values
Out[40]: 
0    a
1    b
2    c
3    d
dtype: object

pd.concat([s1,s2], keys=['s1', 's2']) # set keys to construct hierarchical index as the outermost level
Out[41]: 
s1  0    a
    1    b
s2  0    c
    1    d
dtype: object

pd.concat([s1,s2], keys=['s1','s2'], names=['Series name', 'Row ID'])
Out[42]: 
Series name  Row ID
s1           0         a
             1         b
s2           0         c
             1         d
dtype: object

s3 = pd.Series([1,2,3], index=['a','b','c'])

s3
Out[44]: 
a    1
b    2
c    3
dtype: int64

s4 = pd.Series([5,6,7], index=['a','c','d'])

s4
Out[46]: 
a    5
c    6
d    7
dtype: int64

pd.concat([s3,s4], axis=1)
Out[47]: 
     0    1
a  1.0  5.0
b  2.0  NaN
c  3.0  6.0
d  NaN  7.0

pd.concat([s3,s4], axis=1, join_axes=[['a','b','c']])
Out[48]: 
   0    1
a  1  5.0
b  2  NaN
c  3  6.0

df1 = pd.DataFrame([['a',1],['b',2]], columns=['letter', 'number'])

df1
Out[50]: 
  letter  number
0      a       1
1      b       2

df2 = pd.DataFrame([['c',3],['d',4]], columns=['letter', 'number'])

df2
Out[52]: 
  letter  number
0      c       3
1      d       4

pd.concat([df1,df2], ignore_index=True)
Out[55]: 
  letter  number
0      a       1
1      b       2
2      c       3
3      d       4

new_df = pd.concat([df1,df2], axis=1, keys=['lv1','lv2'], names=['upper','lower'], levels=[['lv1','lv2','lv3']])

new_df
Out[57]: 
upper    lv1           lv2       
lower letter number letter number
0          a      1      c      3
1          b      2      d      4

df3 = pd.DataFrame([['c',3,'cat'],['d',4,'dog']], columns = ['letter', 'number', 'animal'])

df3
Out[60]: 
  letter  number animal
0      c       3    cat
1      d       4    dog

pd.concat([df1,df2,df3])
Out[61]: 
  animal letter  number
0    NaN      a       1
1    NaN      b       2
0    NaN      c       3
1    NaN      d       4
0    cat      c       3
1    dog      d       4

pd.concat([df1,df2,df3], join='inner') # Column with NaN entries are excluded when join='inner'
Out[63]: 
  letter  number
0      a       1
1      b       2
0      c       3
1      d       4
0      c       3
1      d       4
# Pandas merge
    #https://pandas.pydata.org/pandas-docs/stable/merging.html
df1 = pd.DataFrame({"city":["new york", "chicago", "orlando", "baltimore"], "temperature": [21,14,35,38]})

df1
Out[78]: 
        city  temperature
0   new york           21
1    chicago           14
2    orlando           35
3  baltimore           38

df2 = pd.DataFrame({"city": ["chicago", "new york", "san diego"], "humidity": [65,68,71]})
df2
Out[74]: 
        city  humidity
0    chicago        65
1   new york        68
2  san diego        71

df3 = pd.merge(df1,df2, on="city", how="inner")

df3
Out[80]: 
       city  temperature  humidity
0  new york           21        68
1   chicago           14        65

df3 = pd.merge(df1,df2, on="city", how="outer")

df3
Out[82]: 
        city  temperature  humidity
0   new york         21.0      68.0
1    chicago         14.0      65.0
2    orlando         35.0       NaN
3  baltimore         38.0       NaN
4  san diego          NaN      71.0

df3 = pd.merge(df1,df2, on="city", how="right") # merge the two dataframes using the cities in df2

df3
Out[84]: 
        city  temperature  humidity
0   new york         21.0        68
1    chicago         14.0        65
2  san diego          NaN        71

df3 = pd.merge(df1, df2, on="city", how="outer", indicator = True) #add a column showing the sources of each row

df3
Out[86]: 
        city  temperature  humidity      _merge
0   new york         21.0      68.0        both
1    chicago         14.0      65.0        both
2    orlando         35.0       NaN   left_only
3  baltimore         38.0       NaN   left_only
4  san diego          NaN      71.0  right_only

df3 = pd.merge(df1, df2, left_on="city", right_on="city", how = "outer", indicator=True) #se the "left_on" & "right_on" to replace "on"

df3
Out[88]: 
        city  temperature  humidity      _merge
0   new york         21.0      68.0        both
1    chicago         14.0      65.0        both
2    orlando         35.0       NaN   left_only
3  baltimore         38.0       NaN   left_only
4  san diego          NaN      71.0  right_only

df1 = pd.DataFrame({"city":["new york", "chicago", "orlando", "baltimore"], "humidity":[65,68,71,75], "temperature":[21,14,35,38]})

df1
Out[90]: 
        city  humidity  temperature
0   new york        65           21
1    chicago        68           14
2    orlando        71           35
3  baltimore        75           38

df2 = pd.DataFrame({"city": ["chicago", "new york", "san diego"], "humidity": [65,68,71], "temperature": [21,14,35]})

df2
Out[92]: 
        city  humidity  temperature
0    chicago        65           21
1   new york        68           14
2  san diego        71           35

df3 = pd.merge(df1, df2, on="city", how="outer", suffixes=('_first','_second'))

df3
Out[94]: 
        city         ...          temperature_second
0   new york         ...                        14.0
1    chicago         ...                        21.0
2    orlando         ...                         NaN
3  baltimore         ...                         NaN
4  san diego         ...                        35.0

[5 rows x 5 columns]
# Pandas dropna, fillna
    # https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.dropna.html
df.dropna() # Drop missing observations
df.dropna(how='all') # Drop observations where all cells in NA
df.dropna(axis=1, how='all') # Drop column if all the values are missing
df.dropna(thresh = 5) # Drop rows that contain less than 5 non-minssing values
df.fillna(0) # Replace missing values with zeros
df.isnull() # returns True if the value is missing
df.notnull() # returns True for non-missing values

df = pd.read.cvs("http") # read a dataset 
df[df.isnull().any(axis=1)].head() # Select the rows that have at least one missing value

df.dropna(axis=1, how='all') # drop the column only if all column values are NaN
df.dropna(axis=1, how='any') # drop the column if at lease one NaN cell
df.dropna(thresh=2) # Keep only the rows with at least 2 non-na values

# Pandas slicing, loc, iloc （subset the Data Frame)
df['salary']
df[['rank','salary]]
df[10:20]

#loc (select a range of rows, using their labels)
df.sub.loc[10:20,['rank','sex','salary']]

#iloc (select a range of row and/columns, using their positions)
df_sub.iloc[10:20,[0,3,4,5]]
    
# Pandas filtering
df_sub=df[df['salary']>120000]
# Pandas read_csv / to_csv
df = pd.read_cvs("http")
# Pandas drop_duplicates
  #https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.drop_duplicates.html
df = pd.DataFrame({'A': [1,1,2,3,5,6,7,8],'B': [1,1,6,7,8,9,10,11]})

df
Out[26]: 
   A   B
0  1   1
1  1   1
2  2   6
3  3   7
4  5   8
5  6   9
6  7  10
7  8  11

df.drop_duplicates() #()= using all by default elements
Out[27]: 
   A   B
0  1   1
2  2   6
3  3   7
4  5   8
5  6   9
6  7  10
7  8  11
# Pandas groupby
df_rank = df.groupby(['rank'])

df_rank.mean()
Out[101]: 
                 phd    service         salary
rank                                          
AssocProf  15.076923  11.307692   91786.230769
AsstProf    5.052632   2.210526   81362.789474
Prof       27.065217  21.413043  123624.804348

df.groupby('rank')[['salary']].mean() # cal mean salary for each professor rank
Out[102]: 
                  salary
rank                    
AssocProf   91786.230769
AsstProf    81362.789474
Prof       123624.804348
# Pandas apply
    #https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.apply.html
# Pandas sort_values
df_sorted = df.sort_values(by='service')
df_sorted = df.sort_values(by='service','salary'], ascending=[True,False])
# Pandas to_datetime (convert argument to datetime)
    #https://pandas.pydata.org/pandas-docs/stable/generated/pandas.to_datetime.html
    dt = ['2017-01-05 2:30:00 PM', 'Jan 5, 2017 14:30:00', '01/05/2016', '2017.01.05', '2017/01/05', '20170105']
    pd.to_datetime(dt)
   Out[32]: 
DatetimeIndex(['2017-01-05 14:30:00', '2017-01-05 14:30:00',
               '2016-01-05 00:00:00', '2017-01-05 00:00:00',
               '2017-01-05 00:00:00', '2017-01-05 00:00:00'],
              dtype='datetime64[ns]', freq=None)
# Datetime strptime
