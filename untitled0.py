# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 10:37:03 2018

@author: mikke
"""
import sympy as sp
x = sp.Symbol("x")

f = sp.Lambda(x,x**2)

f1=sp.Lambda(x,sp.differentiate_finite(f(x),x,points=[x-1,x+1]))
print(f1(2))