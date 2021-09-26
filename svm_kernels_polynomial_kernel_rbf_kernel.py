# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 11:03:38 2021

@author: t
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
pd.pandas.set_option("display.max_rows",None)
x=np.linspace(-5.0,5.0,100)
y=np.sqrt(10**2-x**2)
x=np.hstack([x,-x])
y=np.hstack([y,-y])

x1=np.linspace(-5.0,5.0,100)
y1=np.sqrt(5**2-x1**2)
y1=np.hstack([y1,-y1])
x1=np.hstack([x1,-x1])

plt.scatter(y,x)
plt.scatter(y1,x1)
#these data cannot be linearly seperable

df1=pd.DataFrame(np.vstack([y,x]).T,columns=['X1','X2'])
df1['Y']=0
df2=pd.DataFrame(np.vstack([y1,x1]).T,columns=['X1','X2'])
df2['Y']=1
df=df1.append(df2)
df.head()

#dependent features and independent feature:
X=df.iloc[:,:2]
X
y=df.Y
y

#Splitting dataset as Train and Test dataset:
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)
X_train
y_train

from sklearn.svm import SVC
classifier=SVC(kernel="linear")
classifier.fit(X_train,y_train)
y_pred=classifier.predict(X_test)

from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)
df.head()

#We need to find components for polynomial kernel:
#considering x1,x2,x1_square,x2_square,x1*x2 terms obtained from dot product as features:
df['X1_square']=df['X1']**2
df['X2_square']=df['X2']**2
df['X1*X2']=df['X1']*df['X2']
df.head()

#Independent features and dependent features:
X=df[['X1','X2','X1_square','X2_square','X1*X2']]    
y=df.iloc[:,2]
y
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)
X_train

import plotly.express as px #has to be implemented in Jupyter notebook
fig=px.scatter_3d(df,x='X1',y='X2',z='X1*X2',color='Y')
fig.show()

fig=px.scatter_3d(df,x='X1_square',y='X2_square',z='X1*X2',color='Y')
fig.show()
#poly kernel and rbf kernels internally select the components and check whether they can classify data points perfectly and then select only those
#components which classify perfecly to give accuracy 1 or 100%
#without creating components we can simply apply rbf or polynomial kernels:

classifier=SVC(kernel="poly")
classifier.fit(X_train,y_train)
y_pred=classifier.predict(X_test)
accuracy_score(y_test, y_pred)

#with rbf kernel:
classifier=SVC(kernel="rbf")
classifier.fit(X_train,y_train)
y_pred=classifier.predict(X_test)
accuracy_score(y_test, y_pred)
#these kernels are set by hyperparameter tuning