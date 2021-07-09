# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 14:24:11 2021

@author: Gouri
"""

#Python OOPS Inheritance:
#All variables are public...and its a car's blueprint
class Car():
    def __init__(self,windows,doors,enginetype):#initialisation constructor
        self.windows=windows
        self.doors=doors
        self.enginetype=enginetype
    def drive(self):
        print('The person drives the Car')
dir(Car)
car=Car(4,4,'Diesel')
dir(car)
car.windows
car.enginetype
car.drive()

class audi(Car):
    def __init__(self,windows,doors,enginetype,enableai):
        super().__init__(windows,doors,enginetype)
        self.enableai=enableai
    def selfdriving(self):
        print('Audi sipports self driving')
        
audiQ7=audi(4,4,'diesel',True)
audiQ7.selfdriving()
type(audiQ7.enableai)
audiQ7.drive()
