#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 14:15:54 2018

@author: olivia
"""

# ％ provides the remainder
# immutable: cannot change the data inside once you created it.
# Strings: "" (immutable, ordered)
# Tuples: () (immutable, ordered)
# Lists: [] (mutable)
# Dictionaries: {} (mutable)

len() #find out the length of a sequence
myStrings[0,5] #Produce from 0-4 but not 5

String_a = "All lowercase."

myList = ['l', 'o', 'w', 'e', r', c', 'a', 's', 'e']
myList[0] = 'L'

# append and extend
myList = [ True, 'Boo', 3]
myList.append([5,6])
myList.extend([5,6])

#Dictionary
arabic2roman = {1:"I", 2:"II", 3:"III", 4:"IV", 5:"V"}
arabic2roman[1] # find out the corresponding answer for 1
arabic2roman.get(500, "None") # return 500, if dun have that value then return 'None'

#Displaying Contents
age = {'Alice' : 25, 'Carol' : 'twenty-two'}
age.items()
age.keys()
age.values()

# Updating directories
age.update({'Bob' : 29}) # add a now content into the dict
age.update({'Carol' : 23}) # update the value stored

# Returning a value
age.get('Bob')
age['Bob']

# Removing a specific item
age.pop('Carol')

# Removing a random item
age.popitem()

#Set
# Duplicates are eliminated, Immutable, no order
cset = {11,11,22}

aset = {11,22,33}
bset = {12,23,33}

aset | bset # Union of two sets
aset & bset # Intersection of two sets
aset - bset # Difference, ie. elements that contains in aset but not in bset
aset ^ bset # Symmetric difference

######### FOR ALL the DATA TYPE CONVERSION, refer to Lecture 1 Slide p.119

x = 4
if x > 2: # two-way
    print('Bigger')
else:
    print('Smaller')
print('All done')

if x < 2: # Multi-way
    print('Small')
elif x < 10:
    print('Medium')
else:
    print('LARGE')
print('All Done')

range(5) #returns range(0,5) (a range object)
list(range(5)) # returns [0,1,2,3,4,] (a list)
for x in range(5):
    print(x)
    
# For Loops and Dictionaries
ages = {"Sam": 4, "Mary": 3, "Bill": 2}
for name in ages.keys():
    print(name, ages[name])
    
# Creating a New Function
def functionName(arguments):
    
    
# Import Python Libraries
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mpl
import seaborn as sns

a = np.array([1,2,3,4,5,6,7,8,9])
b = a.reshape((3,3)) 
# reshape(x,y,z) x = row, y = column, z = no. of sheet

np.array([1,2,3,4]) # Explicitly from a list of values
np.arange(10) # As a range of values
np.linspace(0, 1, 5) # from 0 to 1, having 5 elements in total
np.zeros((2,2)) # Zero-initialized
np.ones((1,5)) #One-initialized
np.eye(3) #Constant diagonal value (3 = having a 3*3 diagonal)
np.diag([1,2,3,4]) #Multiple diagonal values (showling a diagonal with those value)

#Indexing and Slicing
arr[0:2,:] # 1-2 row,but no third row, all values
arr[2,1:] #only third row, from the second value till the end

a.ndim #dimension
a.shape 
a.size
a.T #Transpose
a.dtype
a.tolist() #converting a numpy array to a python list
a.fill(0) #set all values in an array

# Mathematic Binary Operators
a = np.array([1,2])
b = np.array([3,4])

a + b
np.add(a,b) #both mean adding a and b tgt

c = np.array(((1,2,3,4), (2,3,4,5)))
d = np.array(((1,2,5,4), (1,3,4,5)))
c == d
Out array([[ True,  True, False,  True],
       [False,  True,  True,  True]])
    
#Axis
c.sum() #adding all the cell tgt
c.sum(axis=0) #adding the cells from top to down
    array([3, 5, 7, 9])
c.sum(axis=1) # add the cells from left to right
    array([10, 14])
    
### Summary of array attributes/methods (p.69-72)
    
# Reading data using pandas
df = pd.read_csv("http://rcs.bu.edu/examples/python/data_analysis/Salaries.csv")

# if single brackets are used to specify the column, then the output is Pandas series objects.
# when double brackets are used the output is a Data Frame.