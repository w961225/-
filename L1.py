# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#first_variable = 1
#print (first_variable)
#
#second_variable = first_variable + 1
#print (second_variable)

for i in range(42):
    print("Hello world for the " + str(i) + " time")

f= open('file.txt','w')
    path = "/Users/macbook/Desktop"
    
import os

path = r'/Users/macbook/Desktop'

f = open(path + os.sep + "Hello_World.txt", 'w')
for i in range(42):
    f.write("this is the " + str(i) + " time of saying hello to the world \n")
f.close()

f = open(path + os.sep + "Hello_World_" + str(i) ".txt", 'w')