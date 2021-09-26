# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 11:45:54 2021

@author: t
"""

#Libraries:
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.datasets import load_breast_cancer
pd.pandas.set_option("display.max_columns",None)
cancer=load_breast_cancer() #this cancer is a dictionaries with key value pairs
cancer.keys() #to get all the keys of the dictitionaries
cancer["DESCR"] #it provides all the info...Number of Instances means no. of records
#Number od Attributes indicate no. of features
df=pd.DataFrame(cancer['data'],columns=cancer['feature_names'])
df.head()
df.columns
# len(df.columns)
# df.shape[1]
#all the features of dataframe depict the characteristics of a tumour.

# PCA Visualization:
#Its difficult to visualise high dimensional data,hence we use PCA to find the two 
#principal components and visualize the data in this new, two dimensional plane(space),
#with a single scatter-plot. 
#Before doing it, we have to first scale the data to standard normal distribution so that all features have same units
#We will apply standard normal distribution to all the features and rescale them to same units 
#when it is rescaled, data will be compact and very nearer to each of them 

from sklearn.preprocessing import StandardScaler #this converts any distribution to standard normal distribution where mean=0 and std deviation=1:
scaler=StandardScaler()
scaler.fit(df)
scaled_data=scaler.transform(df)

#PCA with Scikit Learn uses a very similar process to other preprocessing functions that come with Scikit learn.
#We instantiate a PCA object, find the Principal Components using the fit method,then apply rotation and dimensionality 
#reduction by calling transform().
#We can specify how many componets we want to keep when creating PCA object.
from sklearn.decomposition import PCA
pca=PCA(n_components=2) #here it is converted from 30 into 2 features if we want to reduce it to 3 then n_components=3
pca.fit(scaled_data)
x_pca=pca.transform(scaled_data)
scaled_data.shape
x_pca.shape

#these 30 dimensions are reduced to 2. Now we have to plot these two dimensions:
plt.figure(figsize=(8,6))
plt.scatter(x_pca[:,0],x_pca[:,1],c=cancer["target"],cmap='plasma')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.show()
#In the output yellow is malignant and dark blue points are benign
#len(cancer['target'])
