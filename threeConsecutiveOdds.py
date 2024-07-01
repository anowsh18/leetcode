#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Solution:
    def threeConsecutiveOdds(self, arr):
        for  i in range(0,len(arr)-2):
            if arr[i]%2!=0 and arr[i+1]%2!=0 and arr[i+2]%2!=0:
                return True
        return False


# In[5]:


sol=Solution() #object
sol.threeConsecutiveOdds([2,6,4,1]) # return Fasle


# In[4]:


sol.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12])# returns True


# In[ ]:




