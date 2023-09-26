#!/usr/bin/env python
# coding: utf-8

# ## Import Pandas

# In[3]:


import pandas as pd


# ## Read in the dataset

# In[4]:


zillow = pd.read_table('data-zillow.csv', sep=',')
zillow.head()


# ## Simple sort

# In[5]:


zillow.sort_values('Metro')


# ## Changing the sort order

# In[6]:


sorted = zillow.sort_values('Metro', ascending=False)
sorted.head()


# ## Sort by more than one column 

# In[7]:


sorted = zillow.sort_values(by=['Metro','County'])
sorted.head()


# ## Sort by multiple columns and mixed ascending order

# In[8]:


sorted = zillow.sort_values(by=['Metro','County', 'Zhvi'], 
                            ascending=[True, True, False])
sorted.head()


# ## Sort a Series

# ### Let's create a Series object

# In[9]:


regions = zillow.RegionID
type(regions)


# ### Let's sort the series

# #### Original Series

# In[10]:


regions.head()


# #### Sorted

# In[11]:


regions.sort_values().head()


# In[ ]:




