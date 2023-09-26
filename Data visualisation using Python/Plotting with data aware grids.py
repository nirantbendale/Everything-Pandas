#!/usr/bin/env python
# coding: utf-8

# ## Import Modules

# In[3]:


import pandas as pd
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# ## Read in the dataset

# In[6]:


df = pd.read_csv('data-titanic.csv')
df.head()


# ### Plotting with `FacetGrid()`

# In[20]:


g = sns.FacetGrid(df, col="Sex", hue='Survived')
g.map(plt.hist, "Age");
g.add_legend();


# ### Plotting with `PairGrid()` 

# ### MLB Players Height, Weight, Age and Positions dataset

# In[14]:


mlb = pd.read_csv('data-mlb-players.csv')
mlb.head()


# Data from
# 
# http://wiki.stat.ucla.edu/socr/index.php/SOCR_Data_MLB_HeightsWeights

# ### Plot it with `PairGrid()`

# In[20]:


g = sns.PairGrid(mlb, vars=["Height", "Weight"], hue="Position")
g.map(plt.scatter);
g.add_legend();


# ### Plotting with `PairPlot()`

# In[17]:


sns.pairplot(mlb, hue="Position", size=2.5);


# In[ ]:




