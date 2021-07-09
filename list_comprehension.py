# -*- coding: utf-8 -*-
"""
Created on Tue May 25 11:46:14 2021

@author: Gouri
"""

#List comprehension provides a concise way to create lists. It contains brackects which consist of 
# an expression followed by a for clause, then zero or more for or if clauses. The expressions can be 
# anything i.e we can add any objects in to lists.
list1=[]
def lst_square(lst):
    for i in lst:
        list1.append(i*i)
    return list1

lst_square([1,2,3,5,6,8])

#list comprehension:first parameter is:expression want to be returned and next is for clause:
lst=[1,2,3,5,6,8]
[i*i for i in lst]

#if we want to square only even numbers:
[i*i for i in lst if i%2==0]

#if we want to square only odd numbers:
[i*i for i in lst if i%2!=0]
