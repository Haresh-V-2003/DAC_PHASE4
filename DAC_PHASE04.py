#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import matplotlib.pyplot as plt


# In[28]:


import numpy as np


# In[30]:


import seaborn as sns


# In[4]:


data=pd.read_csv("C:\DAC\DAC_PHASE1\DAC_Dataset.csv")


# In[5]:


x=(data['Stn Code'])


# In[6]:


y=(data['NO2'])


# In[7]:


plt.plot(x)


# In[19]:


plt.bar(x,y,width=50)


# In[22]:


xpos=np.arange(len(x))


# In[24]:


plt.plot(xpos,y)


# In[27]:


plt.bar(xpos,y)


# In[33]:


heat=data[['Stn Code','NO2','SO2']]


# In[34]:


heat.head()


# In[41]:


df_corr=heat.corr()


# In[43]:


figure=plt.figure(figsize=(20,15))


# In[44]:


sns.heatmap(df_corr,annot=True,fmt='fig')
plt.show()


# In[45]:


sulphur=(data['SO2'])


# In[46]:


plt.plot(xpos,sulphur,'r')


# In[47]:


plt.bar(xpos,sulphur)


# In[53]:


plt.stackplot(data["Stn Code"],data["SO2"],data["NO2"])


# In[54]:


plt.scatter(xpos,sulphur)


# In[55]:


nitrogen=y


# In[57]:


plt.scatter(xpos,nitrogen,c='r')


# In[ ]:




