#!/usr/bin/env python
# coding: utf-8

# ## Import Pandas

# In[19]:


import pandas as pd


# ## Concatenate Dataset DataFrames

# In[38]:


dataset1 = pd.DataFrame({'Age': ['32', '26', '29'],
                         'Sex': ['F', 'M', 'F'],
                         'State': ['CA', 'NY', 'OH']},
                         index=['Jane', 'John', 'Cathy'])
    
dataset2 = pd.DataFrame({'Age': ['34', '23', '24', '21'],
                         'Sex': ['M', 'F', 'F', 'F'],
                         'State': ['AZ', 'OR', 'CA', 'WA']},
                         index=['Dave', 'Kris', 'Xi', 'Jo'])


# In[39]:


pd.concat([dataset1, dataset2])


# ## Concatenate using append()

# In[32]:


dataset1.append(dataset2)


# ## Concatenate on columns

# In[40]:


dataset1 = pd.DataFrame({'Age': ['32', '26', '29'],
                         'Sex': ['F', 'M', 'F'],
                         'State': ['CA', 'NY', 'OH']},
                         index=['Jane', 'John', 'Cathy'])

dataset2 = pd.DataFrame({'City': ['SF', 'NY', 'Columbus'],
                         'Work Status': ['No', 'Yes', 'Yes']},
                         index=['Jane', 'John', 'Cathy'])    


# In[41]:


pd.concat([dataset1, dataset2], axis=1)


# ### Merging DataFrames

# In[20]:


dataset1 = pd.DataFrame({'Name': ['Jane', 'John', 'Cathy', 'Sarah'],
                         'Age': ['32', '26', '29', '23'],
                         'Sex': ['F', 'M', 'F', 'F'],
                         'State': ['CA', 'NY', 'OH', 'TX']})

dataset2 = pd.DataFrame({'Name': ['Jane', 'John', 'Cathy', 'Rob'],
                        'City': ['SF', 'NY', 'Columbus', 'Austin'],
                         'Work Status': ['No', 'Yes', 'Yes', 'Yes']})


# In[25]:


pd.merge(dataset1, dataset2, on='Name', how='inner')


# ### Left outer merge

# In[26]:


pd.merge(dataset1, dataset2, on='Name', how='left')


# ### Right outer merge

# In[27]:


pd.merge(dataset1, dataset2, on='Name', how='right')


# ### Full outer merge

# In[28]:


pd.merge(dataset1, dataset2, on='Name', how='outer')


# In[ ]:




