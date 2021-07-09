# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 11:50:52 2021

@author: Gouri
"""

from sklearn.datasets import load_boston
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=load_boston()
data
df=pd.DataFrame(data.data) #converting into dataframe
df
df.head()
df.columns=data.feature_names
df.head()
data.target
data.target.shape #'target' is a dependent variable
df['Price']=data.target #creating a new variable in dataframe called Price for dependent variable
df.head()
X=df.iloc[:,:-1] #independent features ...all columns except last column
y=df.iloc[:,-1] #only last column

#Linear regression:
from sklearn.model_selection import cross_val_score # to perform cross validation
from sklearn.linear_model import LinearRegression
lin_regressor=LinearRegression() #lin regression object
#cross validation is done with 5 experiments
mse=cross_val_score(lin_regressor,X,y,scoring='neg_mean_squared_error',cv=5) #neg of mean_squarred_error should be as close as possible to zero
# model perf increases if its closeness to 0 increases
mean_mse=np.mean(mse) # mean squared error..mse
print(mean_mse) 

#Ridge Regression:
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

ridge=Ridge()
parameters={'alpha':[1e-15,1e-10,1e-8,1e-3,1e-2,1,5,10,20,30,35,40,45,50,55,100]}
ridge_regressor=GridSearchCV(ridge,parameters,scoring='neg_mean_squared_error',cv=5)
ridge_regressor.fit(X,y)
ridge_regressor.best_params_
ridge_regressor.best_score_

#Lasso Regressor:
from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV
lasso=Lasso()
parameters={'alpha':[1e-15,1e-10,1e-8,1e-3,1e-2,1,5,10,20,30,35,40,45,50,55,100]}
lasso_regressor=GridSearchCV(lasso,parameters,scoring='neg_mean_squared_error',cv=5)
lasso_regressor.fit(X,y)
lasso_regressor.best_params_
lasso_regressor.best_score_
#here lasso has more value than that of ridge ...it is bcs it ignores some of featues ....it performs usually better when more features are there
#lasso is more generalised one as it considers only magnitude of slope...generalised means not meant for any particular kind of data..such as trained or test data
from sklearn.model_selection import train_test_split
X_train, X_test,y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=0)
prediction_lasso=lasso_regressor.predict(X_test)
prediction_ridge=ridge_regressor.predict(X_test)
import seaborn as sns
sns.distplot(y_test-prediction_lasso)
sns.distplot(y_test-prediction_ridge)    
#in the plots, ridge appears to be more stable than that of Lasso's.
 