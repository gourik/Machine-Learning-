# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 17:19:19 2021

@author: Gouri
"""
#Multiple linear regression:
#importing libraries:
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing dataset:
dataset=pd.read_csv('E:\ml\python\Startups_50.csv')
X=dataset.iloc[:,:-1]
y=dataset.iloc[:,4]
dataset
#Convert the categorical column into numerical ones by one-hot encoding:
states=pd.get_dummies(X['State'],drop_first=True)#it drops first column after one hot encoding

#Drop state column:
X=X.drop('State',axis=1)

#Concatinate dummy variables:
X=pd.concat([X,states],axis=1) # its like y=ß0+ß1.x1+ß2.x2+ß3.x3+ß4.x4+ß5.x5

#Splitting the dataset into test and train dataset:
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)

#Fitting Multiple Linear Regression into Training set:
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,y_train)

#Predicting the Test results:
y_pred=regressor.predict(X_test) 

#comparing y_test and predicted y values:
from sklearn.metrics import r2_score #the more the score near the value 0 more accurate is prediction
score=r2_score(y_test,y_pred)
score #0.93 is very nearer to 1 ...so linear regression model is a good model
