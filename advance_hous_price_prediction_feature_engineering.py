# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 16:38:23 2021

@author: Gouri
"""

#In this step following things are performed:
#1.Missing values:
#2.Temporal Variables
#3.Categorical variables:we remove rare variables 
#4.Standardising values of variables to same range

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#To visualise all the columns in a dataframe:
pd.pandas.set_option('display.max_columns',None)

dataset=pd.read_csv(r'E:\ml\python\train.csv')
dataset.head() 
#Always there will be a chance of data leakage, so we need to split the data first and then do feature engineering:
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(dataset,dataset['SalePrice'],test_size=0.1,random_state=0) 
X_train.shape,X_test.shape

#Missing values:
#Capturing all nan values:
#First handling categorical variables which have missing values:
nan_features=[feature for feature in dataset.columns if dataset[feature].isnull().sum()>1 and dataset[feature].dtypes=='O'] 
for feature in nan_features:
    print('{}: {}%'.format(feature,np.round(dataset[feature].isnull().mean(),4)))
    
#Replace missing value with a new label:
def replace_cat_feature(dataset,nan_features):
     data=dataset.copy()
     data[nan_features]=data[nan_features].fillna('Missing')
     return data

dataset=replace_cat_feature(dataset, nan_features)    
dataset[nan_features].isnull().sum()
dataset.head()

#Now checking for numeric variables if they have nan values or not:
numerical_nan_features=[feature for feature in dataset.columns if dataset[feature].dtypes!='O' and dataset[feature].isnull().sum()>1] 
#dataset[numerical_features]

#printing numerical nan variables and % of missing values in each variable:
for feature in numerical_nan_features:
    print('{}: %{}'.format(feature,np.round(dataset[feature].isnull().mean(),4)))

#replacing missing values of numeric variables with median since there are outliers:
for feature in numerical_nan_features:
    median_value=dataset[feature].median()
    #create a new feature to capture nan values:
    dataset[feature+'nan']=np.where(dataset[feature].isnull(),1,0)
    dataset[feature].fillna(median_value,inplace=True)
    
dataset[numerical_nan_features].isnull().sum()
dataset.head(50)

#Temporal variables:
for feature in['YearBuilt','YearRemodAdd','GarageYrBlt']:
    dataset[feature]=dataset['YrSold']-dataset[feature]#changing values of year features with their diff from YrSold feature bcs they have good relation with dependent feature SalePrice
dataset.head()    
dataset[['YearBuilt','YearRemodAdd','GarageYrBlt']].head()

#Numerical variables:
#Since numerical variables are skewed we will perform lognormal distribition:
dataset.head()
# numerical_features=[feature for feature in dataset.columns if dataset[feature].dtypes!='O']
numerical_features=['LotFrontage','LotArea','1stFlrSF','GrLivArea','SalePrice']
for feature in numerical_features:
    dataset[feature]=np.log(dataset[feature])
    
dataset.head()

#Handling rare categorical feature: in this step we will remove categorical variabes that are present less than 1% of total observations:
categorical_features=[feature for feature in dataset.columns if dataset[feature].dtypes=='O']
categorical_features

for feature in categorical_features:
    temp=dataset.groupby(feature)['SalePrice'].count()/len(dataset)
    temp_df=temp[temp>0.01].index
    dataset[feature]=np.where(dataset[feature].isin(temp_df),dataset[feature],'Rare_var')

dataset.head(100)    
for feature in categorical_features:
    labels_ordered=dataset.groupby([feature])['SalePrice'].mean().sort_values().index
    labels_ordered={k:i for i,k in enumerate(labels_ordered,0)}
    dataset[feature]=dataset[feature].map(labels_ordered)
dataset.head(10)
#Feature scaling:
feature_scale=[feature for feature in dataset.columns if feature not in ['Id','SalePrice']]
feature_scale
len(feature_scale)
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
scaler.fit(dataset[feature_scale])

scaler.transform(dataset[feature_scale])

#Transform train and test set and add on Id and SalePrice variables:
data=pd.concat([dataset[['Id','SalePrice']].reset_index(drop=True),
                pd.DataFrame(scaler.transform(dataset[feature_scale]),columns=feature_scale)],axis=1)
data.head()
data.to_csv('X_train.csv',index=False)#it might work in jupyter notebook

