# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 10:18:10 2021

@author: FAMILIA URVINA
"""

x=input("Ingrese un número de veces a contar: ")
x=int(x)
y=1
while y <= x:
    print (y)
    y+=1
 
x=input("Ingrese un número de veces a contar: ")
x=int(x)
y=1 
while True:
    print(y)
    y+=1
    if y>x:
        break
"""
descubri error
"""
while True:
    x=input("Ingrese un número para contar hasta: ")
    if x=="q" or x=="quit":
       break
    x=int(x)       
    y=1
    while True:
           print(y)
           y=y+1
           if y > x: 
              break