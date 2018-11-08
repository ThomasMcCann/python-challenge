#!/usr/bin/env python
# coding: utf-8

# In[28]:


import os


# In[29]:


import csv


# In[30]:


import pandas as pd


# In[31]:


cd 10.31.18


# In[32]:


pybank = 'pybank.csv'
pybank_df = pd.read_csv("pybank.csv")
pybank_df.head()


# In[99]:


total_months = pybank_df.shape[0]
total_profit = pybank_df["Profit/Losses"].sum()
average_change = pybank_df["Profit/Losses"].mean()
biggest_increase = pybank_df["Profit/Losses"].max()
biggest_decrease = pybank_df["Profit/Losses"].min()


# In[101]:


print("Financial Analysis")
print("------------------------------")
print ("Total Months: " + str(total_months))
print ("Total: $" + str(total_profit))
print ("Average Change: $" + str(average_change))
print("Greatest Increase: $" +str(biggest_increase))
print("Greatest Decrease: $" + str(biggest_decrease))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




