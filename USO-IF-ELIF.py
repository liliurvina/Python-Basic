# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 08:21:50 2021

@author: FAMILIA URVINA
"""

acl=int(input("Ingrese el numero de ACL:"))
if acl>=1 and acl <=99:
    print("es una ACL estandar")
elif acl>=100 and acl <=199:
    print ("es una ACL extendida"101)
else:
    print("El # ingresado no es de una ACL")