# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 11:01:41 2018

@author: Frankie Ho
"""

#Objective: understanding date and time in Python

import datetime as dt
x = dt.date(1993, 12, 14)
print(x)

#type:datetime.date, and there are also time object

print(dt.date.min)
print(dt.date.max)

#By default, date order is y-m-d

x.toordinal()
#returns the proleptic Gregorian ordinal, where day 1 is 1582-01-01. Current calandar system was introduced in 1582

dt.date.fromordinal(727911)
dt.date.today()

print(x.day)
print(x.month)
print(x.year)


t = dt.time(15, 6, 23)
#order: hour, minute, second, time zone
print(t)

t.hour, t.minute, t.second

t = t.replace(hour=11, minute=59) 

print(t)

t = dt.datetime(2017, 4, 19, 16, 31, 0)
#order is year, month, day, hour, minute, second
print(t)

#Difference between time
delta = dt.datetime(1993, 12, 14) - dt.datetime(1991, 4, 30)
print(delta)
print(type(delta))
#class 'datetime.timedelta' = difference of two days
print(delta.days)

t1 = dt.datetime(2017, 1, 31, 14, 17)
t2 = dt.datetime(2015, 12, 15, 16, 59)
delta = t1 - t2
delta
# datetime.timedelta(412, 76680)[days, second]
print(delta)
delta.days, delta.seconds


#midterm: import and transformation
#BELOW WILL APPEAR IN MID-TERM
#https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

str(t1) #Convert datetime object to string

today = dt.date.today()
#must define today first by dt.date.today()
print(today.strftime('%Y-%m-%d')) #Convert datetime object to string with specified format. Here is yyyy-mm-dd
#lower case in Y will show in short form
print(today.strftime('%y-%m-%d'))
print(today.strftime('%d/%m/%Y'))
print("weekday: " + today.strftime('%a'))
print("weekday as a full name: " + today.strftime('%A'))
# Weekday as a decimal number, where 0 is Sunday 
# and 6 is Saturday
print("weekday as a decimal number: " + today.strftime('%w'))
print("weekday as a decimal number: " + today.strftime('%W'))
# capital letter W is the week tor the whole year

#trim 0
print(today.strftime('%d/%m/%Y').lstrip('0'))


# Day of the month as a zero-padded decimal number. 
# 01, 02, ..., 31
print(today.strftime('%d'))
# Month as locale’s abbreviated name. 
# Jan, Feb, ..., Dec (en_US); 
print(today.strftime('%b'))
# Month as locale’s full name. 	
# January, February, ..., December (en_US);
print(today.strftime('%B'))
# Month as a zero-padded decimal number. 
# 01, 02, ..., 12
print(today.strftime('%m'))


#Convert string to datetime object
#Strptime function takes two parameters(string, date format)
t = dt.datetime.strptime("30 Nov 00", "%d %b %y")
#must match with the % form and separater (ie /, -)
print(t)
d = dt.datetime.strptime("16/07/18", "%d/%m/%y")
print(d)
d = dt.datetime.strptime("16/07/2018", "%d/%m/%Y")
print(d)
print(d.strftime('%y-%m-%d'))