#!/usr/bin/env python
# coding: utf-8

# ## Import modules

# In[19]:


import pandas as pd
import numpy as np


# ## Read in the dataset

# In[20]:


data = pd.read_csv('data-titanic.csv')
data.head()


# ## Apply functions using apply()

# In[21]:


func_lower = lambda x: x.lower()


# In[22]:


data.Name.apply(func_lower)


# ## Apply functions using applymap()

# In[23]:


data[['Age', 'Pclass']].applymap(np.square)


# ### Applying our own functions 

# In[24]:


def my_func(i):
    return i + 20


# In[25]:


data[['Age', 'Pclass']].applymap(my_func)


# ## A `SettingWithCopyWarning` scenario

# In[36]:


data[data.Age.isnull()].Age = data.Age.mean()


# ## Handling the `SettingWithCopyWarning`

# In[39]:


data[data.Age.isnull()].Age.head()


# In[41]:


data.loc[data.Age.isnull(), 'Age'] = data.Age.mean


# In[42]:


data[data.Age.isnull()]


# In[7]:


data = pd.read_csv('data-titanic.csv')
data.head()


# ## Missing Records

# ### Find out total records in the dataset

# In[8]:


data.shape


# ### Number of valid records per column

# In[9]:


data.count()


# ## Dropping missing records

# ### Drop all records that have  one or more missing values

# In[10]:


data_missing_dropped = data.dropna()
data_missing_dropped.shape


# ### Drop only those rows that have all records missing

# In[11]:


data_all_missing_dropped = data.dropna(how="all")
data_all_missing_dropped.shape


# ## Fill in missing data

# ### Fill in missing data with zeros

# In[10]:


data_filled_zeros =  data.fillna(0)
data_filled_zeros.count()


# ### Fill in missing data with a mean of the values from other rows

# In[12]:


data_filled_in_mean = data.copy()
data_filled_in_mean.Age.fillna(data.Age.mean(), inplace=True)
data_filled_in_mean.count()


# ## Default Index

# In[5]:


data.head()


# ## Set an Index post reading of data

# In[6]:


data.set_index('Name')


# ## Set an Index while reading data

# In[1]:


data = pd.read_csv('data-titanic.csv', index_col=3)
data.head()


# ## Selection using Index

# In[8]:


data.loc['Braund, Mr. Owen Harris',:]


# ## Reset Index

# In[9]:


data.reset_index(inplace=True)


# In[10]:


data.head()


# ## Remove column(s)

# ### Remove one column

# In[5]:


data.drop('Ticket', axis=1, inplace=True)


# In[6]:


data.head()


# ### Remove more than one column

# In[7]:


data.drop(['Parch', 'Fare'], axis=1, inplace=True)


# In[8]:


data.head()


# ## Remove row(s)

# In[9]:


data.drop(['Braund, Mr. Owen Harris', 'Heikkinen, Miss. Laina'], inplace=True)


# In[10]:


data.head()


# ## Renaming Columns

# ## Rename columns while reading the data

# In[5]:


list_columns = ['Date', 'Region ID', 'Region Name', 'State',
             'City', 'County', 'Size Rank','Price']
data = pd.read_csv('data-zillow.csv', names = list_columns)
data.head()


# ## Rename columns using rename method

# ### Read in the dataset again

# In[4]:


data = pd.read_csv('data-zillow.csv')
data.head()


# ### Rename 

# In[7]:


data.columns


# In[8]:


data.rename(columns={'RegionName':'Region', 'Metro':'City'}, inplace=True)


# In[9]:


data.columns


# ## Rename all columns

# In[12]:


data.columns = ['Date', 'Region ID', 'Region Name', 'State',
             'City', 'County', 'Size Rank','Price']


# In[ ]:




