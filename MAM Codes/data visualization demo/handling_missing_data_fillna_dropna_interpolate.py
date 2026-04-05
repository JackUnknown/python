#!/usr/bin/env python
# coding: utf-8

# ## <font color="maroon"><h4 align="center">Handling Missing Data - fillna, interpolate, dropna</font>

# In[11]:


#data cleaning/data munging
import pandas as pd
df = pd.read_csv("weather_data_missing.csv")
#df = pd.read_csv("weather_data_missing.csv",index_col='day',parse_dates=['day'])
#df = pd.read_csv("weather_data_missing.csv",skiprows =3,parse_dates=['day'])
#type(df.day[0])
df


# In[21]:


#df.set_index('day',inplace=True)
#df.loc["01-07-2017"]
df
df.info()
#df.isnull()
import seaborn as sns
#sns.heatmap(df.isnull(),yticklabels=False,cmap="viridis")
sns.color_palette("rocket", as_cmap=True)
sns.heatmap(df.isnull(),yticklabels=False,cmap="YlGnBu")


# In[ ]:





# In[15]:


#df.reset_index('day',inplace=True)
df.reset_index(inplace=True)
df
#df.info()


# ## <font color="blue">fillna</font>

# <font color="purple">**Fill all NaN with one specific value**</font>

# In[31]:


#thresh= 2 Require that minimum 2 non-NA values.
#new_df=df.dropna(thresh=2)
new_df = df.fillna(0)
new_df
new_df.info()


# <font color="purple">**Fill na using column names and dict**</font>

# In[3]:


new_df = df.fillna({
        'temperature': 0,
        'windspeed': 1,
        'event': 'No Event'
    })
new_df


# In[ ]:


new_df=df.copy()
new_df['temperature'].fillna(new_df['temperature'].mean(),inplace=True)
new_df['windspeed'].fillna(new_df['windspeed'].mean(),inplace=True)
new_df


# <font color="purple">**Use method to determine how to fill na values**</font>

# In[4]:


df
new_df = df.fillna(method="ffill") #forward fill
new_df


# In[ ]:


#ffill on specific column
new_df=df.loc[:,'windspeed'].ffill()
new_df


# In[5]:


new_df = df.fillna(method="bfill")
new_df


# <font color="purple">**Use of axis**</font>

# In[ ]:


new_df = df.fillna(method="bfill", axis="columns") # axis is either "index" or "columns"
new_df


# <font color="purple">**limit parameter**</font>

# In[7]:


#limit will specify how many values should get replace
new_df = df.fillna(method="ffill",limit=2)
#new_df = df.fillna(method="ffill")
new_df


# ### <font color="blue">interpolate</font>

# In[6]:


new_df = df.interpolate()
new_df


# In[ ]:


new_df = df.interpolate() 
new_df


# In[8]:



df['temperature f']=df['temperature'].map(lambda x:x+10)
df



# In[ ]:


def myconvert(num):
    if num<30:
        return num+10
    elif num>=30 and num<35:
        return num+20
    else:
        return num+30
    
df['temperature f']=df['temperature'].apply(myconvert) 
df


# **Notice that in above temperature on 2017-01-04 is 29 instead of 30 (in plain linear interpolate)**

# **There are many other methods for interpolation such as quadratic, piecewise_polynomial, cubic etc. 
# Just google "dataframe interpolate" to see complete documentation**

# ### <font color="blue">dropna</font>

# In[ ]:


new_df = df.dropna()    
new_df


# In[ ]:


new_df =df .dropna(how='all')
new_df


# In[ ]:


new_df = df.dropna(thresh=2)
new_df
#less that 2 not null values
  


# ### <font color="blue">Inserting Missing Dates</font>

# In[ ]:


dt = pd.date_range("01-01-2017","01-11-2017")
idx = pd.DatetimeIndex(dt)
df.reindex(idx)

