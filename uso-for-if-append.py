# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 09:14:02 2021

@author: FAMILIA URVINA
"""
lista1=[]
lista2=[]
lista=["R1","R2","R3","S1","S3"]
for i in lista:
    if "S" in i:
        lista1.append(i)
    else:
        lista2.append(i)
print(lista1)
print(lista2)