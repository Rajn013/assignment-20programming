#!/usr/bin/env python
# coding: utf-8

# Create a function that takes a list of strings and integers, and filters out the list so that it returns a list of integers only.
# 

# In[9]:


def filter_list(lst):
    result = []
    for items in lst:
        if isinstance(items, int):
            result.append(items)
    return result


# In[10]:


filter_list([1, 2, 3, "a", "b", 4])


# In[11]:


filter_list(["A", 0, "Edabit", 1729, "Python", "1729"])


# In[12]:


filter_list(["Nothing", "here"]) 


# Given a list of numbers, create a function which returns the list but with each element's index in the list added to itself. This means you add 0 to the number at index 0, add 1 to the number at index 1, etc...
# 

# In[13]:


def add_indexes(lst):
    return [i + lst[i] for i in range(len(lst))]


# In[15]:


add_indexes([0, 0, 0, 0, 0])


# In[16]:


add_indexes([1, 2, 3, 4, 5])


# In[17]:


add_indexes([5, 4, 3, 2, 1])


# Create a function that takes the height and radius of a cone as arguments and returns the volume of the cone rounded to the nearest hundredth. See the resources tab for the formula.
# 

# In[19]:


import math

def cone_volume(height, radius):
    volume =(1/3) * math.pi * radius**2 * height
    return round(volume, 2)


# In[20]:


cone_volume(3, 2)


# In[21]:


cone_volume(15, 6)


# In[22]:


cone_volume(18, 0)


# This Triangular Number Sequence is generated from a pattern of dots that form a triangle. The first 5 numbers of the sequence, or dots, are: 
# 1, 3, 6, 10, 15
# This means that the first triangle has just one dot, the second one has three dots, the third one has 6 dots and so on.
# Write a function that gives the number of dots with its corresponding triangle number of the sequence.
# 

# In[23]:


def triangle(n):
    triangle = (n * (n+1)) // 2
    return triangle


# In[24]:


triangle(1)


# In[25]:


triangle(6)


# In[26]:


triangle(215)


# In[27]:


def missing_num(lst):
    for i in range(1, 11):
        if i not in lst:
            return i


# In[28]:


missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10])


# In[29]:


missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8])


# In[30]:


missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9])


# In[ ]:




