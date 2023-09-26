#!/usr/bin/env python
# coding: utf-8

# ## Import Modules

# In[3]:


import pandas as pd
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# ## The dataset

# In[4]:


df = pd.read_csv('data-alcohol.csv')
df.head()


# ### Color Palettes

# In[5]:


sns.palplot(sns.color_palette())


# ### Look at how these colors look on a plot

# In[6]:


sns.set()
sns.boxplot(data=df);


# ### Change the color palette

# In[6]:


sns.set_palette("bright")


# ### Impact on the plot

# In[7]:


sns.boxplot(data=df);


# ### `seaborn` palettes

# In[9]:


sns.palplot(sns.color_palette("deep", 7))


# In[10]:


sns.palplot(sns.color_palette("muted", 7))


# In[11]:


sns.palplot(sns.color_palette("pastel", 7))


# ### `seaborn` palettes

# In[12]:


sns.palplot(sns.color_palette("bright", 7))


# In[13]:


sns.palplot(sns.color_palette("dark", 7))


# In[14]:


sns.palplot(sns.color_palette("colorblind", 7))


# ### `matplotlib` colormaps as color palettes

# In[15]:


sns.palplot(sns.color_palette("RdBu", 7))


# In[16]:


sns.palplot(sns.color_palette("Blues_d", 7))


# ### Let's set the palette to a `matplotlib colormap`

# In[17]:


sns.set_palette("Blues_d")


# ### Impact on the plot

# In[18]:


sns.boxplot(data=df);


# ### Building custom color palettes

# In[19]:


my_palette = ['#4B0082', '#0000FF', '#00FF00', '#FFFF00', '#FF7F00', '#FF0000']
sns.set_palette(my_palette)
sns.palplot(sns.color_palette())


# ### Let's see how the plot has changed

# In[20]:


sns.boxplot(data=df);


# ### First plot with `seaborn`

# In[79]:


sns.distplot(df.beer_servings)


# ## Changing the plot style with `set_style`

# ### Set plot background to a white grid

# In[80]:


sns.set()
sns.set_style("whitegrid")
sns.lmplot(x='beer_servings', y='wine_servings', data=df);


# ### Set the plot background to dark

# In[81]:


sns.set()
sns.set_style("dark")
sns.lmplot(x='beer_servings', y='wine_servings', data=df, fit_reg=False);


# ### Set the background to white

# In[82]:


sns.set()
sns.set_style("white")
sns.swarmplot(x='country', y='wine_servings', data=df);


# ### Adding '`ticks`

# In[83]:


sns.set()
sns.set_style("ticks")
sns.boxplot(data=df);


# ## Customizing the styles

# ### Style parameters

# In[84]:


sns.axes_style()


# In[85]:


sns.set()
sns.set_style("ticks", {"axes.facecolor": ".1"})
sns.boxplot(data=df);


# ## Plotting Context Presets

# ### Plotting Context Preset - `paper`

# In[86]:


sns.set()
sns.set_context("paper")
sns.lmplot(x='beer_servings', y='wine_servings', data=df);


# ### Plotting Preset - `talk`

# In[87]:


sns.set()
sns.set_context("talk")
plt.figure(figsize=(8, 6))
sns.lmplot(x='beer_servings', y='wine_servings', data=df);


# ### Plotting Preset - `poster`

# In[88]:


sns.set()
sns.set_context("poster")
plt.figure(figsize=(8, 6))
sns.lmplot(x='beer_servings', y='wine_servings', data=df);


# In[ ]:




