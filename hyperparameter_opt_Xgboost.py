# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 10:28:25 2021

@author: t
"""

import numpy as np
import pandas as pd
pd.pandas.set_option('display.max_columns',None)

df=pd.read_csv("E:\ml\python\Churn_Modelling.csv")
df.head()

#Correlation:TO check whether each of the independent features affect the dependent variabels:
import matplotlib.pyplot as plt
import seaborn as sns
#to get correlations of each feature in dataset:
df.columns
corr_matrix=df.corr()
corr_matrix
top_corr_features=corr_matrix.index
top_corr_features
plt.figure(figsize=(20,20))
#plot heatmap:
g=sns.heatmap(df[top_corr_features].corr(),annot=True,cmap="RdYlGn")

#Getting independent and dependent features:
#As first 3 columns have correlation value as negetive and are not that significant 
X=df.iloc[:,3:13]
Y=df.iloc[:,13]
#as a part of feature engineering categorical variables should be converted to dummy variables 
geography=pd.get_dummies(X["Geography"],drop_first=True)#drop_first is set ture to prevent it from dummy variable trap
#Categorical variables cannot be used directly for ML algorithms hence they need to be converted into numerical variables which are called dummy variables
#this is done through label encoding..one hot encoding can be implemented as a type of label encoding in which each of categorical classes of each variable are converted into attributes.
#each attribute contain binary values which represent presence and absence of those attributes. But these attributes are highly correlated ...one attribute predicts value of other attribute
#hence one attribute column always will be dropped to prevent redundancy which is called dummy variable trap
  
geography.head()
gender=pd.get_dummies(X["Gender"],drop_first=True)
gender.head()

#dropping categorical features:
X=X.drop(["Gender","Geography"],axis=1)
X.head()
X=pd.concat([X,gender,geography],axis=1)#appended as columns
X.head()

#Hyper parameter optimization:
#XGBClassifier() method has so many parameters which are difficult to set by us. Hence
# a randomized XGBClassifier() can be implemented. This will set the parameters the values internally
# at which method performs well. we can also set values for some of the features.
# when a list of values instead of a single value is passed, XGBClassifier() takes different permutations and combinations of these values
params={
        "learning_rate"    : [0.05,0.10,0.15,0.20,0.25,0.30],
        "max_depth" : [ 3,4,5,6,8,10,12,15],
        "min_child_weight" : [ 1,3,5,7],
        "gamma"            : [0.0,0.1,0.2,0.3,0.4],
        "colsample_bytree" : [0.3,0.4,0.5,0.7]
        }
    
#hyper parameter optimization using RandomizedSearchCV:
from sklearn.model_selection import RandomizedSearchCV,GridSearchCV
import xgboost
classifier=xgboost.XGBClassifier()
random_search=RandomizedSearchCV(classifier,param_distributions=params,n_iter=5,scoring="roc_auc",n_jobs=-1,cv=5,verbose=3)

def timer(start_time=None):
    if not start_time:
        start_time=datetime.now()
        return start_time
    elif start_time:
        thour,temp_sec=divmod((datetime.now()-start_time).total_seconds(),3600)
        tmin,tsec=divmod(temp_sec,60)   
        print("\n Time taken:%i hours %i minutes amd %i seconds"%(thour,tmin,round(tsec,2)))
        
from datetime import datetime
start_time=timer(None) #timing starts from this point for "start_time" variable
random_search.fit(X,Y)
timer(start_time) #timing ends here for "start_time" variable

random_search.best_estimator_
classifier=xgboost.XGBRFClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,
              colsample_bynode=1, colsample_bytree=0.5, gamma=0.4, gpu_id=-1,
              importance_type='gain',
              learning_rate=0.2, max_delta_step=0, max_depth=3,
              min_child_weight=7, missing=nan, monotone_constraints='()',
              n_estimators=100, n_jobs=4, num_parallel_tree=1, random_state=0,
              reg_alpha=0, reg_lambda=1, scale_pos_weight=1, subsample=1,
              tree_method='exact', validate_parameters=1, verbosity=None)

random_search.best_params_

from sklearn.model_selection import cross_val_score
score=cross_val_score(classifier, X,Y,cv=10)
score
score.mean()
