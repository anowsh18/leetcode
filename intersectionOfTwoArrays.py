#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Solution:
    def intersect(self, nums1, nums2):
        from collections import Counter
        if len(nums1)>len(nums2):
            f=nums2
            l=nums1
        else:
            f=nums1
            l=nums2
        f=Counter(f)
        l=Counter(l)
        x=[]
        for i,j in f.items():
            if i in l.keys():
                x.extend([i]*min(f[i],l[i]))     
        return(x)


# In[5]:





# In[4]:


sol.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12])# returns True


# In[ ]:




