#!/usr/bin/env python
# coding: utf-8

# ## Import Pandas

# In[41]:


import pandas as pd


# ## Read in the dataset

# In[42]:


zillow = pd.read_table('data-zillow.csv', sep=',')


# ## Looking at the data

# In[43]:


zillow.head()


# ## Select single row, single column

# In[44]:


zillow.loc[7, 'Metro']


# In[45]:


zillow.iloc[7,4]


# ## Select single row, multiple columns

# In[46]:


zillow.loc[7, ['Metro', 'County']]


# In[47]:


zillow.iloc[7, [4,5]]


# ## Select single row, all columns

# In[48]:


zillow.loc[11, :]


# ## Select multiple rows, single column

# In[49]:


zillow.loc[101:105, 'Metro']


# ## Select multiple rows and multiple contiguous columns 

# In[50]:


zillow.loc[201:204, "State":"County"]


# In[51]:


zillow.iloc[201:205, 3:6]


# ## Select multiple rows and multiple non-contiguous columns
# 

# In[52]:


zillow.loc[201:205, ['RegionName', 'State']]


# 
# ## Select multiple rows and all columns

# In[53]:


zillow.loc[201:205, :]


# ## Select non-contiguous rows

# In[54]:


zillow.loc[[0,5,10], :]


# 
# ## Selecting rows based on a  specific column's value

# In[55]:


zillow.loc[zillow.County=="Queens"]


# ## Selecting all rows for a specific column based on a value of another column 

# In[56]:



zillow.loc[zillow.Metro=="New York", "County"]


# In[ ]:




