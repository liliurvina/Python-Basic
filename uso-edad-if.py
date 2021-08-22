# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 11:37:58 2021

@author: FAMILIA URVINA
"""

space=" "
print("Nombre")
nombre=input()
print("Dirección")
direccion=input()
edad=int(input("Edad:"))
print ("Bienvenido"+space+nombre)
if edad >= 1 and edad <= 10:
    print(nombre+space+"Eres un niño")
elif edad >= 11 and edad <= 17:
    print(nombre+space+"Eres un adolescente")
else:
    print(nombre+space+"Eres un adulto")