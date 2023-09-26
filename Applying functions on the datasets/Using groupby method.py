#!/usr/bin/env python
# coding: utf-8

# ## Import Pandas

# In[2]:


import pandas as pd


# ## Read in the dataset

# In[3]:


data = pd.read_csv('data-zillow.csv')
data.head()


# ## Get Mean price for every State

# In[7]:


grouped_data = data[['State', 'Price']].groupby('State').mean()
grouped_data.head()


# ## Split the data into groups

# In[8]:


grouped_data = data[['State', 'Price']].groupby('State')


# In[9]:


list(grouped_data)


# ## Apply a function on each group and combine the results

# In[10]:


grouped_data.mean().head()


# ## Get Descriptive statistics by Groups(States)

# In[11]:


grouped_data.describe()


# ## Group by data on State and Region 

# In[16]:


grouped_data = data[['State',
                     'RegionName', 
                     'Price']].groupby(['State','RegionName']).mean()
grouped_data.head()


# ## Get the number of records per State

# In[13]:


grouped_data = data.groupby(['State']).size()
grouped_data


# ## Group by Columns

# In[14]:


grouped_data = data.groupby(data.dtypes, axis=1)
list(grouped_data)


# ## Iterate over Groups

# In[15]:


for state, grouped_data in data.groupby('State'):
    print(state, '\n', grouped_data)


# In[ ]:




