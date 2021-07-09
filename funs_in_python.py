# -*- coding: utf-8 -*-
"""
Created on Mon May 24 17:01:05 2021

@author: Gouri
"""

num=24
if num%2==0:
    print('the number is even')
else:
    print('the number is odd')
    
#Using functions:
  def even_odd(num):
    if num%2==0:
        print('the number is even')
    else:
        print('the number is odd')
                
even_odd(24)

#print vs return:
def hello_world():
    print('hello_world')
    
val=hello_world()
val
print(val)  #its bcs hello_world() just prints a sentence, deosn't return any value

def hello_world():
    return 'hello_world'

val=hello_world()
val

#Positional and keyword arguements:
def hello(name,age=29):
    print('My name is {} and my age is {}'.format(name,age)) #name is positional argument and age=29 is keyword argument
    
hello('Gouri')
hello('gouri',30)

def hello(name,age):
    print('My name is {} and my age is {}'.format(name,age)) #name and age both are positional arguments
hello('gou',40)

#another way of defining positional and keyword argument:
def hello(*args,**kwargs):
    print(args)
    print(kwargs)
    
hello('gouri','puranik',age=29,dob=1992)
lst=['gouri','puranik']
dict_args={'age':29,'dob':1992}
hello(lst,dict_args)
hello(*lst,**dict_args)

lst=[1,2,3,4,5,6,7,8]
def even_odd(lst):
    even_sum=0
    odd_sum=0
    for i in lst:
        if i%2==0:
            even_sum=even_sum+i
        else:
            odd_sum=odd_sum+i
        
    return even_sum,odd_sum
even_odd(lst)

#Map function in python:
def even_odd(num):
    if num%2==0:
        return 'the number {} is even'.format(num)
    else:
        return 'the number {} is odd'.format(num)

even_odd(6)        

#Map function:
lst=[1,2,3,4,5,6,7,8,9,24,56,78]

list(map(even_odd,lst)) #first parameter is func, sec is iterable


# Lambda function:
# A function with no name:when a function has a single expression like a+b, Lambda function can be used
def addition(a,b):
    return a+b
addition(4,5)

addition=lambda a,b:a+b #a,b are inputs, a+b is action performed and value to be returned 
addition(13,2)

def even(num):
    if num%2==0:
        return True
    
even(20)
even(37)

#Converting above function into lambda function:
even1=lambda a:a%2==0
even1(33)

def addition(x,y,z):
    return x+y+z
addition(5, 7, 3)

addition3=lambda x,y,z:x+y+z
addition3(4,5,6)

#Filter functions in Python:
#its just like map function but used when there is a single expression/operation (num%2==0) to be executed:
def even(num):
    if num%2==0:
        return True
    #else:       #this doesn't throws an error, rather it outputs for only expression
     #   return False
lst=[1,2,3,4,5,6,7,8,9,0]
filter(even,lst) #filter object is created
list(filter(even,lst))

#creating lambda fun and filter for it:
list(filter((lambda n:n%2==0),lst))
list(map((lambda n:n%2==0),lst))

