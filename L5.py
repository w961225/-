# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#slide 171
def fancyMath(a,b):
    c = a*b+b/(a+b)+b**a
    print(c)
# or   def fancyMath(a=2,b=3):

#183
#lambda (input):(output)
f = lambda x:x+1
f()
f(1)

(lambda z:z*2)(7)

(f = lambda x,y : 2 * x + y)(3,4)

map(lambda x: x+1, [1,2,3,4])
list(map(lambda x: x+1, [1,2,3,4]))
#map(lambda (x,y):(x+2: y+3),{1:2, 3:4})

#188
list_hk_income = [8000, 100000, 140000, 200000, 300000, 7000, 9000]
list(filter(lambda x:x>=100000, list_hk_income))
len(list(filter(lambda x:x>=100000, list_hk_income)))
len(list(filter(lambda x:x>=100000, list_hk_income)))/len(list_hk_income)


#lecture 2 notes

import os
import pandas as pd
data = pd.read_sas(path + os.sep + "trademark_pub.sas7bdat")

import numpy as np
a = np.array([1,2,3,4,5])
a = np.array([1,2,3,4,5,6,7,8,9])
a.reshape(3,3)
type (a)
b = np.array([1,2,3,4,5,6])
b.reshape(2,3)
c = a.reshape(3,3)
c + 10
c*2
list(map(lambda x:x*2,[2,3,4]))
d = np.arange(10)
np.arange(10).reshape(5,2)
np.linspace(0,1,0.2,1)

#34
e = np.arange(10).reshape(5,2)
e[3:4,0]
e[3:5,0]
e[2:4,0]

a = np.arange(15).reshape(3,5)
a[:2,2:3]

a.size
a.itemsize
a.nbytes
b=a.copy()
a[1][1]
a[1][1] = 7
a.fill(2)
a[:]=1
a+10
b = np.arange(5)*2
a = np.arange(15).reshape(3,5)
a+b
