# -*- coding: utf-8 -*-
"""
Created on Wed May 19 16:29:12 2021

@author: Gouri
"""

import seaborn as sns
df=sns.load_dataset("tips")
df.head()

#Correlation with Heatmap:
#A Correlation Heatmap uses colored cells typically in a monochromatic scale to show
#a 2D correlation matrix (table) between two discrete dimensions or event types.It is very important in Feature Selection
df.corr() 
sns.heatmap(df.corr())
df.dtypes

#Join Plot:
# It allows to study relationship between 2 numeric variables. The central chart display their correlation. It is usually 
# a scatter plot, hexbin plot, 2D histogram or 2D density plot

#Univariate Analysis:
sns.jointplot(x='tip',y='total_bill',data=df,kind='hex')

#Pair plot:
#It is also called Scatter plot, in which one variable in the same data row is matched with another variable's value.
sns.pairplot(df)     
sns.pairplot(df,hue='sex')

#Dist plot:
# it helps to check the distribution of columns feature.
sns.distplot(df['tip'])
sns.distplot(df['tip'],kde=False,bins=10)

#Categorical Plots:
#boxplot, violin plot, countplot, barplot

#Count plot:
sns.countplot('sex',data=df) 
sns.countplot('smoker',data=df)
sns.countplot('day',data=df)
sns.countplot(y='smoker',data=df)

#Barplot:
sns.barplot(x='total_bill',y='smoker',data=df)
sns.barplot(y='total_bill',x='smoker',data=df)

#Boxplot:
#Box and whisker plot represent info from a five-number summary:
sns.boxplot('sex','total_bill',data=df)
sns.boxplot('day','total_bill',data=df,palette='rainbow')
sns.boxplot(data=df,orient='v')
#categorize my data based on some other categories:
sns.boxplot(x='total_bill',y='day',hue='smoker',data=df)

#Violin plot helps us to see both kernel density estimation and the box plot:
sns.violinplot(x='total_bill',y='day',data=df,palette='rainbow')
