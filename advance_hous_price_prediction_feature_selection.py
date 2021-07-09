# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 14:13:08 2021

@author: t
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import Lasso
from sklearn.feature_selection import SelectFromModel

#To visualise all the columns in the dataframe:
pd.pandas.set_option('display.max_columns',None)

dataset=pd.read_csv('X_train.csv')
dataset.head()
#Capture dependent feature:
y_train=dataset[['SalePrice']]
y_train

#dropping dependent feature from dataset:
X_train=dataset.drop(['Id','SalePrice'],axis=1)
X_train

# Applying Feature selection:
#1.Selecting Lasso Regression model and 
#2.selecting suitable alpha(equivalent of penalty)
#3.The bigger the alpha value, less no. of features will be selected
#4. then using selectFromModel object from sklearn,which selects features whose coefficients are non-zero
feature_select_model=SelectFromModel(Lasso(alpha=0.005,random_state=0)) #we should remember to set seed value bcs same seed value should be used for test data
feature_select_model.fit(X_train,y_train) 
feature_select_model.get_support()
#printing no. of total and selected features:
#making list of selected features:
selected_features=X_train.columns[(feature_select_model.get_support())]
#Printing some statistics:
print("Total features:{}".format(X_train.shape[1]))
# print("Total features:{}".format(dataset.shape[1]))
print('Total no. of selected features are: {}'.format(len(selected_features)))
print("Features with their co-efficients schrank to zero:{}".format(np.sum(feature_select_model.estimator_.coef_==0)))
selected_features
X_train=X_train[selected_features]
X_train.head()
