# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 22:46:41 2021

@author: Gouri
"""

#pandas is an open source library providing high performance , easy to use data structure 
# data analysis tools for python programming language.

import pandas as pd
import numpy as np

df= pd.DataFrame(np.arange(0,20).reshape(5,4),index=['row1','row2','row3','row4','row5'],columns=['column1','column2','column3','column4'])
df.head()
df.to_csv('test1.csv')

#Accessing the elements from Dataframe:
#1..loc :
#2.iloc:
df.loc['row1']
type(df.loc['row1']) #any single row or single column of Dataframe is called Series

#2..iloc[]:
df.iloc[0:2,0:1]
type(df.iloc[0:2,0:1]) #its type is dataframe

df.iloc[0:2,0]
type(df.iloc[0:2,0]) #now its type is Series

#Taking elements from column2:
df.iloc[0:2,1:]

#Converting dataframes into an array:
df.iloc[:,1:].values
df.iloc[:,1:].values.shape

df.isnull().sum()
df['column1'].value_counts() #counts of each items in column1
df['column1'].unique() #just displays unique elements but not the repeated ones.
df[['column3','column4']]

df=pd.read_csv('E:\ml\python\mercedesbenz.csv')#,sep=';' if we want to read ; seperated values
df.head()
df.info()
df.describe()

#Get the unique category counts:
df['X0'].value_counts()
df[df['y']>100]

#CSV:
from io import StringIO, BytesIO
data=('col1,col2,col3\n'
      'x,y,z\n'
      'a,b,c\n'
      'c,d,3')
type(data)
df=pd.read_csv(StringIO(data))
df=pd.read_csv(StringIO(data),usecols=['col1','col2'])
df
df.to_csv('data.csv')

#Specifying column datatypes:
data=('a,b,c,d\n'
      '1,2,3,4\n'
      '5,6,7,8\n'
      '9,10,11,12')
print(data)
df=pd.read_csv(StringIO(data),dtype=object) 
df #its values are all strings. ex:
df['a']
df['a'][1]
df=pd.read_csv(StringIO(data),dtype=int)
df
df['a']
df=pd.read_csv(StringIO(data),dtype=float)
df

df=pd.read_csv(StringIO(data),dtype={'b':int,'c':float,'a':'int64'})
df
df.dtypes

#Index columns and training delimiters:
data=('index,a,b,c\n'
      '4,apple,bat,5.7\n'
      '8,orange,cow,10')
df=pd.read_csv(StringIO(data))
df
df=pd.read_csv(StringIO(data),index_col=0)
df
df=pd.read_csv(StringIO(data),index_col='a')
df
data=('a,b,c\n'
      '4,apple,bat,\n'
      '8,orange,cow,')
pd.read_csv(StringIO(data)) # now 4,8 is taken as index column ...bcs there is default dtype as None
pd.read_csv(StringIO(data),index_col=False) # to handle such scenario:

#Combining usecols and index_cols:
data=('a,b,c\n'
      '4,apple,bat,\n'
      '8,orange,cow,')
pd.read_csv(StringIO(data),usecols=['b','c'],index_col=False)

#Quoting and Escape characters.
data='a,b\n"hello, \\"Bob\\", nice to see you",5'
pd.read_csv(StringIO(data),escapechar='\\')

#URL to CSV:
df=pd.read_csv('http://download.bls.gov/pub/time.series/cu/cu.items',sep='\t') #if links have tab separations
df.head()

#Read Json to CSV:Json contains data in key value pairs:
Data='{"employee_name":"James","email":"james@gmail.com","job_profile":[{"title1":"Team Lead","Title2":"Sr.Developer"}]}'
df1=pd.read_json(Data)
df=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data',header=None)
df.head()
#Convert JSON to CSV:
df.to_csv('wine.csv')
df1.to_json()
df1
df1.to_json(orient="records")
df1

#Reading HTML content:
url='https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/'
dfs=pd.read_html(url)
dfs[0]

url_mcc='https://en.wikipedia.org/wiki/Mobile_country_code'
dfs=pd.read_html(url_mcc,match='Country',header=0)#header=0 implies first row to be read as column names
dfs

#Reading Excel files:
df_excel=pd.read_excel('E:\ml\python\Excel_Sample_.xlsx')
df_excel.head()

#Pickling:
#All pandas objects are equipped with to_pickle methods which use Python's cPickle module to save data structures to disk using pickle format:
df_excel.to_pickle('df_excel')
pd.read_pickle('df_excel')
df.head()
