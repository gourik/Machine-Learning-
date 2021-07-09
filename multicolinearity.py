# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 17:08:18 2021

@author: Gouri
"""

import pandas as pd
import statsmodels.api as sm
df_ad=pd.read_csv('E:\ml\python\Advertising.csv',index_col=0)
X=df_ad[['TV','radio','newspaper']]
y=df_ad['sales']
df_ad.head()
#fit a OLS model with intercept: OLS stands for Ordinary Least Square method which adds a column of 
#constant i.e here with value 1 in order to be multiplied by intercept ß0.
X=sm.add_constant(X)
X
model=sm.OLS(y,X).fit() #endog:output value exog:input value
model.summary()
#first have to check values of coeffiecients,if there is no multicollinearity problem among independent features then
# coefficients will have values nearer to 0, R2 error adj. R-sqrd error will be 0.8-1.0 and stderr will also be less.
#In this case only p value is more ..its only bcs newspaper expenditure has negative value ...so there is no need to expend much for newspaper..so its neg
#so there is no multicollinearity problem among independent features.
#so this is one way of checking dependency or collinearity among features
#correlation is checked among features:another way of checking multicollinearity

import matplotlib.pyplot as plt
X.iloc[:,1:].corr()
#here values are less than 0.5 so there is no much correlation among independent features so there is no  problem of multicollinearity.
df_salary=pd.read_csv('E:\ml\python\Salary_Data.csv')
df_salary.head()
X=df_salary[['YearsExperience','Age']]
y=df_salary['Salary']
#checking multicollinearity with OLS method:
X=sm.add_constant(X)
model=sm.OLS(y,X).fit()
model.summary()
# coefficients and sqrred error values are normal but std error and p value of Age are not. Std err values are very high and p value should be less than 0.05
# so this indicates that there is possibility of correlation btwn the feautes
#in order to confirm we can use corr():
X.iloc[:,1:].corr()
#this confirms that both features have more correlation i.e 98%..
#so they both provide same info to output variable or feature in order to determine it .
#as p value for Age is more, we can drop it. But we have to always check the correlation among features using corr() before dropping them...bcs p-value just
#indicates possibility of correlation but its magnitude will be determined by corr() only.
