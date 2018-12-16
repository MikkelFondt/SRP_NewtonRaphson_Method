# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 16:29:06 2018

@author: Mikkel Meisner Fondt
"""
import math
import sympy as sp
import copy


class Method_Line:
    
    def __init__(self):
        self.l = []
    
    def diff_func(self,x1,y,dp):
        Delta_x = 100
        x2 = x1+Delta_x
        y1 = eval(y.replace("x","{}".format(x1)))
        y2 = eval(y.replace("x","{}".format(x2)))
        a = math.inf
        
        while a - ((y2-y1)/(x2-x1)) > dp:
            a = ((y2-y1)/(x2-x1))
            Delta_x = Delta_x/2
            x2 = x1 + Delta_x
            y2 = eval(y.replace("x","{}".format(x2)))
        a = ((y2-y1)/(x2-x1))
        b = y1-a*x1
        
        nxt_x = x1-(y1/a)
        
        if nxt_x < x1:
            diff = (x1+abs(nxt_x-x1))
            if diff > 100:
                diff = 100
        else:
            diff = (x1-abs(nxt_x-x1))
            if diff < -100:
                diff = -100
        
        tangent = a*diff+b
        func = a*x1+b
        
        self.l.append([nxt_x,tangent,diff,func])
        #print(self.l[0])
        return self.l

    def clear_list(self):
        self.l = []
