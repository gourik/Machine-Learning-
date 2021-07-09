# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 15:46:16 2021

@author: Gouri
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv')
df.head()
df.shape
##Univariate analysis: we use only one feature:
df_setosa=df.loc[df['species']=='setosa'] #saving all info pertaining to setosa into df_setosa
df_versicolor=df.loc[df['species']=='versicolor'] #saving all info pertaining to setosa into df_setosa
df_virginica=df.loc[df['species']=='virginica'] #saving all info pertaining to setosa into df_setosa
df_virginica
plt.plot(df_setosa['sepal_length'],np.zeros_like(df_setosa['sepal_length']),'o') #x is sepal_length y is zeroes bcs its a univariate analysis
plt.plot(df_versicolor['sepal_length'],np.zeros_like(df_versicolor['sepal_length']),'o') #x is sepal_length y is zeroes bcs its a univariate analysis
plt.plot(df_virginica['sepal_length'],np.zeros_like(df_virginica['sepal_length']),'o') #x is sepal_length y is zeroes bcs its a univariate analysis
plt.xlabel('Sepal length')
plt.show()

#Bivariate Analysis:
sns.FacetGrid(df,hue='species',size=5).map(plt.scatter,'sepal_length','sepal_width').add_legend()
plt.show()

sns.FacetGrid(df,hue='species',size=5).map(plt.scatter,'petal_length','petal_width').add_legend()
plt.show()

#Multivariate Analysis:
sns.pairplot(df,hue='species',size=5)
