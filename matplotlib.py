# -*- coding: utf-8 -*-
"""
Created on Tue May 18 19:27:32 2021

@author: Gouri
"""

import matplotlib.pyplot as plt
#%matplotlib
import numpy as np
x=np.arange(0,10)
y=np.arange(11,21)

#Plotting using matplotlib:
#plt scatter: it is used to scatter the values of x,y in 2D graph


plt.xlabel('X_axis')
plt.ylabel('Y_axis')
plt.title('Graph in 2D')
plt.scatter(x,y,c='r')

plt.show()
plt.savefig('Test.png')

y=x*x
#plt plot:
plt.plot(x,y,'r')
plt.plot(x,y,'r--')
plt.plot(x,y,'r*')
plt.plot(x,y,'r*-')
plt.plot(x,y,'ro')
plt.plot(x,y,'ro--')
plt.plot(x,y,'r*-',linestyle='dashed',linewidth=2,markersize=12)

#Creating subplots:
plt.subplot(2,2,1)
plt.plot(x,y,'r')
plt.subplot(2,2,2)
plt.plot(x,y,'g')
plt.subplot(2,2,3)
plt.plot(x,y,'b')
plt.subplot(2,2,4)
plt.plot(x,y,'o')

x=np.arange(1,11)
y=3*x+5
plt.title("Matplotlib demo")
plt.xlabel("X axis caption")
plt.ylabel("Y axis caption")
plt.plot(x,y)
plt.show()

np.pi
#Compute x and y coordinates for points on a sine curve:
x=np.arange(0,4*np.pi,0.1)
y=np.sin(x)
plt.title('Sine wave form')

#plot the points using matplotlib:
plt.plot(x,y)
plt.show()

#subplot:
#Compute x and y coordinates for points on sine and cosine curves:
x=np.arange(0,5*np.pi,0.1)
y_sin=np.sin(x)
y_cos=np.cos(x)

#setting up a sub plot grid that has height 2 and width 1 and set the first such subplot as active:
plt.subplot(2,1,1)
#make the first plot:
plt.plot(x,y_sin,'g--')
plt.title('Sine')
 
plt.subplot(2,1,2)
plt.plot(x,y_cos,'r--')
plt.title('Cosine')

#Show the figure:
plt.show()

#Bar plot:
x=[2,8,10]
y=[11,16,9]
x2=[3,9,11]
y2=[6,15,7]
plt.bar(x,y)
plt.bar(x2,y2,color='g')
plt.title('Bar graph')
plt.ylabel('Y Axis')
plt.xlabel('X Axis')
plt.show()

#Histogram:
a=np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
#plt.hist(a)
plt.hist(a,20)
plt.title("Histogram")
plt.show()

#Box plot using Matplotlib:
data=[np.random.normal(0,std,100) for std in range(1,4)]
#rectangular box plot:
plt.boxplot(data,vert=True,patch_artist=False)

#Pie chart:
#Data to plot:
labels='python','C++','Ruby','Java'
sizes=[215,130,245,210]
colors=['gold','yellowgreen','lightcoral','lightskyblue']
explode=(0.1,0,0,0)

#plot:
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True)
plt.axis('equal')
plt.show()