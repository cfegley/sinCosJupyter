#!/usr/bin/env python
# coding: utf-8

# # Defining Functions That Return sin(x) and cos(x) Coding Journal Prompt 6

# The first thing we want to do is create functions that will return sin(x) and cos(x)

# In[4]:


import numpy as np
import math

def computeSin():
    sinx = np.linspace(0, 2*np.pi, 1000)

    x = np.array(sinx)
    
    for i, val in enumerate(x, start=1):
        print(f"Sin of x:  = {val}")
        
def computeCos():
    
    cosx = np.linspace(0, 2*np.pi, 1000)

    x = np.array(cosx)
    
    cosValues = np.cos(x)
    
    for i, val in enumerate(x, start=1):
        print(f"Cosine of x: {val}")
        
def computeFirstTen():
        
# computeSin()
computeCos()


# In[ ]:




