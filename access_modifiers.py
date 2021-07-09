# -*- coding: utf-8 -*-
"""
Created on Mon May 31 17:41:31 2021

@author: Gouri
"""

#Python oops Public,private and protected variables:
#all class variables are public :
class Car():
    def __init__(self,windows,doors,enginetype):
        self.windows=windows #public variables
        self.doors=doors
        self.enginetype=enginetype
        
audi=Car(4,5,'Diesel')
audi

#All class variables are protected:
class Car():
    def __init__(self,windows,doors,enginetype):
        self._windows=windows #public variables
        self._doors=doors
        self._enginetype=enginetype
dir(audi)
#'doors', 'enginetype' and 'windows' are public variables bcs they are not with _
#Protected variables are overridden only from sub classes..but in

audi=Car(4,4,'Diesel')
dir(audi)
#now doors windows and enginetype are protected
audi.windows=5
audi.windows  #windows parameter is overridden as it is public variable
#but protected variables can be overrided only in sub classes
class Truck(Car):
    def __init__(self,windows,doors,enginetype,horsepower):
        super().__init__(windows,doors,enginetype)
        self.horsepower=horsepower
        
truck=Truck(4,4,'Diesel',4000)
dir(truck)
truck._doors=5
truck._doors
truck.windows=4
truck.windows
audi._windows=5
audi._windows

#Private:only inside Car class these private attributes can be modified
#these are only for other developers to indicate when and which all variables to modify,,
#bcs other lang offer thses kind of accessing privileges
class Car():
    def __init__(self,windows,doors,enginetype):
        self.__windows=windows #public variables
        self.__doors=doors
        self.__enginetype=enginetype
audi=Car(4,4,'Diesel')
dir(audi)
class train(Car):
    def __init__(self,windows,doors,enginetype,compartments):
        super().__init__(windows,doors,enginetype)
        self.compartments=compartments
Train=train(4,4,'Diesel',40)
train.__windows=30
train.__windows
