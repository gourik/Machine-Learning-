# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 11:16:00 2021

@author: t
"""
#threshold selected depends on ROC Curve and accuracy obtained using the curve: 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import make_classification #using this we can create datasets
X,y=make_classification(n_samples=2000,n_classes=2,weights=[1,1],random_state=1) #n_samples is records,
#n_features=20 (default),n_classes indicate output classes such as 0 and 1 in binary classification..
#here usecase considered is binary classification only.weights indicate the balancing of classes of y in the dataset..
#i.e the proportion of two classes in this usecase 
X.shape
y #here 1000 will be 1 and 1000 will be 0.

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=1)

from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

#Random Forests:
#Applying RandomForestClassifier:
from sklearn.ensemble import RandomForestClassifier
rf_model=RandomForestClassifier()
rf_model.fit(X_train,y_train)
y_train_pred=rf_model.predict_proba(X_train)
print("RF train roc-auc-score:{}".format(roc_auc_score(y_train, y_score)))