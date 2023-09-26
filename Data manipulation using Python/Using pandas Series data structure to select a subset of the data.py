#!/usr/bin/env python
# coding: utf-8

# ## Introduce our dataset

# * Data from Zillow.com, a real estate marketplace.
# * A public and free to use dataset, after attribution.
# * Real dataset which lists mean prices of houses in various locations in US.
# * Dataset is a csv or a comma separated values text file.
# * Available here - https://www.zillow.com/research/data/

# ## Import Pandas

# In[1]:


import pandas as pd


# ## Read in the dataset

# In[2]:


data = pd.read_table('data-zillow.csv', sep=',')


# ## View the dataset

# In[14]:


data.head()


# # Select data

# ### Select a Series with bracket notation

# In[20]:


regions = data['RegionName']


# In[21]:


type(regions)


# In[22]:


regions


# ## DataFrame vs Series

# ## Multi Column Selection - Series or DataFrame

# In[25]:


region_n_state = data[['RegionName', 'State']]
region_n_state.head()


# In[26]:


type(region_n_state)


# ## Select using dot notation

# In[28]:


data.State


# ## Creating a new series by selection

# In[29]:


data['Address'] = data.County + ', ' + data.Metro + ', ' + data.State


# In[31]:


data.Address


# In[ ]:




