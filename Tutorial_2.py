# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 10:01:43 2018

@author: user
"""
# Dictionary usage

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # update existing entry
dict['School'] = "DPS School" # Add new entry

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])


#Dictionary keys are unordered
dict.keys
dict.keys[0] #Error!
dict['Age']

#Key must be immutable
dict = {['Name']: 'Zara', 'Age': 7, 'Class': 'First'} #Error

dict.pop('Name') #Remove entry 'Name'
dict['sex'] = female #add new key and value
dict.clear() #Clear all entries
del dict #Remove variable dict alltogether

webster = {
    "Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

for key in webster:
    print (webster[key])
    
    
#Another loop example
for letter in 'Python':     # traversal of a string sequence
   print ('Current Letter :', letter)
print()
fruits = ['banana', 'apple',  'mango']

for fruit in fruits:        # traversal of List sequence
   print ('Current fruit :', fruit)

print ("Good bye!")




#Loop through indexes for above example
for index in range(len('Python')):     # traversal of a string sequence
   print ('Current Letter :', 'Python'[index])
print()
fruits = ['banana', 'apple',  'mango']

for index in range(len(fruits)):        # traversal of List sequence
   print ('Current fruit :', fruits[index])

print ("Good bye!")


#Using for loop, find whether the list contains an even number
numbers = [11,33,55,39,55,75,37,21,23,41,13]

for num in numbers:
   if num%2 == 0:
      print ('the list contains an even number')
      break
else:
   print ('the list doesnot contain even number')