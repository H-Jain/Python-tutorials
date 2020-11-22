#!/usr/bin/env python
# coding: utf-8

# In[1]:


#finding roots of a quadratic equation using simple iteration method for quadratic equation ax^2 + bx + c=0

import cmath
a=float (input ('enter a: '))
b=float (input ('enter b: '))
c=float (input ('enter c: '))
x=float (input ('enter x: ')) #initial guess i.e. enter the guessed root value

print('\n') 

for iteration in range (101):
    xn= (a *x**2 + c)/b #can also use xn=sqrt((-b-c)/a) and to define sqrt, mention  from math import sqrt
    print (iteration, x)
    if abs(xn-x)<0.000001:
        break
    x=xn
    print ('the root is: %0.5f' %xn)
    print ('the number of iterations: %d' %iteration)
    print()


# In[ ]:




