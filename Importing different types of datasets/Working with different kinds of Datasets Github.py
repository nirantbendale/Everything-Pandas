#!/usr/bin/env python
# coding: utf-8

# # Using advanced options while reading data from csv files

# ## Import Module(s)

# In[1]:


import pandas as pd


# ## The most basic read

# In[2]:


df = pd.read_csv('IMDB.csv', encoding = "ISO-8859-1")
df.head()


# ## Advanced read options

# ## Manipulating Column & Index Locations and Names

# ### No header or column names

# In[3]:


df = pd.read_csv('IMDB.csv', encoding = "ISO-8859-1", header=None)
df.head()


# ### Specify a different row as header

# In[4]:


df = pd.read_csv('IMDB.csv', encoding = "ISO-8859-1", header=2)
df.head()


# ### Specify a column as index

# In[5]:


df = pd.read_csv('IMDB.csv', encoding = "ISO-8859-1", index_col='Title')
df.head()


# ### Choose only a subset of columns to be read

# In[6]:


df = pd.read_csv('IMDB.csv', encoding = "ISO-8859-1", usecols=['Title', 'Genre1'])
df.head()


# ### Handling Missing and NA data

# ```
# NaN: ”, ‘#N/A’, ‘#N/A N/A’, ‘#NA’, ‘-1.#IND’, ‘-1.#QNAN’, ‘-NaN’, ‘-nan’, ‘1.#IND’, ‘1.#QNAN’, ‘N/A’, ‘NA’, ‘NULL’, ‘NaN’, ‘nan’`.
# ```

# In[7]:


df = pd.read_csv('IMDB.csv', encoding = "ISO-8859-1", na_values=[''])


# ### Choose whether to skip over blank rows or not

# In[8]:


df = pd.read_csv('IMDB.csv', encoding = "ISO-8859-1", skip_blank_lines=False)


# ## Data Parsing options

# ### Skip rows

# In[9]:


df = pd.read_csv('IMDB.csv', encoding = "ISO-8859-1", skiprows = [1,3,7])
df.head()


# ### Skip rows from footer or from end of the file

# In[10]:


df.tail(2)
df = pd.read_csv('IMDB.csv', encoding = "ISO-8859-1", skipfooter=2, engine='python')
df.tail(2)


# ### Reading only a subset of the file or a certain number of rows

# In[11]:


df = pd.read_csv('IMDB.csv', encoding = "ISO-8859-1", nrows=100)
df.shape


# # Reading data from excel files

# ## Basic Excel read 

# In[12]:


df = pd.read_excel('IMDB.xlsx')
df.head()


# ## Advanced read options

# ```
# pandas.read_excel(io, sheetname=0, header=0, skiprows=None, skip_footer=0, index_col=None, names=None, parse_cols=None, parse_dates=False, date_parser=None, na_values=None, thousands=None, convert_float=True, has_index_names=None, converters=None, dtype=None, true_values=None, false_values=None, engine=None, squeeze=False, **kwds)
# ```
# 
# **from [Pandas Doc](http://pandas.pydata.org/pandas-docs/version/0.20/generated/pandas.read_excel.html)

# ### Which Sheet to read?

# In[13]:


df = pd.read_excel('IMDB.xlsx', sheet_name=0)
df.head()


# ## Reading data from multiple sheets in an excel file

# ## Find out the sheet list of the excel file

# In[14]:


xls_file = pd.ExcelFile('IMDB.xlsx')
xls_file.sheet_names


# In[15]:


df1 = xls_file.parse('movies')
df2 = xls_file.parse('by genre')
df1.head()
df2.head()


# ## Choose Header or column labels

# In[16]:


df = pd.read_excel('IMDB.xlsx', sheet_name=1, header=3)
df.head()


# ## No header

# In[17]:


df = pd.read_excel('IMDB.xlsx', sheet_name=1, header=None)
df.head()


# ## Skip Rows at the beginning of the file

# In[18]:


df = pd.read_excel('IMDB.xlsx', sheet_name=1, skiprows=7)


# ## Skip rows from the end of the file

# In[19]:


df = pd.read_excel('IMDB.xlsx', sheet_name=1, skipfooter=10)


# ## Choose Columns

# In[20]:


df = pd.read_excel('IMDB.xlsx', sheet_name= 0, usecols=[0,1])
df.head()


# ## Column Names

# In[21]:


df = pd.read_excel('IMDB.xlsx', sheet_name=0, usecols=[0,1,2], names=['X','Title', 'Rating'], )
df.head()


# ## Set an Index while reading data

# In[22]:


df = pd.read_excel('IMDB.xlsx', sheet_name=0, index_col='Title')
df.head()


# ## Handle missing data while reading

# In[23]:


df = pd.read_excel('IMDB.xlsx', sheet_name= 0, na_values=[' '])


# # Reading data from some other popular formats

# ## Reading JSON data into Pandas

# In[24]:


movies_json = pd.read_json('IMDB.json')
movies_json.head()


# ## Reading HTML data

# In[25]:


pd.read_html('IMDB.html')


# ## Read a pickle file

# In[26]:


df = pd.read_pickle('IMDB.p')
df.head()


# ## Read SQL data

# In[27]:


import sqlite3


# In[28]:


conn = sqlite3.connect("IMDB.sqlite")
df = pd.read_sql_query("SELECT * FROM IMDB;", conn)
df.head()


# ## Read data from clipboard

# In[30]:


df = pd.read_clipboard()
df.head()


# In[ ]:




