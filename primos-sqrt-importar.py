# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 11:27:02 2021

@author: FAMILIA URVINA
"""

de matemáticas importar sqrt

def primosHasta(n):
    números = rango(2, n)
    para i en el rango(2, int(2*sqrt(n))):
        números = filtro(lambda x: x==i o x%i, números)
    números devueltos 