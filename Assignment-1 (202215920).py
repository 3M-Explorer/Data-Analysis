#!/usr/bin/env python
# coding: utf-8

# # Assignment 1
# 
# ### ID: g202215920

# ### Task: Create two columns that contains letter grades related to both reading and writing scores. 

# In[1]:


import pandas as pd
#importing pandas modulue
from tabulate import tabulate


# In[2]:


location = './Downloads/Studentsperformance.csv'
# Specifying file location
# Main Code: './location/filename.type'
df = pd.read_csv(location)
# reading the from the location
df.head()
# Display data (by default 5)


# In[3]:


df[['reading_score', 'writing_score']].head()
# Displaying data from the given dataframe


# In[4]:


data = {
    'Key1': df['reading_score'],
    'Key2': df['writing_score']
}

# Creating a directory that contain information about reading_score and writing_score


# In[5]:


new_df = pd.DataFrame(data)
# Creating new dataframe using directory


# In[6]:


def score_to_grade(score):
    if score <= 30:
        return 'F'
    elif score <= 66:
        return 'D'
    elif score <= 75:
        return 'C'
    elif score <= 90:
        return 'B'
    else:
        return 'A'
# Applying condition statment by defining new function


# In[7]:


df['reading_grade'] = df['reading_score'].apply(score_to_grade)
df['writing_grade'] = df['writing_score'].apply(score_to_grade)


# In[8]:


print(tabulate(df[['reading_grade', 'writing_grade']].head(10), headers='keys', tablefmt='grid'))


# In[ ]:




