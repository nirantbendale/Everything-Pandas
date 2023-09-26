#!/usr/bin/env python
# coding: utf-8

# ## Import Pandas

# In[15]:


import pandas as pd


# ## Read in the dataset

# In[16]:


data = pd.read_table('data-zillow.csv', sep=',')
data.head()


# ## Usage of axis parameter

# In[25]:


data.head()


# In[17]:


data.axes


# ## axis usage examples

# ## axis = 0

# In[18]:


data.mean(axis=0)


# ## axis = 1

# In[26]:


data.mean(axis=1).head()


# ## use labels instead of 0 and 1

# In[27]:


data.mean(axis='rows')


# In[29]:


data.mean(axis='columns').head()


# In[22]:


data.drop(0, axis=0).head()


# In[23]:


data.drop('Date', axis=1).head()


# In[24]:


data.filter(regex='Region', axis=1).head()


# In[ ]:




