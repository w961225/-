# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 11:12:38 2018

@author: user
"""

def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return

# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")

#Pass by reference
# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print ("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print ("Values outside the function: ", mylist)

#What happen if you use mylist.extend instead of mylist.append?
#append: [10, 20, 30, [1, 2, 3, 4]]
#extend: [10, 20, 30, 1, 2, 3, 4]

# Function definition is here
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print ("Values inside the function: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme( mylist );
print ("Values outside the function: ", mylist)
# Different output compared to the case above! Why? 

# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return;

# Lambda function, Function definition is here
sum = lambda arg1, arg2: arg1 + arg2; #Only one expression is allowed
# once defined valuables in lambda, it cannot be used in other for whole code

# Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))


sequence = list(map(lambda x: x**2, [0,1,2,3,4]))
sequence = list(map(lambda x: x**2, range(5)))
#it must be a list
#Out: [0, 1, 4, 9, 16]

#Exception handling
try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
   fh.close()
   
import os
os.getcwd()
   
try:
   fh = open("testfile", "r")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
# it will show error as "r" is read only

# Define a function here.
def temp_convert(var):
   try:
      return int(var)
   except ValueError as e:
      print ("The argument does not contain numbers\n", e)
#type e to print default error message

# Call above function here.
temp_convert("xyz");
temp_convert("820")
