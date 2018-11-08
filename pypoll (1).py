#!/usr/bin/env python
# coding: utf-8

# In[102]:


import os


# In[103]:


import csv


# In[108]:


import pandas as pd


# In[109]:


cd 10.31.18


# In[110]:


pypoll = 'electiondata.csv'
pypoll_df = pd.read_csv("electiondata.csv")
pypoll_df.head()


# In[339]:


total_votes = pypoll_df.shape[0]
candidates = pypoll_df["Candidate"].unique()
number_votes = pypoll_df["Candidate"].value_counts()
percentage_votes = round(number_votes / total_votes*100)


print("Election Results")
print("------------------------------")
print ("Total votes: " + str(total_votes))
print("------------------------------")
for name in candidates:
  
    print (name + ": " + (str(percentage_votes) + "%" + str(number_votes)))
    print ("-------------------------------")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




