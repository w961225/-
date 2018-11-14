#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 13:53:09 2018

@author: olivia
"""
rawstr = input('Enter a positive number:')
try: 
    ival + int(rawstr)
except:
    ival = -1
    
if ival > 0 :
    print('Nice work')
else:
    print('Not a positive number')

if True:
    print(5)
    
if False:
    print(5)
else:
    print(6)
    
for x in range(5):
    if x < 3:
        print("the value of x is " + str(x))
        print("x smaller than 3")
    elif x == 3:
        print("the value of x is " + str(x))
        print("x is equal to 3")
    else:
        print("the value of x is " + str(x))
        print("x greater than 3")
        print("\n\n")
        
        
"wzg" in ["wzg","Frankie"]
name_list = 
for x in range(5):
    if x < 3:
        print("the value of x is " + str(x))
        print("x smaller than 3")
    elif x == 3:
        print("the value of x is " + str(x))
        print("x is equal to 3")
    else:
        print("the value of x is " + str(x))
        print("x greater than 3")
        print(\n\n)
for x in range(5):
    if x < 3:
        print("the value of x is " + str(x))
        print("x smaller than 3")
    elif x == 3:
        print("the value of x is " + str(x))
        print("x is equal to 3")
    else:
        print("the value of x is " + str(x))
        print("x greater than 3")
        print("\n\n")
        
counter = 1
i = 1
import time
counter = 0
while(counter >= 0):
    print(counter)
    counter = counter + 1
    if counter%3 == 0:
        continue
    time.sleep(3)
    
number_list = [1,2,3,4,5,6,7,8,9, '10', 11,12,13,14,15,16]
for number in number_list:
    print(number + 1)
    
for number in number_list:
    try:
        print(number + 1)
    except:
        print("something is wrong")
        
for number in number_list:
    try:
        print(number + 1)
    except Exception as e: print(e)