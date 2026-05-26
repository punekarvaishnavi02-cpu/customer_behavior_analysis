#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 

df=pd.read_csv("customer_shopping_behavior.csv")


# In[2]:


df.head()


# In[3]:


df.info()


# In[4]:


df.describe(include='all')


# In[5]:


df.isnull().sum()


# In[6]:


df['Review Rating']=df.groupby('Category')['Review Rating'].transform (lambda x:x.fillna(x.median()))


# In[7]:


df.isnull().sum()


# In[8]:


df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
df=df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})


# In[9]:


df.columns


# In[10]:


#Create new column age_group
labels=['young Adult','Adult','Middle-Age','Senior']
df['age_group']=pd.qcut(df['age'],q=4,labels=labels)


# In[11]:


df[['age','age_group']].head(10)


# In[12]:


#create column purchase_frequency_days

frequency_mapping = {
'Fortnightly': 14,
'Weekly': 7,
'Monthly': 30,
'Quarterly': 90,
'Bi-Weekly': 14,
'Annually': 365,
'Every 3 Months': 90}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)


# In[13]:


df[['purchase_frequency_days','frequency_of_purchases']].head(10)


# In[14]:


df[['discount_applied', 'promo_code_used']].head(10)


# In[15]:


(df['discount_applied']==df['promo_code_used']).all()


# In[16]:


df=df.drop('promo_code_used',axis=1)


# In[17]:


df.columns


# In[18]:


get_ipython().system('pip install sqlalchemy pymysql ')


# In[26]:


from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root@localhost:root123 @localhost/customer_beheviour")

df.to_sql(name='customer_beheviour', con=engine, if_exists='replace', index=False)

print("Done! Table loaded successfully!")


# In[24]:


#Connecting to MySQL 
engine = create_engine("mysql+pymysql://root:@localhost/customer_beheviour")


# In[30]:


#Code for connecting to MySQL
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:YOUR_WORKBENCH_PASSWORD@localhost/customer_beheviour")

df.to_sql(name='customer_beheviour', con=engine, if_exists='replace', index=False)

print("Done!")

