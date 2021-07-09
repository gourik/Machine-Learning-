# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 21:59:11 2021

@author: Gouri
"""


#Sets: Sets are unordered collection of elements which are of same data type which are iterable,
#mutable but has no duplicate elements.
set_var=set() 
set_var
type(set_var)

set_var={1,2,3,4,3}
set_var

set1={'ella','emma','emili'}
set1.add('anna')
set1

set2={'suresh','ramesh','usha','hema','uma'}
set3={'suresh','ramesh','usha','hema','uma','lata'}
set4={'suresh','ramesh','usha','hema','uma','jaya'}
set3.difference(set2)

set3.difference_update(set2)
set3

set4.intersection(set2)

#Dictionaries:
# It is collection which is unordered, changable and indexed. In Python dictionaries are written
# with curly braces and they have keys and values.

dictionary_1={'car1':'mercidies','car2':'audi'}
dictionary_1
for x in dictionary_1:
    print(x)

for x in dictionary_1.values():
    print(x)

for x in dictionary_1.items():
    print(x)

dictionary_1['car3']='audi2.1'
dictionary_1

dictionary_1['car1']='maruti'
dictionary_1

#Nested dictionaries:
car1_model={'mercidies':1960}
car2_model={'audi':1970}
car3_model={'ambassador':1980}

car_type={'car1':car1_model,'car2':car2_model,'car3':car3_model}
car_type['car1']['mercidies']

#Tuples:
# it is unchangeable.Entire tuple can be changed but only item within it cannot be changed.
tuple1=('hi','hello','bye')
tuple1

tuple1[0]='guten_morgen' #is not supported
tuple1=('hi','hello','world') #this works

#Inbuilt functions:
tuple1.count('hi')

tuple1.index('hi')
