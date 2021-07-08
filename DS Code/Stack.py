#!/usr/bin/env python
# coding: utf-8

# In[1]:


class stack:
    def __init__(self):
        self.l=[]
    
    def push(self,val):
        self.l.append(val)
  
    def pop(self):
        return self.l.pop()

    def peek(self):
        return self.l[-1] 
  


# In[2]:


s = stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)

print(s.peek())
print(s.pop())
print(s.peek())


# In[ ]:




