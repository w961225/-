# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 16:35:22 2018

@author: Frankie Ho
"""

print("Hello World!")
#What is the fifth letter of "Hello World"?
fifth_letter = "Hello World"[4]
fifth_letter

#String as tuple
wzg = "Wang Zigan"
len(wzg)

str(2)

print("Wang" + "Zigan")
#The following three lines give the same output
print("Wang" + " " + "Zigan")
print("Wang " + "Zigan")
print("Wang","Zigan")

#List
University = ["HKU", "CUHK", "HKUST"]
University[0]
## cant change the variable in tuple() but can change in list[]
University2 = ("HKU", "CUHK", "HKUST")
University2[0]
University2[0] = ("Cityu")

x = 123
type(x)

y = 123.0
type(y)

str(x)
type(str(x))

5/2
#floor division
## one / will generate float number while // will become int number
5//2

# multiply function
## remember to leave 2 space or tab for function / loop / class etc..
def multiply(x):
    return 4 * x
multiply(5)

# same as above with default value 5
def multiply (x = 5):
    return 4 * x
multiply()

b = 2
multiply (b)

multiply (b + 8)
## b will be updated as it is a call function

#get current working directory
import os
os.getcwd()

##change directory
os.chdir("/Users/macbook/Documents/HKU/YR3/sem1")

## window: os.sep = \
## mac: os.sep = \\

os.chdir("C:\\" + os.sep + "macbook" + os.sep + "Documents" + os.sep + "HKU")