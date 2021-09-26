# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 12:22:03 2021

@author: t
"""

import numpy as np
import pandas as pd
 
dataset=pd.read_csv("E:\ml\python\Mall_Customers.csv")
dataset.head()

X=dataset.iloc[:,[3,4]].values
#Applying DBSCAN algorithm:
from sklearn.cluster import DBSCAN
dbscan=DBSCAN(eps=3,min_samples=4)
#fitting the model:(training the model):
model=dbscan.fit(X)
labels=model.labels_ #labels_ indicate how many groups of cluters are formed for each row of data 
# -1 is noise. 
from sklearn import metrics
#identifying points which are core points:means they are not gouped into any of the clusters
#0,1,2... indicate oth ,1st and 2nd cluster and so on and soforth
sample_cores=np.zeros_like(labels,dtype=bool)
sample_cores.shape
sample_cores[dbscan.core_sample_indices_]=True #this attribute core_sample_indices indicates index of core samples
#except -1, all other values are made as true..bcs they all indicate clusters 
#calculating no. of clusters:
n_clusters=len(set(labels))-(1 if -1 in labels else 0)
n_clusters
print(metrics.silhouette_score(X,labels))

#it is a very good algo if we want to cluster the datasets based on their density... 