# -*- coding: utf-8 -*-
"""
Created on Tue May 25 12:57:19 2021

@author: Gouri
"""

lst=[1,2,3,4,5,6,7]
for i in lst:
    print(i)
# here lst is a iterable
lst1=iter(lst) #now lst1 is a iterator. Unless a particular list element is called its not initialised into memory i.e its not stored into memory 
lst1 #only its object is created. we cannot access elements
next(lst1) #In order to see or retrieve list contents one by one next() is used
# when our lists contain millions of data.. its unnecessary to store all the data into memory unless we need to retrieve all of them.
#In such scenario, we can convert lists into iterators and retrive and store elements of list which we want to.
for i in lst1: # when next() is used one time and for is followed by it.. pointer continues value from 1..i.e it takes value 2
    print(i)
# for has builtin StopIteration exception handling unlike in next()
    
# diff btn Iterable and Iterator: Iterable is initialised into memory once it is executed but Iterators are initialised only when they are retrieved separately
    
