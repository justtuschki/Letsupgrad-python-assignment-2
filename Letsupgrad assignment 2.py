#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Remove empty List from List 


# In[3]:


test_list = [5, 6, [], 3, [], [], 9] 
print("The original list is : " + str(test_list))
res = [ele for ele in test_list if ele != []] 
print ("List after empty list removal : " + str(res))


# In[ ]:


#Given a sentence containing n words/strings. Remove all duplicates words/strings which are similar to each others.


# In[12]:



  s = "Python is great and Java is also great"
l = s.split() 
k = [] 
for i in l: 
  
    # If condition is used to store unique string  
    # in another list 'k'  
    if (s.count(i)>1 and (i not in k)or s.count(i)==1): 
        k.append(i) 
print(' '.join(k)) 
     


# In[ ]:


#program to find all occurrences of a character in the given string


# In[20]:


test_str = "Letsupgrade"
count = 0
  
for i in test_str: 
    if i == 'e': 
        count = count + 1
        print ("Count of e in Letsupgrade is : "
                            +  str(count)) 


# In[ ]:




