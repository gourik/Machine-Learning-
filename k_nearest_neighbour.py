# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 15:04:06 2021

@author: t
"""

#A classified dataset from a company is considered,in which feature(column) names are hidden but data and target classes are given
#Using KNN algorithm, a model will be created which directly predicts a class for new data point.

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
pd.pandas.set_option('display.max_columns',None)
df=pd.read_csv(r"E:\ml\python\Classified Data.csv",index_col=0)
df.head()

#Standardization:
#As the values of columns will be in differenet units, they have to be standardized.
#Bcz KNN classifier predicts class of a given test observation by identifying observations which are nearest to it. Scale of variables matter.
#Any variables that are on a large scale will have a much larger effect on the distance between observations and hence on the KNN classifier than variables 
#that are on a small scale.

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
scaler.fit(df.drop('TARGET CLASS',axis=1))
scaled_features=scaler.transform(df.drop('TARGET CLASS',axis=1))
df_scaled_features=pd.DataFrame(scaled_features,columns=df.columns[:-1])
df_scaled_features.head()

#Pair plot: To visualise the distribution:
sns.pairplot(df,hue="TARGET CLASS")

#Training the model:
#Train test split:
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(scaled_features,df['TARGET CLASS'],test_size=0.30)

#Using KNN:implementing KNN algorithm:
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train,y_train)
pred=knn.predict(X_test)    

#Predictions and Evaluations:
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test,pred))
print(classification_report(y_test,pred))

#Choosing K-Value:
error_rate=[]
for i in range(1,40):
    knn=KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train,y_train)
    pred_1=knn.predict(X_test)
    error_rate.append(np.mean(pred_1!=y_test))
    
plt.figure(figsize=(10,6))
plt.plot(range(1,40),error_rate,color='blue',linestyle='dashed',marker='o',markerfacecolor='red',markersize=10)
plt.title("Error rate v/s K-Value")
plt.xlabel("K-Value")
plt.ylabel("Error rate")

#at K=23:
knn=KNeighborsClassifier(n_neighbors=23) 
knn.fit(X_train,y_train)
pred_2=knn.predict(X_test)
print(confusion_matrix(y_test,pred_2))
print(classification_report(y_test, pred_2))

#Choosing K-Value:(another method):
#Using elbow method to pick a good K-Value:
from sklearn.model_selection import cross_val_score
accuracy_rate=[]
for i in range(1,40):
    knn=KNeighborsClassifier(n_neighbors=i)
    score=cross_val_score(knn,df_scaled_features,df["TARGET CLASS"],cv=10)
    accuracy_rate.append(score.mean())
#It can be done either with accuracy rate or error rate bcs one of them will be obtained from the other 
    
error_rate=[]
for i in range(1,40):
    knn=KNeighborsClassifier(n_neighbors=i)
    score=cross_val_score(knn,df_scaled_features,df["TARGET CLASS"],cv=10)
    error_rate.append(1-score.mean())

plt.figure(figsize=(10,6))
plt.plot(range(1,40),error_rate,color='blue',linestyle='dashed',marker='o',markerfacecolor='red',markersize=10)
plt.title("Error rate v/s K-Value")
plt.xlabel("K-Value")
plt.ylabel("Error rate")
#23 is chosen bcs after 23 error_rate is decreasing
plt.figure(figsize=(10,6))
plt.plot(range(1,40),accuracy_rate,color='blue',linestyle='dashed',marker='o',markerfacecolor='red',markersize=10)
plt.title("Error rate v/s K-Value")
plt.xlabel("K-Value")
plt.ylabel("Accuracy rate")
