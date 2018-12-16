# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 20:34:32 2018

@author: mikke
"""
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox as tb
from matplotlib.widgets import Button as bt
#from matplotlib.widgets import CheckButtons as c_bt
import numpy as np
from method_Line import Method_Line

class Main:
    
    def __init__(self):
        self.x = np.arange(0,201)
        self.y = self.x**2
                
        self.dp = 0.5*10**0
        self.start_x = 0
        self.state = 0
        
        self.initial_text = "x**2"
        self.liste = []
        
        self.ml = Method_Line()
        
        self.fig = plt.figure()
        
        self.ax1 = plt.subplot2grid((32,3), (0,0), rowspan = 17, colspan = 4)
        self.ax2 = plt.subplot2grid((32,5), (22,1), rowspan = 2, colspan = 2)
        self.ax3 = plt.subplot2grid((32,5), (24,1), rowspan = 2, colspan = 1)
        self.ax4 = plt.subplot2grid((32,5), (26,1), rowspan = 2, colspan = 1)
        self.ax5 = plt.subplot2grid((32,5), (22,4), rowspan = 2, colspan = 1)
        self.ax6 = plt.subplot2grid((32,5), (24,4), rowspan = 2, colspan = 1)
        self.ax7 = plt.subplot2grid((32,5), (28,4), rowspan = 2, colspan = 1)
        self.ax8 = plt.subplot2grid((32,5), (30,4), rowspan = 2, colspan = 1)

        
        self.start_plot()
        
        self.func_box = tb(self.ax2, 'Funktionen: f(x)=', initial = self.initial_text)
        self.func_box.on_submit(self.submit_func)
        
        self.deci_precision = tb(self.ax3, 'Decimal præcision:', initial = "0")
        self.deci_precision.on_submit(self.submit_precision)
        
        self.guess_box = tb(self.ax4, 'Start gæt:', initial = str(self.start_x))
        self.guess_box.on_submit(self.start_guess)
        
        self.nxt_guess = bt(self.ax5, 'Næste x')
        self.nxt_guess.on_clicked(self.find_next)
        self.ax5.set_title("Med numerisk differentiation", fontsize = 8)
        
        self.finish = bt(self.ax6, 'Færdigør')
        self.finish.on_clicked(self.find_all)
        
        self.nxt_guess2 = bt(self.ax7, 'Næste x')
        self.nxt_guess2.on_clicked(self.find_exact_next)
        self.ax7.set_title("Med eksakt differentiation", fontsize = 8)
        
        self.finish2 = bt(self.ax8, 'Færdigør')
        self.finish2.on_clicked(self.exact_find_all)
        

    
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
            self.liste = []
    
    def find_next(self,event):
        if self.liste != []:
            self.liste = self.ml.diff_func(self.liste[-1][0], self.initial_text, self.dp)
            self.ax1.plot([self.liste[-2][0],self.liste[-2][0]],[0,self.liste[-1][3]], linestyle = 'dashed')
            print("x-værdi: "+ str(self.liste[-2][0]))
            print("f("+str(self.liste[-2][0])+") = "+str(self.liste[-1][3]))
        elif self.start_x != '':
            self.start_plot()
            self.liste = self.ml.diff_func(self.start_x,self.initial_text,self.dp)
            self.ax1.plot([self.start_x,self.start_x],[0,self.liste[-1][3]], linestyle = 'dashed')
            print("x-værdi: "+ str(self.start_x))
            print("f("+str(self.start_x)+") = "+str(self.liste[-1][3]))
            
        #print(len(self.liste))
        #print(self.liste[0])
        #self.start_plot()
        self.ax1.plot([self.liste[-1][0],self.liste[-1][2]],[0,self.liste[-1][1]])
        plt.draw()
        
    
    def find_all(self,event):
        gentagelser = 0
        if self.liste == []:
            gentagelser += 1
            self.start_plot()
            self.liste = self.ml.diff_func(self.start_x,self.initial_text,self.dp)
            
            self.ax1.plot([self.liste[-1][0],self.liste[-1][2]],[0,self.liste[-1][1]])
            self.ax1.plot([self.start_x,self.start_x],[0,self.liste[-1][3]], linestyle = 'dashed')
            
        while abs(self.liste[-1][3]) > self.dp:
            gentagelser += 1
            self.liste = self.ml.diff_func(self.liste[-1][0], self.initial_text, self.dp)

            self.ax1.plot([self.liste[-1][0],self.liste[-1][2]],[0,self.liste[-1][1]])
            self.ax1.plot([self.liste[-2][0],self.liste[-2][0]],[0,self.liste[-1][3]], linestyle = 'dashed')
            plt.draw()
        print("antal gentagelser: " + str(gentagelser))
        print("x-værdi: "+ str(self.liste[-2][0]))
        print("f("+str(self.liste[-2][0])+") = "+str(self.liste[-1][3]))
    
    def find_exact_next(self,event):
        if self.liste != []:
            self.liste = self.ml.exact_diff(self.liste[-1][0],self.initial_text)
            self.ax1.plot([self.liste[-2][0],self.liste[-2][0]],[0,self.liste[-1][3]], linestyle = 'dashed')
            print("x-værdi: "+ str(self.liste[-2][0]))
            print("f("+str(self.liste[-2][0])+") = "+str(self.liste[-1][3]))
        elif self.start_x != '':
            self.start_plot()
            self.liste = self.ml.exact_diff(self.start_x,self.initial_text)
            self.ax1.plot([self.start_x,self.start_x],[0,self.liste[-1][3]], linestyle = 'dashed')
            print("x-værdi: "+ str(self.start_x))
            print("f("+str(self.start_x)+") = "+str(self.liste[-1][3]))
        self.ax1.plot([self.liste[-1][0],self.liste[-1][2]],[0,self.liste[-1][1]])
        plt.draw()
        
    
    def exact_find_all(self,event):
        gentagelser = 0
        if self.liste == []:
            gentagelser += 1
            self.start_plot()
            self.liste = self.ml.exact_diff(self.start_x,self.initial_text)
            
            self.ax1.plot([self.liste[-1][0],self.liste[-1][2]],[0,self.liste[-1][1]])
            self.ax1.plot([self.start_x,self.start_x],[0,self.liste[-1][3]], linestyle = 'dashed')
            
        while abs(self.liste[-1][3]) > self.dp:
            gentagelser += 1
            self.liste = self.ml.exact_diff(self.liste[-1][0], self.initial_text)

            self.ax1.plot([self.liste[-1][0],self.liste[-1][2]],[0,self.liste[-1][1]])
            self.ax1.plot([self.liste[-2][0],self.liste[-2][0]],[0,self.liste[-1][3]], linestyle = 'dashed')
            plt.draw()
        print("antal gentagelser: " + str(gentagelser))
        print("x-værdi: "+ str(self.liste[-2][0]))
        print("f("+str(self.liste[-2][0])+") = "+str(self.liste[-1][3]))
        
        
main = Main()
plt.show()