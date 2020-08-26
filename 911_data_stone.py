#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df=pd.read_csv('F:/Py-DS-ML-Bootcamp-master/Refactored_Py_DS_ML_Bootcamp-master/10-Data-Capstone-Projects/911.csv')


# In[5]:


df.info()


# In[6]:


df.head(3)


# In[7]:


s=df['zip'].value_counts().nlargest(5)
print(s)


# In[8]:


k=df['twp'].value_counts().nlargest(5)
print(k)


# In[9]:


df['title'].nunique()


# In[20]:


df['Reason']=df.title.apply(lambda x:pd.Series(str(x).split(':')[0]))


# In[11]:


df['Reason'].value_counts()


# In[12]:


sns.countplot(df.Reason)


# In[24]:


df['timeStamp']=pd.to_datetime(df['timeStamp'])


# In[8]:


type(df['timeStamp'].iloc[0])


# In[9]:


df['timeStamp']=df['timeStamp'].apply(pd.to_datetime)


# In[13]:


df['Hour']=df['timeStamp'].apply(lambda time:time.hour)
df['Hour']


# In[16]:


time = df['timeStamp'].iloc[0]
time.day


# In[28]:


df['Month']=df['timeStamp'].apply(lambda time:time.month)
df['Day of Week']=df['timeStamp'].apply(lambda time:time.dayofweek)
df.head()


# In[30]:


dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of Week']=df['Day of Week'].map(dmap)


# In[32]:


df.head()


# In[36]:


plt.figure(figsize=[10,6])
sns.countplot(df['Day of Week'],hue=df['Reason'])


# In[46]:


plt.figure(figsize=[10,6])
sns.countplot(df['Month'],hue=df['Reason'],palette='viridis')


# In[47]:


bymonth=df.groupby(df['Month']).count()
bymonth.head()


# In[52]:


bymonth['lat'].plot()


# In[54]:


sns.lmplot(x='Month',y='twp',data=bymonth.reset_index())


# In[60]:


df['Date']=df['timeStamp'].apply(lambda t:t.date())
df.head()


# In[69]:


plt.figure(figsize=[10,6])
df.groupby(df['Date']).count()['lat'].plot()


# In[82]:


plt.figure(figsize=[10,6])
df[df['Reason']=='EMS'].groupby(df['Date']).count()['lat'].plot()


# In[84]:


plt.figure(figsize=[10,6])
df[df['Reason']=='Traffic'].groupby(df['Date']).count()['lat'].plot()


# In[86]:


plt.figure(figsize=[10,6])
df[df['Reason']=='Fire'].groupby(df['Date']).count()['lat'].plot()


# In[103]:


dow=df.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack()
plt.figure(figsize=[10,6])
sns.heatmap(dow,cmap='magma')


# In[105]:


sns.clustermap(dow,cmap='magma')


# In[110]:


mow=df.groupby(by=['Day of Week','Month']).count()['Reason'].unstack()


# In[114]:


plt.figure(figsize=[15,6])
sns.heatmap(mow,cmap='magma')


# In[118]:


plt.figure(figsize=[15,6])
sns.clustermap(mow,cmap='magma')


# # A special thanks to Jose Portilla Sir, for his wonderful Lectures
