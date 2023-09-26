#!/usr/bin/env python
# coding: utf-8

# ## Import Pandas

# In[2]:


import pandas as pd


# ## Read in the dataset

# In[3]:


data = pd.read_table('data-zillow.csv', sep=',')
data.head()


# ## Filtering based on multiple conditions 

# In[4]:


data[(data['Zhvi'] > 1000000) & (data['State'] == 'NY')].head()


# ## Filtering on  multiple conditions - OR

# In[5]:


data[((data['State'] == 'CA') | (data['State'] == 'NY'))].head()


# ## Filtering using `isin` method

# In[6]:


filter = data['Metro'].isin(['New York', 'San Francisco'])
data[filter].head()


# ## Using `isin` method with multiple conditions

# In[7]:


filter = data.isin({'State': ['CA'], 'Metro': ['San Francisco']})
data[filter].head()


# In[ ]:




