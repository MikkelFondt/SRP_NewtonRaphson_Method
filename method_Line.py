# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 16:29:06 2018

@author: Mikkel Meisner Fondt
"""
import sympy as sp
from scipy.misc import derivative

global x
class Method_Line:
    
    def __init__(self):
        global x
        x = sp.Symbol("x")
        self.l = []
    
    def diff_func(self,x1,y,dp):
        f = sp.Lambda(x,y)
        
        f1 = derivative(f,x1,dx = dp)

        b = f(x1)-f1*x1
        
        nxt_x = x1-(f(x1)/f1)
        
        if nxt_x < x1:
            diff = (x1+abs(nxt_x-x1))
            if diff > 20:
                diff = 20
        else:
            diff = (x1-abs(nxt_x-x1))
            if diff < 0:
                diff = 0
        
        tangent = f1*diff+b
        func = f(x1)
        
        self.l.append([nxt_x,tangent,diff,func])
        #print(self.l[0])
        return self.l
    
    def exact_diff(self,x1,y):
        f = sp.Lambda(x,y)
        f1 = sp.Lambda(x,sp.diff(f(x),x))
        
        nxt_x = x1-(f(x1)/f1(x1))
        
        if nxt_x < x1:
            diff = (x1+abs(nxt_x-x1))
            if diff > 20:
                diff = 20
        else:
            diff = (x1-abs(nxt_x-x1))
            if diff < 0:
                diff = 0
        
        tangent = f1(x1)*diff+f(x1)-(f1(x1)*x1)
        
        self.l.append([nxt_x,tangent,diff,f(x1)])
        return self.l

    def clear_list(self):
        self.l = []
