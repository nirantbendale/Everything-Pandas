#!/usr/bin/env python
# coding: utf-8

# ## Import Pandas

# In[3]:


import pandas as pd


# ## Our dataset

# In[4]:


dataset = pd.DataFrame({'DOB': ['1976-06-01', '1980-09-23', '1984-03-30', '1991-12-31', '1994-10-2', '1973-11-11'],
                        'Sex': ['F', 'M', 'F', 'M', 'M', 'F'],
                        'State': ['CA', 'NY', 'OH', 'OR', 'TX', 'CA'],
                        'Name': ['Jane', 'John', 'Cathy', 'Jo', 'Sam', 'Tai']})


# In[5]:


dataset


# ## let's first convert our date column to `datetime`

# In[6]:


dataset.dtypes


# In[38]:


dataset.DOB = pd.to_datetime(dataset.DOB)


# In[7]:


dataset.dtypes


# ### Let's set index to the date column

# In[8]:


dataset.set_index('DOB', inplace=True)


# In[9]:


dataset


# ### Filter and select time series Data

# In[41]:


dataset['1980']


# In[42]:


dataset['1980':]


# In[43]:


dataset[:'1980']


# In[45]:



dataset['1980':'1984']


# In[51]:


dataset.reset_index(inplace=True)


# ### Get properties of date-time series data

# In[55]:


dataset.DOB.dt.dayofyear


# In[56]:


dataset.DOB.dt.weekday_name


# In[ ]:




