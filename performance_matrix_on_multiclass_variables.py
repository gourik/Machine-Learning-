# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 17:34:58 2021

@author: t
"""

from sklearn import metrics
C="Cat"
D="Dog"
F="Fox"
#Precision of Cat is no. of correctly predicted Cat out of all predicted Cat.
#Recall for Cat is no. of correctly predicted Cat photos out of no. of actual cat
#True values:(actual values):
y_true=[C,C,C,C,C,C, F,F,F,F,F,F,F,F,F,F, D,D,D,D,D,D,D,D,D]
#Predicted values:
y_pred=[C,C,C,C,D,F, C,C,C,C,C,C,D,D,F,F, C,C,C,D,D,D,D,D,D]

#print the confusion matrix:
print(metrics.confusion_matrix(y_true,y_pred))
#print precision and recall among other metrics:
print(metrics.classification_report(y_true,y_pred,digits=3))
