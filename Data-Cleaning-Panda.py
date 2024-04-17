#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_excel(r"Downloads\Customer Call List (1).xlsx")
df


# In[3]:


df = df.drop_duplicates()
df


# In[4]:


df = df.drop(columns = "Not_Useful_Column")
df


# In[5]:


df["Last_Name"] = df["Last_Name"].str.strip("123._/")
df


# In[6]:


df["Phone_Number"] = df["Phone_Number"].str.replace('nan--','')

df["Phone_Number"] = df["Phone_Number"].str.replace('Na--','')
df


# In[10]:


df[["Street_Address", "State", "Zip_Code"]] = df["Address"].str.split(',', n=2, expand=True)
df


# In[11]:


df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('Yes','Y')

df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('No','N')
df


# In[12]:


df=df.fillna('')
df


# In[13]:


for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == 'Y':
        df.drop(x, inplace=True)

df


# In[14]:


for x in df.index:
    if df.loc[x, "Phone_Number"] == '':
        df.drop(x, inplace=True)

df


# In[15]:


df = df.reset_index(drop=True)
df


# In[ ]:




