# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 15:42:59 2021

@author: Gouri
"""
#Aim of this project is to predict the house price based on various features.
#Life cycle of datascience project:
#1.Data Analysis
#2.Feature Engineering
#3.Feature selection
#4.Model building
#5.Model deployment

#Data Analysis phase:
#Understanding more about the data:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#To display all the columns of dataframe:
pd.set_option('display.max_columns',None)
dataset=pd.read_csv(r'E:\ml\python\train.csv')
dataset.shape
dataset.head()
#In Data Analysis we will analyse to find out following things:
#1.Missing Data
#2.All the numerical veriables
#3.Distribution of Numerical variables
#4.Categorical variables
#5.Cardinality of categorical variables
#6.Outliers
#7.Relationship between independent and dependent feautre (SalePrice)

#Missing Values:
#here percentage of nan values missing in each feature is determined:
#step-1:make a list of features which has missing values:
features_with_na=[features for features in dataset.columns if dataset[features].isnull().sum()>1]
#step-2:Print feature name and mean of missing values present in each feature:
for feature in features_with_na:
    print(feature,np.round(dataset[feature].isnull().mean(),4))

#since there are many missing values, we need to find relationship between missing values and SalesPrice
#Plotting diagram for this relationship:
    for feature in features_with_na:
        data=dataset.copy()
        
    #Let's make a variable that indicates 1 if the observation was missing or zero for observation not missing
        data[feature]=np.where(data[feature].isnull(),1,0) 
        
    #Let's calculate mean of Saleprice where information is missing :
        data.groupby(feature)['SalePrice'].median().plot.bar() #names of columns we want to group on are passed to groupby() function follwed by column on which we want to perform aggreagation or other functionality.
        
        plt.title(feature)
        plt.show()       
#Relation between Missing values and dependent variable is clearly visible i.e for some features mean of SalePrice has highest value for its missing values and some features have highest mean of Saleprice for its non-missing values.
#We need to replace these Missing values(nan) with some meaningful values which is done in Feature Engineering.
        
# From above dataset 'Id' is not required
        print('Total Id´s of houses{}'.format(len(dataset.Id)))
#Numerical variables:
#to find how many features are numerical variables:
numerical_features=[feature for feature in dataset.columns if dataset[feature].dtypes != 'O']
print('number of numerical variables:{}'.format(len(numerical_features)))
# len(dataset.columns)
#visualize numerical variables:
dataset[numerical_features].head()
#Temporal variables:Eg:Datetime variable:These variables are called so bcs every year new data of its type or in its column arrives and current data depends on previous data.
#From dataset we have 4 variables.
year_features=[feature for feature in numerical_features if 'Yr' in feature or 'Year' in feature]
year_features
#to explore contents of these Year variables:
for feature in year_features:
    print(feature,dataset[feature].unique())
    
#Analysing Temporal Datetime variable:
#Checking the relationship between the variable 'YrSold' and dependent variable:
dataset.groupby('YrSold')['SalePrice'].median().plot()
plt.xlabel('YearSold')
plt.ylabel('Average of House Prices')
plt.title('House Price Vs YearSold')
#here price is decreasing as the Years increas, which should not be true
#hence we have to extract some more info:
year_features
#now we can compare all Year features with YearSold by taking difference between them:
for feature in year_features:
    if feature != 'YrSold':
        data=dataset.copy()
        #now taking difference between year variables and the year the house was sold
        data[feature]=data['YrSold']-data[feature]
        plt.scatter(data[feature],data['SalePrice'])#plotting relationship between difference of each year variable from YearSold and SalePrice
        plt.xlabel(feature)
        plt.ylabel('SalePrice')
        plt.show()    
        
#Numerical variables are of 2 types:
#1. Continuous variables
#2. Discrete variables
# here threshold to consider variable as discrete is 25.
discrete_features=[feature for feature in numerical_features if len(dataset[feature].unique())<25 and feature not in year_features + ['Id']]
print('Discrete Variables Count: {}'.format(len(discrete_features)))
#finding the relationship between descrete variables and SalePrice:
for feature in discrete_features:
    data=dataset.copy()
    data.groupby(feature)['SalePrice'].median().plot.bar()
    plt.xlabel(feature)
    plt.ylabel('SalePrice')
    plt.title(feature)
    plt.show()
    
#Continuous variable:
continuous_features=[feature for feature in numerical_features if feature not in discrete_features + year_features + ['Id']]
print('Continuous feature count:{}'.format(len(continuous_features)))
#Let's analyse continuous variables by plotting histograms to understand the difference between each distributions:
for feature in continuous_features:
    data=dataset.copy()
    data[feature].hist(bins=25)
    plt.xlabel(feature)
    plt.ylabel('Count')
    plt.title(feature)
    plt.show()
    
# Exploratory Data Analysis part 2:
# Using Lognormal distribution for skewed distribution:
# Using Logarithmic transformation:
for feature in continuous_features:
    data=dataset.copy()
    if 0 in data[feature].unique():
        pass
    else:
        data[feature]=np.log(data[feature])
        data['SalePrice']=np.log(data['SalePrice'])
        plt.scatter(data[feature],data['SalePrice'])
        plt.xlabel(feature)
        plt.ylabel('SalePrice')
        plt.title(feature)
        plt.show()
        
#To find out outliers in each feature's distribution
        for feature in continuous_features:
            data=dataset.copy()
            if 0 in data[feature].unique():
                pass
            else:
                data[feature]=np.log(data[feature])
                data.boxplot(column=feature) #boxplot can be used only for continuous variables 
                plt.ylabel(feature)
                plt.title(feature)
                plt.show()
                
#Categorical variables:
categorical_features=[feature for feature in dataset.columns if dataset[feature].dtype=='O']
categorical_features
dataset[categorical_features].head()

for feature in categorical_features:
    print('The Feature is {} and number of categories are {}'.format(feature,len(dataset[feature].unique())))

#To find out relationship between categorical variables and dependent variable:
for feature in categorical_features:
    data=dataset.copy()
    data.groupby(feature)['SalePrice'].median().plot.bar()
    plt.xlabel(feature)
    plt.ylabel('SalePrice')
    plt.title(feature)
    plt.show()