# -*- coding: utf-8 -*-
"""
Created on Tue May 25 12:32:31 2021

@author: Gouri
"""

print('Hello everyone')
strs='Hello'

def greeting(name):
    return 'Hello {} Welcome to community'.format(name)
greeting('Gouri')

def welcome_email(name,age):
    return 'Welcome {}. Your age is {}'.format(name,age)

welcome_email('Gouri',29)
welcome_email(29,'Gouri') #Sentence is meaningless

def welcome_email(name,age):
    return 'Welcome {name}. Your age is {age}'.format(age=age,name=name) #now order doesn't matter
welcome_email('Gouri',29)


