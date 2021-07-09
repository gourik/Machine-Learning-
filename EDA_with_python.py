# -*- coding: utf-8 -*-
"""
Created on Thu May 20 09:54:05 2021

@author: Gouri
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
train=pd.read_csv(r'E:\ml\python\titanic_train.csv')
train.head()
#Exploratory Data Analysis:
#1. Checking out for Missing Data: It implies that there may exist null values.
train.isnull()
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')

#Handling missing data:
train['Age']
#Roughly 20% of Age data is missing. So the proportion of Age missing is small to replace with some form of imputation.
#where as Cabin column has too many missing data to make something at basic level, this can be created as another feature:'Cabin Known':1 or 0
#Visualizing some more data:
sns.set_style('whitegrid')
sns.countplot(x='Survived',data=train)
sns.countplot(x='Survived',hue='Sex',data=train,palette='RdBu_r')
sns.countplot(x='Survived',hue='Pclass',data=train,palette='rainbow')
sns.distplot(train['Age'].dropna(),kde=False,color='darkred',bins=40)
train['Age'].hist(bins=30,color='darkred',alpha=0.3) #this can also be used to create a histogram 
sns.countplot(x='SibSp',data=train)
train['Fare'].hist(color='green',bins=40,figsize=(8,4))

#Data Cleaning:
# We have to fill in missing Age data instead of just dropping the Age data rows. One way to do this is by filling in mean age of all the passengers(imputation). 
plt.figure(figsize=(12,7))
sns.boxplot(x='Pclass',y='Age',data=train,palette='winter') 
def impute_age(cols):
    Age=cols[0]
    Pclass=cols[1]
    if pd.isnull(Age):
        if Pclass==1:
            return 37
        elif Pclass==2:
            return 29
        else:
            return 24
        
    else:
        return Age

train['Age']=train[['Age','Pclass']].apply(impute_age,axis=1)        
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
#dropping the Cbin col bcs it has lot many NaN values.
train.drop(['Cabin'],axis=1,inplace=True)
#train['Cabin'].head() # does show error bcs inplace=true returns no dataframe with cabin column
#del train['Cabin']
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
train.head()
train.dropna(inplace=True)
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')

#Converting Categorical features:
#We have to convert categorical features into dummy variables using Pandas, otherwise machine learning algorithms won't be able to directly take in those features as inputs
train.info()
#embark=pd.get_dummies(train['Embarked'],drop_first=True).head() #dummy variable trapping
sex=pd.get_dummies(train['Sex'],drop_first=True)
embark=pd.get_dummies(train['Embarked'],drop_first=True)
train.drop(['Sex','Embarked','Name','Ticket'],axis=1,inplace=True)
train.head()
train=pd.concat([train,sex,embark],axis=1)
train.head()
#Survived column is dependent variable:

#Building a logistic regression model:
#Staring with splitting data into training and test dataset
train.drop('Survived',axis=1).head() #bcs Survived is a dependent variable
train['Survived'].head()
#train
#train=train.reset_index()
# np.isfinite(train)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train,y_test=train_test_split(train.drop('Survived',axis=1),train['Survived'],test_size=0.30,random_state=101)

#Training and Predicting:
from sklearn.linear_model import LogisticRegression
logmodel=LogisticRegression()
logmodel.fit(X_train,y_train)

predictions=logmodel.predict(X_test)
from sklearn.metrics import confusion_matrix
accuracy=confusion_matrix(y_test, predictions)
accuracy

from sklearn.metrics import accuracy_score
accuracy=accuracy_score(y_test,predictions)
accuracy
predictions
