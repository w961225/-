# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
a_string = "This is Frankie"
##slide 57

if "f" in a_string:
    print("Found a f!)
    
"f" in a_string
## this only return true or false

for element in a_string:
    print(element)
    
#slide62-
a_string[2]
a_string[2:5]
b_string = "abcdefghijklmn"
b_string[2:5]
#"cde"
b_string[2:-1]
#"cdefghijklm"
b_string[2:]
#"cdefghijklmn"
b_string[:-1]
#"abcdefghijklm"
b_string[2:2]
#""
c_string = b_string[2:-2]
c_string

#slide 77-82
a_list = ["wang",1,2.5,[2,3.5,"frankie"]]
a_list[3][1]
#3.5
len(a_list)
#4
for element in a_list:
    print(element)
    
a_list[-1]
a_list[0] = a_list[0].upper()
a_list

a_list = ['a','b','c','d']
b_list = [1,2,3,4,5]
a_list.append(b_list)
# ['wang', 1, 2.5, [2, 3.5, 'frankie'], [1, 2, 3, 4, 5]]
a_list.extend(b_list)
#['wang', 1, 2.5, [2, 3.5, 'frankie'],  1, 2, 3, 4, 5]

#b_list.extend(a_list) to make b_list at 1st position
a_list[:2] + b_list[:2]+a_list[3:] + b_list[3:]

d_list = [1,2,3,4,5,"WANG",2,2.5,1,2,3,4,5]
list(set(d_list))

len(list(set(d_list)))
c_list = []
for i in range(len(a_list)):
    c_list.append([a_list[i]])
    c_list.append([b_list[i]])
    
c_list = []
for i in range(len(a_list)):
    c_list.append(a_list[i])
    c_list.append(b_list[i])
c_list.extend(b_list[len(a_list):])
c_list

#slide 65-67
a_tuple = (1,2,3,4,5)
a_tuple[0]
a_tuple[0] = 2
#this becomes error as it cannot be changed

b_tuple = (9)
#this is not tuple

b_tuple = (9,)
#this is tuple 

a_tuple[2:4]
#(3,4)
a_tuple[2:3]
#(3,)
a_tuple[2:2]
#()
a_tuple[2]
#(3)

#slide68
a_tuple = (11,22)
b_tuple = a_tuple
b_tuple
#(11,22)
a_tuple+=(33,44)
a_tuple
#(11,22,33,44)
b_tuple
#(11,22)

a_list = [11,22]
b_list = a_list
b_list
#[33,22]
a_list[0]=33
a_list
#[33,22]
b_list  
#[33,22]

b_list = a_list[:]
#in this case b_list wont change

#slide69-72
a_tuple = (33,22)
a_tuple.sort()
# this will give error as tuple can be changed
sorted(a_tuple)
#this will change to list, so
tuple(sorted(a_tuple))

f_string = "FRANKIE"
list(f_string)
#['F', 'R', 'A', 'N', 'K', 'I', 'E']
i for i in f_string
#['F', 'R', 'A', 'N', 'K', 'I', 'E']
tuple(f_string)

#slide73
def area_volume_of_cube(sideLength):
    area = 6 * sideLength*sideLength
    volume = sideLength*sideLength*sideLength
    return area, volume
#the return is a tuple as it has ,
    
area_volume_of_cube(4)
#(96,64)
area_4 = area_volume_of_cube(4)[0]
area_4
#96

(a,b) = (4,5)
b
#5
a
#4
c=b
b=a
a=c
#a=2, b=1
a,b = b,a
#a=1, b=2

#slide76
[1,2] < [2,3]
#compare first element first to see if it is true or not
#if same, then look for second element
("Jones", "Sally") > ("Adams", "Sam")
#true
#small letter is larger than capital letter

#slide83
a_dict = {1:'A',2:'B'}
a_dict[0]
#this is error as there is no sequence

a_dict[1]
#'A'
for key, value in a_dict.item():
    print(key,value)
#1 A
#2 B
    
#dict is good for storing tree data
class_dict = {"Jun":{"gender":"male", "age":23,"nationality":"korean"},"Alice":{"gender":"female","age":30,"nationality":"american"}}
class_dict["Jun"]
#{'gender': 'male', 'age': 23, 'nationality': 'korean'}
class_dict["Jun"]["age"]
#23
len(class_dict)
#2
#show number of key

age_list=[]
for info_dict in class_dict.values():
    age_list.append(info_dict["age"])
age_list
#[23,30]

import pandas as pd
.pickle

ord("a")
#97
ord("A")
#65

#keys cannot change so that it cannot be a list

#slide 93
age["Bob"] = 37

#slide 110
#aset[0] is error
#| can only be used in set