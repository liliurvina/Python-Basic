# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 08:33:05 2021

@author: FAMILIA URVINA
"""

def multiply(x,y):
    print(x*y)
    
multiply(5,8)

def multiply(x,y):
    print(x*y)
    return (x*y)
    print(x*y)
    return (x*y)
w=float(multiply(5.1,8.45))
resultado=w+10
print("{:.2f}".format(resultado))

def listafun (lista):
    for i in lista:
        print("Hola",i)
    print("\n"*2)
    
listafun(["Juan"])
listafun(["Juan","Carlos"])
listafun(["Juan","Carlos","Ana"])
listafun(["Juan","Carlos","Ana","Dillan"])

def crealista(n):
    lista=[]
    for i in range(n):
        lista.append(i)
    return lista
resultado=crealista(5)
print(resultado)

def suma(*args):
    print("\nTip de datos del argumento: ", type(args))
    sum=0
    for n in args:
        sum +=n
    print ("Suma:", sum)
suma(3)
suma(1)
suma(3,5)
suma(4,5,7,7)


seq=["soup", "dog", "salda","cat","great"]
result=(list(filter (lambda word: word [1]=="a",seq)))
