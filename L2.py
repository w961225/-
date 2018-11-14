# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import pandas as pd
import numpy as np

def myFunction(a = 5, b = 4):
    if a < 10:
        print(b,a)
    c = a*b*b
    return c

# small letter for variable name
# capital letter for class name
   
#def function
def square(a = 5):
    c = a*a
    return c

# loop function
for i in range(10):
    if i > 5:
        i = i + 1
        print(i)
    else:
        print(i)
        
        
# use of %
"I eat %d shit" % 0

for name in ["shit", "shits", "shitssss"]:
    print ("I eat %s" %name)
    
#https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting
    
  
#type
"I eat " + str(1) + " shit"
bool("0")
#bool--> true or false only

def area(pi=3.14, r):
    a = pi *r*r
    return a
area (r=10)

#create a txt file
path = r'/Users/macbook/Documents/HKU/YR3/sem1/FINA2390 Financial Programming and Databases'
import os
f = open(path + os.sep + 'helloworld.txt', 'w')
f.write("Hello World")
f.close

#w = write
#a = append
f.write("Hello World \n" *100)

# list, tuple, string, dictionary
a_list = [1,2]
b_list = a_list
a_list[1] = 3
b_list
#a_list = [1,2]

a_tuple = (1,2)
b_tuple = a_tuple
b_tuple[1] = 3
b_tuple
#a_tuple = (1,2)
#add variable in existing tuple must be in format of (xx,)
#no direct sort function, only can use "variable = sorted (x)"

a_string = 'Frankie'
a_string[1]

#string and tuple are immutable (cannot change
a_dict = {1:'A', 2:'B'}
for key, value in a_dict.items():
    print (key, value)
    
for key in a_dict.keys():
    print (a_dict[key])

a_dict[1]
#this will give 'A' (performing search function)

#string
a_string
for i in range(len(a_string)):
    print (a_string[i])
for i in a_string:
    print (i)
a_string [-1]
#-1 = count from tbe back (i.e."e")

#.lower = lower case
#.upper = upper case