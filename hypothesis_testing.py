# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 15:09:18 2021

@author: Gouri
"""
#One sample T-test:
ages=[10,20,35,50,28,40,55,18,16,55,30,25,43,18,30,28,14,24,16,17,32,35,26,27,65,18,43,23,21,20,19,70]
len(ages)
import numpy as np
ages_mean=np.mean(ages)
ages_mean

#Sample:
sample_size=10
age_sample=np.random.choice(ages,sample_size)
age_sample

from scipy.stats import ttest_1samp
ttest,p_value=ttest_1samp(age_sample,30)
ttest
p_value
#null hypothesis:h0:there is no diff btwn population mean and sample mean.
#as p_value is less than 0.05 this null hyp should be rejected.
if p_value<0.05:
    print('we are rejecting hypothesis')
else:
    print('we are accepting hypothesis')
#example_2:
#Consider age of students in a college and in Class A:
import numpy as np
import pandas as pd
import scipy.stats as stats
import math
np.random.seed(6)
#null hyp: there is no diff btwn school_ages and ClassA_ages
school_ages=stats.poisson.rvs(loc=18,mu=35,size=1500) # here poisson distribution is used to generate population
#age of a student starts from 18,all the ages of students have mean as 35, total size will be 1500
ClassA_ages=stats.poisson.rvs(loc=18,mu=30,size=60)
ClassA_ages.mean()
ttest,p_value=ttest_1samp(ClassA_ages,school_ages.mean())
p_value
#as p_value is very less than 0.05 null hyp is rejected
school_ages.mean()
if p_value<0.05:
    print('we are rejecting hypothesis')
else:
    print('we are accepting hypothesis')
    
#Two sample T-Test:or Independent t-test:
#In this Test, means of two independent groups is compared in order to check if population means have significant difference. 
np.random.seed(12)
ClassB_ages=stats.poisson.rvs(loc=18,mu=33,size=60)
ClassB_ages.mean()
#Two sample T-Test is performed now:
_,p_value=stats.ttest_ind(a=ClassA_ages,b=ClassB_ages,equal_var=False)
p_value
if p_value<0.05:
    print('we are rejecting null hypothesis')
else:
    print('we are accepting null hypothesis')
#Paired T-test:
#when we want to check how different the samples from same group are, we can perform paired T-Test.
weight1=[25,30,28,35,28,34,26,29,30,26,28,32,31,30,45]
weight2=weight1+stats.norm.rvs(scale=5,loc=-1.25,size=15)
print(weight1)
print(weight2)     
weight_df=pd.DataFrame({'weight_1':np.array(weight1),'weight2':np.array(weight2),'weight_change':np.array(weight2)-np.array(weight1)})
weight_df
_,p_value=stats.ttest_rel(weight1,weight2)
p_value
#as p_value is greater than 0.05 null hyp is accepted
if p_value<0.05:
    print('we are rejecting hypothesis')
else:
    print('we are accepting hypothesis')

#Correlation:
import seaborn as sns
df=sns.load_dataset('iris')
df.shape
df.corr()
sns.pairplot(df)

#Chi square test:
#It is used to check association between two categorical features of same population.
import scipy.stats as stats
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
dataset=sns.load_dataset('tips')
dataset.head()
#to check assocition between sex and smoker:
dataset_table=pd.crosstab(dataset['sex'],dataset['smoker'])#crosstab calculates how man male and females smoke and dont smoke in 2X2 2D array
dataset_table

#Obseved values:
Observed_Values=dataset_table.values
val=stats.chi2_contingency(dataset_table)
val
expected_values=val[3]
# dataset_table.shape
no_of_rows=len(dataset_table.iloc[0:2,0])
no_of_columns=len(dataset_table.iloc[0,0:2])
degrees_of_freedom=(no_of_rows-1)*(no_of_columns-1)
print('Degrees of Freedom',degrees_of_freedom)
alpha=0.05
#chi-square formula: X2=summation((o-e)2/e)
from scipy.stats import chi2
chi_square=sum(((o-e)**2./e for o,e in zip(Observed_Values,expected_values)))
chi_square_statistic=chi_square[0]+chi_square[1]
chi_square_statistic
critical_value=chi2.ppf(q=1-alpha,df=degrees_of_freedom)
critical_value

#another way to conclude about hypothesis:
p_value=1-chi2.cdf(x=chi_square_statistic,df=degrees_of_freedom)
p_value
print('Significance value:', alpha)
if chi_square_statitic>=critical_value:
    print('Null Hypothesis is rejected: There is no difference between two features is accepted')
else:
    print('Null Hypothesis is accepted: There is no difference between two features')
    
if p_value<=alpha:
    print('Reject H0:There is difference between two features')
else:
    print('Accept H0:There is difference between two features')