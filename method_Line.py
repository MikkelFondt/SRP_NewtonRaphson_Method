# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 16:29:06 2018

@author: Mikkel Meisner Fondt
"""
import sympy as sp
#from scipy.misc import derivative

global x
class Method_Line:
    
    def __init__(self):
        global x
        x = sp.Symbol("x")
        self.l = []
    
    def diff_func(self,xn,f,dp):
        f = sp.Lambda(x,f)      
        f1 = sp.Lambda(x,sp.differentiate_finite(f(x),x,points = [x-dp,x+dp]))
        
        nxt_x = xn-(f(xn)/f1(xn))
                
        if nxt_x < xn:
            diff = (xn+abs(nxt_x-xn))
            if diff > 20:
                diff = 20
        else:
            diff = (xn-abs(nxt_x-xn))
            if diff < 0:
                diff = 0
        
        b = f(xn)-f1(xn)*xn
        
        tangent = f1(xn)*diff+b
        func = f(xn)
        
        self.l.append([nxt_x,tangent,diff,func])
        #print(self.l[0])
        return self.l
    
    def exact_diff(self,xn,f):
        f = sp.Lambda(x,f)
        f1 = sp.Lambda(x,sp.diff(f(x),x))
        
        nxt_x = xn-(f(xn)/f1(xn))
        
        if nxt_x < xn:
            diff = (xn+abs(nxt_x-xn))
            if diff > 20:
                diff = 20
        else:
            diff = (xn-abs(nxt_x-xn))
            if diff < 0:
                diff = 0
        
        tangent = f1(xn)*diff+f(xn)-(f1(xn)*xn)
        
        self.l.append([nxt_x,tangent,diff,f(xn)])
        return self.l

    def clear_list(self):
        self.l = []
