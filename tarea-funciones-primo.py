# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 10:24:38 2021

@author: FAMILIA URVINA
"""

def l100kmtompg(liters):
#
# put your code here
#
# 100Km=62,13711922373 
    milla=1609.344
    cienkm=62.13711922373 
    l=3.785411784 
    print (type(liters))
    x=cienkm*l/float(liters)
    return float(x)
def mpgtol100km(miles):
#
# put your code here
#
 milla=1609.344
    km100=miles*1609.344/1000/100
    liters=3.785411784
    return liters/km100

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))