# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 20:34:32 2018

@author: mikke
"""
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox as tb
from matplotlib.widgets import Button as bt
import numpy as np
from method_Line import Method_Line

class Main:
    
    def __init__(self):
        self.x = np.arange(-100,101)
        self.y = self.x**2
                
        self.dp = 0.5*10**0
        self.start_x = 0
        self.initial_text = "x**2"
        self.liste = []
        
        self.ml = Method_Line()
        
        self.fig = plt.figure()
        
        self.ax1 = plt.subplot2grid((28,3), (0,0), rowspan = 18, colspan = 4)
        self.ax2 = plt.subplot2grid((28,5), (22,1), rowspan = 2, colspan = 2)
        self.ax3 = plt.subplot2grid((28,5), (24,1), rowspan = 2, colspan = 1)
        self.ax4 = plt.subplot2grid((28,5), (26,1), rowspan = 2, colspan = 1)
        self.ax5 = plt.subplot2grid((28,5), (22,4), rowspan = 2, colspan = 1)
        self.ax6 = plt.subplot2grid((28,5), (24,4), rowspan = 2, colspan = 1)
        
        self.start_plot()
        
        self.func_box = tb(self.ax2, 'Funktionen: f(x)=', initial = self.initial_text)
        self.func_box.on_submit(self.submit_func)
        
        self.deci_precision = tb(self.ax3, 'Decimal præcision:', initial = "0")
        self.deci_precision.on_submit(self.submit_precision)
        
        self.guess_box = tb(self.ax4, 'Start gæt:', initial = str(self.start_x))
        self.guess_box.on_submit(self.start_guess)
        
        self.nxt_guess = bt(self.ax5, 'Næste gæt')
        self.nxt_guess.on_clicked(self.find_next)
        
        self.finish = bt(self.ax6, 'Færdigør')
        self.finish.on_clicked(self.find_all)
        
    def start_plot(self):
        self.ax1.clear()
        self.ax1.plot(self.x,self.y)
        self.ax1.axhline(y=0, color = (0,0,0), linewidth = 1)
        self.ax1.axvline(x=0, color = (0,0,0), linewidth = 1)
        self.ax1.grid(b=True, which='major', axis='both')
        self.ax1.set_xlabel('x-akse')
        self.ax1.set_ylabel('y-akse')
        self.ax1.set_title('Newton-Raphson Metoden')
        #self.ml.clear_list()
        plt.draw()
    
    def submit_func(self,text):
        self.initial_text = text
        self.y = eval(text.replace("x","self.x"))   
        self.start_plot()
    
    def submit_precision(self,text):
        try:
            self.dp = 0.5*10.0**(0.0-(float(text)))
            print(self.dp)
        except:
            print("Fejl: Der må kun indsættes tal her")
            
    def start_guess(self,text):
        if text != '':
            self.start_x = float(text)
            self.ml.clear_list()
            self.liste = self.ml.diff_func(float(text),self.initial_text,self.dp)
            
            self.start_plot()
            self.ax1.plot([self.liste[0][0],self.liste[0][2]],[0,self.liste[0][1]])
            self.ax1.plot([self.start_x,self.start_x],[0,self.liste[0][3]],linestyle = 'dashed')
            plt.draw()     
            
            """self.liste = ml.get_l(self)
            if ml.l[0][2] < ml.l[0][0]:
                diff = abs(self.liste[0][0]-self.liste[0][2])
                fv = eval(self.liste[0][1].replace("x","{}".format(diff+self.liste[0][0])))
                self.ax1.plot([self.liste[0][2],self.liste[0][0]+diff],[0,fv])"""
    
    def find_next(self,event):
        if self.liste != []:
            self.liste = self.ml.diff_func(self.liste[-1][0], self.initial_text, self.dp)
            
            #print(len(self.liste))
            #print(self.liste[0])
            #self.start_plot()
            self.ax1.plot([self.liste[-1][0],self.liste[-1][2]],[0,self.liste[-1][1]])
            self.ax1.plot([self.liste[-2][0],self.liste[-2][0]],[0,self.liste[-1][3]], linestyle = 'dashed')
            plt.draw()
            print("x-værdi: "+ str(self.liste[-2][0]))
            print("f("+str(self.liste[-2][0])+") = "+str(self.liste[-1][3]))
    
    def find_all(self,event):
        if self.liste != []:
            while abs(self.liste[-1][3]) > self.dp:
                self.liste = self.ml.diff_func(self.liste[-1][0], self.initial_text, self.dp)
                
                #print(len(self.liste))
                #print(self.liste[0])
                #self.start_plot()
                self.ax1.plot([self.liste[-1][0],self.liste[-1][2]],[0,self.liste[-1][1]])
                self.ax1.plot([self.liste[-2][0],self.liste[-2][0]],[0,self.liste[-1][3]], linestyle = 'dashed')
                plt.draw()
            print("x-værdi: "+ str(self.liste[-2][0]))
            print("f("+str(self.liste[-2][0])+") = "+str(self.liste[-1][3]))
                
            
        
main = Main()
plt.show()