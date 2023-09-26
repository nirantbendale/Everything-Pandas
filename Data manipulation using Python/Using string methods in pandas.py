#!/usr/bin/env python
# coding: utf-8

# ## Import Pandas

# In[4]:


import pandas as pd


# ## Read in the dataset

# In[5]:


data = pd.read_table('data-zillow.csv', sep=',')
data.head()


# 
# ## Check for a substring

# In[13]:


data.RegionName.str.contains('New').head()


# ## Make values of a series or column uppercase

# In[7]:


data.RegionName.str.upper().head()


# ## Make values lowercase

# In[8]:


data.County.str.lower().head()


# ## Get the length of each value in a column

# In[10]:


data.County.str.len().head()


# ## Remove all whitespace from the beginning

# In[16]:


data.RegionName.str.lstrip().head()


# ## Replace parts of a column's values

# In[18]:


data.RegionName.str.replace(' ', '').head()


# In[ ]:




