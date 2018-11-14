# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 11:25:34 2018

@author: Frankie Ho
"""

# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Import the numpy package as np
import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)


# Calculate bmi
# numpy numerical computation can handle arrays directly
bmi = np_weight / np_height ** 2

# Print the result
print(bmi)

# Round results to 3 decimal places
bmi_r = np.round(bmi,3)
print(bmi_r)

#How to compute bmi using map in vanila Python?
bmi_2 = list(map(lambda x,y: x/y**2, weight, height))

#Round result to 3 decimal places using map
bmi_2r = list(map(lambda x: round(x,3), bmi_2))
print(bmi_2r)

#Round result to 3 decimal places using list comprehension
bmi_2r = [round(elem,3) for elem in bmi_2]
print(bmi_2r)

#Example using for loop to compute rounded bmi in vanila python
bmi_3r = []
for i in range(len(height)):
    bmi_3r.append(round(weight[i] / height[i] ** 2,3))
print(bmi_3r)

#Numpy gives the simplest code.
#Pandas also work in the same way

# For a boolean response
bmi_r > 25

# Print only those observations above 25 with numpy
filtered_bmi = bmi_r[bmi_r > 25]
print(filtered_bmi)

# Print only those observations above 25 with filter
filtered_bmi_2 = list(filter(lambda x: x > 25,bmi_r))
print(filtered_bmi_2)

#result of numpy and lambda is different as numpy separate number by space but lambda is by ,

#Now print observations above 25 using for loop
filtered_bmi_3 = []
for sample in bmi_r:
    if sample > 25:
        filtered_bmi_3.append(sample)
print(filtered_bmi_3)

#Sorting using numpy
a = np.array([[3,7],[9,1]]) 

print('Our array is:')
print(a) 
print('\n')

#default by acending
print('Applying sort() function:') 
print(np.sort(a))
print('\n') 

#decending order
print('Applying sort() function:') 
print(-np.sort(-a))
print('\n')
  
print('Sort along axis 0:')
print(np.sort(a, axis = 0))
print('\n')  

# Order parameter in sort function 
# as long as name is not larger than 10, then it is ok?
dt = np.dtype([('name', 'U10'),('age', int)]) 
a = np.array([("raju",21),("anil",25),("ravi", 17), ("amar",27)], dtype = dt) 

print('Our array is:')
print(a) 
print('\n')  

print('Order by name:') 
print(np.sort(a, order = 'name'))