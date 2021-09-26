# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 11:37:20 2021

@author: t
"""

#EDA with SweetViz library in seconds to perform Visualization:
import pandas as pd

#Dataset link:https://www.kaggle.com/c/house-prices-advanced-regression-techniques
import sweetviz
train=pd.read_csv(r'E:\ml\python\train_sweetviz.csv')
test=pd.read_csv(r'E:\ml\python\test_sweetviz.csv')

train.head()
