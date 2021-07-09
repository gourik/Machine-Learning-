# -*- coding: utf-8 -*-
"""
Created on Tue May 25 14:34:00 2021

@author: Gouri
"""

class Car:
    pass  # empty class..but its a bad way to create a class

car1=Car()
car1
car1.windows=5     #attributes of Car class
car1.doors=4
print(car1.windows)

car2=Car()
car2.windows=3
car2.doors=2
print(car2.windows)
car2.engine_type='petrol'
print(car2.engine_type)

dir(car1)

# good way of creating class in python:
class Car:
    def __init__(self,window,door,enginetype):
        self.windows=window
        self.doors=door
        self.engine_type=enginetype
        
car1=Car(4,5,'Petrol')
print(car1.windows)
car2=Car(3,4,'Diesel')
print(car2.engine_type)

#adding another method to class:
class Car:
    def __init__(self,window,door,enginetype):
        self.windows=window
        self.doors=door
        self.engine_type=enginetype
    def self_driving(self):  #self indicates inbuilt attributes are accessed in this particular method
        return 'this is a {} Car'.format(self.engine_type)
car3=Car(3,4,'Petrol')    
car3.self_driving()
