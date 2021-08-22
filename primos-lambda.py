# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 11:29:31 2021

@author: FAMILIA URVINA
"""

nums = range(2, 50) 
for i in range(2, 8): 
    nums = filter(lambda x: x == i or x % i, nums)
  
    
print (type(nums))
