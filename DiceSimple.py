# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from tkinter import *
import random

#creating tinker instance
root=Tk()
#setting window size
root.geometry("400x400")
root.configure(background='white')


#label for dice in root
l1=Label(root,font=("Helvetica",260),background='white')

def roll():
    
    #dice holing unicode of dice faces
    dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    #dice label config
    l1.config(text=f'{random.choice(dice)}{random.choice(dice)}')
    l1.pack()
    
b1=Button(root,text="Roll the Dice!",foreground='black',background='white', command=roll)
b1.place(x=300,y=0)
b1.pack()

root.mainloop()