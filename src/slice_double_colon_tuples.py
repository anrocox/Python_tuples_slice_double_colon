#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 7, 2014

@author: anroco

How to get a slice tuple using step parameter in python?

¿Como obtener secciones de una tupla usando el parametro step en python?
'''

#create a tuple
tupla = tuple('hello world')
print (tupla)

#tuple[start:stop:step]
#step specify an increment between the elements to cut of the tuple.
_slice = tupla[2:9:2]
print(_slice)

#returns a tuple with a jump every 3 items.
_slice = tupla[::3]
print(_slice)

#when step is negative the jump is made back
_slice = tupla[10:2:-3]
print(_slice)
