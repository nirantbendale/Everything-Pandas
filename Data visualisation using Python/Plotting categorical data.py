#!/usr/bin/env python
# coding: utf-8

# ### Import Modules

# In[4]:


import pandas as pd
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# ### The dataset

# In[14]:


df = pd.read_csv('data_simpsons_episodes.csv')
df.head()


# ### Scatterplots

# In[6]:


sns.stripplot(x="season", y="us_viewers_in_millions", data=df);


# ### Swarmplot

# In[7]:


sns.swarmplot(x="season", y="us_viewers_in_millions", data=df);


# ### Boxplot

# In[8]:


sns.boxplot(x="season", y="us_viewers_in_millions", data=df);


# ### Violinplot

# In[9]:


sns.violinplot(x="season", y="us_viewers_in_millions", data=df);


# ### Barplot

# In[10]:


sns.barplot(x="season", y="us_viewers_in_millions", data=df);


# In[11]:


sns.countplot(x="season", data=df);


# ### Wide form plots

# In[19]:


df = pd.read_csv('data-alcohol.csv')
df.head()


# In[20]:


sns.boxplot(data=df, orient="h");


# In[ ]:




