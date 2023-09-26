#!/usr/bin/env python
# coding: utf-8

# ## Import Pandas

# In[4]:


import pandas as pd


# ## Read in the dataset

# In[5]:


data = pd.read_table('data-zillow.csv', sep=',')
data.head()


# ## Changing an int column to float

# In[6]:


data.dtypes


# In[7]:


data['Zhvi'] = data.Zhvi.astype(float)


# In[8]:


data.dtypes


# ## Changing datatype while reading data

# In[9]:


data2 = pd.read_csv('data-zillow.csv', sep=',', dtype={'Zhvi':float})
data2.dtypes


# ## Converting string to datetime 

# In[16]:


pd.to_datetime(data2.Date,infer_datetime_format=True).head()


# In[ ]:




