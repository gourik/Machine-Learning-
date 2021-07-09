# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 22:58:39 2021

@author: Gouri
"""

#Boolean variables:
#These are two constant objects Truth and False. These are used to represent truth values.
# In numeric contexts(i.e when used as an arguement to arithmetic operator),they behave like
#integers 0 and 1 rsply.
#Builtin func bool() can be used to cast any value to a Boolean, if the value can be 
#interpreted as truth value. They are written as False and True rsply.
print(True,False)
type(True)
type(False)
my_string1='hello'
print(my_string1.isalnum())
my_string2='hellO1234'
print(my_string2.isalnum())
print(my_string2.istitle()) #tests if string contains Title words i.e word starting with Capital letter
print(my_string1.isdigit())
print(my_string2.isupper())
print(my_string1.islower())
print(my_string1.isalpha())
print(my_string1.isnum())
print(my_string1.isspace())
print(my_string1.startswith('h'))
print(my_string1.endswith('o'))

#Boolean and Logical operators:
my_string1.isalpha() or my_string1.isnum()

#Lists:
#It is a data structure which is mutable, ordered sequence of elements. Each element or value that is inside 
# of a list is called an item.
type([])
list_ex=[]
type(list_ex)

lst=list()
type(lst)

list1=['Mathematics','Science',100,200,300,400] # comma seperated values and there can be differt types of data elements
type(list1)
len(list1)
#Append:
list1.append('500')
list1
list1[1:]#from index 1 to all are selected
list1[1:6]#from 1 to 6 are picked up
list1.append(['John','Bala'])
list1
list1.insert(1,'Naik')
list1

#extend():
lst=[1,2,3,4,5,6]
lst.extend([8,9])
lst

#sum()
sum(lst)

#pop():
lst.pop() #it removes last element
lst
lst.pop(0) #pops 1st element
lst

#count():calculates total no. of occurences of given element of list
lst.count(1)

#len():calculates total length of a list:
len(lst)

#index(): returns the index of first occurence. first and end indexes are not necessary parameters:
lst.index(2,0,4)# 1 is to be searched for index ...0 is start index and 4 is stop index to stop the search

#min() and max():
min(lst)

#multiplication:
lst*2 # entire list is multiplied
