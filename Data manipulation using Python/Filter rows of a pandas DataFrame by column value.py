#!/usr/bin/env python
# coding: utf-8

# ## Import Pandas

# In[3]:


import pandas as pd


# ## Read in the dataset

# In[4]:


data = pd.read_table('data-zillow.csv', sep=',')
data.head()


# ## Filter columns by name using filter()

# In[11]:


filtered_data = data.filter(items=['State', 'Metro'])
filtered_data.head()


# ## Filter columns by regular expression using filter()

# In[12]:


filtered_data = data.filter(regex='Region', axis=1)
filtered_data.head()


# ## Filter data using boolean indexing

# In[8]:


price_filter_series = data['Zhvi'] > 500000
price_filter_series.head()


# In[9]:


data[price_filter_series].head()


# ## An alternative way to filter

# In[10]:


data[data.Zhvi >= 1000000].head()


# In[ ]:




