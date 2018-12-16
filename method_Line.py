# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 16:29:06 2018

@author: Mikkel Meisner Fondt
"""
import math
import sympy as sp

global x
class Method_Line:
    
    def __init__(self):
        global x
        x = sp.Symbol("x")
        self.l = []
    
    def diff_func(self,x1,y,dp):
        Delta_x = 100
        x2 = x1+Delta_x
        y = eval(y)
        y1 = y.subs(x,x1)
        y2 = y.subs(x,x2)
        a = math.inf
        
        while abs(a - ((y2-y1)/(x2-x1))) > dp:
            a = ((y2-y1)/(x2-x1))
            Delta_x = Delta_x/2
            x2 = x1 + Delta_x
            y2 = y.subs(x,x2)
        a = ((y2-y1)/(x2-x1))
        b = y1-a*x1
        
        nxt_x = x1-(y1/a)
        
        if nxt_x < x1:
            diff = (x1+abs(nxt_x-x1))
            if diff > 200:
                diff = 200
        else:
            diff = (x1-abs(nxt_x-x1))
            if diff < -200:
                diff = -200
        
        tangent = a*diff+b
        func = a*x1+b
        
        self.l.append([nxt_x,tangent,diff,func])
        #print(self.l[0])
        return self.l
    
    def exact_diff(self,x1,y):
        y = eval(y)
        y1 = y.subs(x,x1)
        f = sp.diff(y,x)
        a = f.subs(x,x1)
        
        nxt_x = x1-(y1/a)
        
        if nxt_x < x1:
            diff = (x1+abs(nxt_x-x1))
            if diff > 200:
                diff = 200
        else:
            diff = (x1-abs(nxt_x-x1))
            if diff < -200:
                diff = -200
        
        tangent = a*diff+y1-(a*x1)
                
        self.l.append([nxt_x,tangent,diff,y1])
        return self.l

    def clear_list(self):
        self.l = []
