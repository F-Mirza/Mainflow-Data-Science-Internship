#!/usr/bin/env python
# coding: utf-8

# LIST OPERATIONS
# 

# In[2]:


# Creating a list
list1 = [1, 2, 3, 4, 5]
print("Originally created list:", list1)


# In[3]:


# Adding elements to the list
list1.append(6)
print("List after adding element:", list1)


# In[4]:


# Removing an element from the list
list1.remove(4)
print("List after removing an element:", list1)


# In[5]:


# Modifying an element in the list
list1[1] = 25
print("List after modifying an element:", list1)


# DICTIONARY OPERATIONS

# In[6]:


# Creating a dictionary
dictionary = {'a': 10, 'b': 20, 'c': 30}
print("Originally created dictionary:", dictionary)


# In[7]:


# Adding a key-value pair to the dictionary
dictionary['d'] = 40
print("Dictionary after adding an element:", dictionary)


# In[8]:


# Removing a key-value pair from the dictionary
del dictionary['c']
print("Dictionary after removing an element:", dictionary)


# In[ ]:


# Modifying a value in the dictionary
dictionary['a'] = 100
print("Dictionary after modifying an element:", dictionary)


# SET OPERATIONS

# In[10]:


# Creating a set
sets = {5,15,25,35,45,55}
print("Originally created set:", sets)


# In[11]:


# Adding an element to the set
sets.add(65)
print("Set after adding an element:", sets)


# In[12]:


# Removing an element from the set
sets.remove(35)
print("Set after removing an element:", sets)


# cannot directly modify set elememts because sets are not indexed

# In[ ]:




