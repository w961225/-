# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 00:16:11 2018

@author: Frankie Ho
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Objective, creating dataframe with BRICS countries information
dict_brics = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

brics = pd.DataFrame(dict_brics)
print(brics)


print(brics['area']) #Return series
print(brics['capital'])
print(brics[['country', 'area']]) #Return dataframe


print(brics[0:3]) #Choose first three rows 
print(brics.iloc[0,]) #Choose first row, 
print(brics.iloc[:,0]) #Choose first column
brics.index = ['BR', 'RU', 'IN', 'CH', 'SA'] #Row names 
print(brics)


print(brics.loc['RU']) #Column names
print(brics.loc['RU','area'])

# import csv from websites
df1=pd.read_csv("http://pythonhow.com/wp-content/uploads/2016/01/Income_data.csv")
print(df1)

brics.to_csv('brics.csv')

brics_2 = pd.read_csv('brics.csv')
print(brics_2)

brics_3 = pd.read_csv('brics.csv', index_col = 0)
print(brics_3)

## Basics Statistics with pandas
#Compute percentage change
s = pd.Series([1,2,3,4,5,4])
print(s.pct_change())

#Randomly generate standard normal distributed variables for 5 rows and 2 columns
df = pd.DataFrame(np.random.randn(5, 2)) 
print(df)
print(df.pct_change())

s1 = pd.Series(np.random.randn(10)) #10 Standard normal variables
s2 = pd.Series(np.random.randn(10)) #10 Standard normal variables
print(s1.cov(s2)) #covariance 

#Generate 5 random series with 10 items for each series
frame = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e']) 
print(frame['a'].corr(frame['b'])) #Correlation between series a and series b
print(frame.corr()) #Correlation matrix

#plot s1 series
x = np.arange(0,10) 
y = s1
#Simple Plot
plt.plot(x,y)

#Labeling the Axes and Title
plt.title("Graph Drawing") 
plt.xlabel("Time") 
plt.ylabel("Distance") 
#Simple Plot
plt.plot(x,y)

# Formatting the line colors
plt.plot(x,y,'r') #red colour

# Formatting the line type  
plt.plot(x,y,'>') #triangle as dots