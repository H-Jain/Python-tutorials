#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = int(input())
b = int(input())
c= int (input())
if c ==1:
    sum= a+b
    print (sum)
elif c ==2:
    sub= a-b
    print (sub)
elif c==3:
    pro=a*b
    print (pro)
elif c ==4:
    div=a//b #use // for answer in integer, not in float. if in float, single /
    mod=a%b
    print (div, mod, sep="\n") #or (print (div, "\n", mod)
else:
    print ("error")


# In[ ]:




