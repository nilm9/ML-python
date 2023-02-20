#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as p


# In[32]:


data = pd.read_csv("https://raw.githubusercontent.com/joanby/python-ml-course/master/datasets/customer-churn-model/Customer%20Churn%20Model.txt")
data


# In[81]:


accLen = data["State"]
data.plot(alpha=.4)


# In[56]:


#We select  the data that we need
wantedCols = ["Account Length","Phone","Eve Charge","Day Calls"]


# In[57]:


wantedCols


# In[58]:


allColumnsList = data.columns.values.tolist()
allColumnsList


# In[70]:


#Loop for choosing the complementary
subList = [x for x in allColumnsList if x not in wantedCols ]


# In[71]:


subListe = [x for x in allColumnsList if x not in wantedCols ]


# In[72]:


data1 = data[subList]


# In[73]:


data1


# In[74]:


# alternatively
# a = set(desired_columns)
# b = set(all_columns_list)
# sublist = b-a
# sublist = list(sublist)


# In[75]:


#Get the first 25 rows!!
data[1:10] #==data[:10]


# In[76]:


#we filter the ones bigger than 
dataB = data[data["Day Charge"]>25]
dataB


# In[77]:


nyUser = data[(data["State"]=="NY") | (data["Eve Mins"]>10.0)]
nyUser.shape


# In[80]:


#tecnica ancestral
subsetFirst50 = data[["Day Mins","Night Mins","State"]][:50]
subsetFirst50.shape


# In[84]:


#check indexes: files i cols
data.iloc[:10, 3:6]
data.iloc[:, 3:6] #totes fils
data.iloc[:10, :] #totes cols


# In[ ]:




