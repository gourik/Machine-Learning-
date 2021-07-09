# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 22:54:33 2021

@author: Gouri
"""

#numpy is general purpose array-processing package.
# pip install numpy
import numpy as np

my_list=[1,2,3,4]

arr1=np.array(my_list)
type(arr1)

arr1

arr1.shape

my_list1=[1,2,3,4]
my_list2=[5,6,7,8]
my_list3=[9,10,11,12]
arr2=np.array([my_list1,my_list2,my_list3])
arr2
arr2.shape
arr2.reshape([4,3])

#Indexing:
arr3=np.array([1,2,3,4,5,6,7,8,9])
arr3[3]

arr2[:,:]
arr2[:,3:]
arr2[1:,2:]
arr2[1:,1:3]
arr2[1,0:3]

#inbuilt functions:
arr=np.arange(0,10,2)
arr

np.linspace(0,10,50)

#copy() function and broadcasting:
arr3[3:]=100 #from index 3 elements are replaced by 100...this is called broadcating
arr3

arr4=arr3
arr4[3:]=500
arr4
arr3 # this is bcs 1rr4 is reference type
#to avoid such scenario...copy() function is used
arr5=arr3.copy()
arr5[3:]=1000
arr5
arr3

#some conditions very useful in Exploratory data analysis:
val=2
arr3<2
arr3 *2
arr3 /2
arr3 %2
arr3[arr3<2]

np.ones(4,dtype=int)
np.ones((2,5),dtype=int)
np.random.rand(3,3)
np.random.randn(3,3) #from std distrbtn
np.random.randint(0,100,8).reshape(4,2) #btwn 0 to 100 ...8 no.s are selected
np.random.random_sample((1,5)) #returns random floats in half-open interval [0.0, 1.0 )
#open interval doesn't include its end points and is represented by ()