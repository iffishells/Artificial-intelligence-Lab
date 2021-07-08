#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Queue:

    def __init__(self):
        self.size=5
        self.q = list(range(self.size))
        self.i = 0
        self.o = 0

        self.is_empty = True
        self.is_full = False

def inc(self,idx):

    if idx + 1 ==self.size:
        return 0
    else:
        return idx +1
Queue.inc = inc

  
def enqueue(self,val):

    if self.is_full:
        raise IndexError("Queue is full ,You can't be Enqueue")

    self.q[self.i] = val
    self.i = self.inc(self.i)

    if self.i == self.o:
        self.is_full = True

    self.is_empty = False

Queue.enqueue = enqueue

def dequeue(self):

    if self.is_empty:
        raise IndexError("Queue is empty you can't be dequeue")

    ret = self.q[self.o]
    self.o = self.inc(self.o)

    if self.i == self.o:
        self.is_empty = True

    self.is_ful = False
    return ret

Queue.dequeue = dequeue


def __str__(self):
    return str(self.q) + " , in : "+str(self.i) + " , out: "+ str(self.o)

Queue.__str__=__str__


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

# q.enqueue(50)  will get error

# print(q)

print(q.dequeue())


# In[ ]:




