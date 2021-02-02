#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 03:21:38 2021

@author: hariniram
"""

from tkinter import*

def btnClick(num):
    global operator
    operator = operator + str(num)
    textInput.set(operator)
    
def btnClearDisplay():
    global operator
    operator = ''
    textInput.set('')
    
def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    textInput.set(sumup)
    operator = ''

cal = Tk()
cal.title("Calculator")
operator = ''
textInput = StringVar()

# displays output of calculation
txtDisplay = Entry(cal, font=('georgia', 20, 'bold'), textvariable = textInput, bd = 30, insertwidth = 4, 
                   bg = "powder blue", justify='right').grid(columnspan=4)

#=====================================================================================================
# button for 0
btn0 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('georgia', 20, 'bold'),
              text="0", bg = "powder blue", command = lambda:btnClick(0)).grid(row=4,column=0)
# button for clear
btnClear = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('georgia', 20, 'bold'),
              text="C", bg = "powder blue", command = lambda:btnClearDisplay()).grid(row=4,column=1)
# button for equals
btnEquals = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('georgia', 20, 'bold'),
              text="=", bg = "powder blue", command = lambda:btnEqualsInput()).grid(row=4,column=2)
# button for division
div = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('georgia', 20, 'bold'),
              text="/", bg = "powder blue", command = lambda:btnClick('/')).grid(row=4,column=3)
#=====================================================================================================
# button for 1
btn1 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('georgia', 20, 'bold'),
              text="1", bg = "powder blue", command = lambda:btnClick(1)).grid(row=3,column=0)
# button for 2
btn2 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('georgia', 20, 'bold'),
              text="2", bg = "powder blue", command = lambda:btnClick(2)).grid(row=3,column=1)
# button for 3
btn3 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('georgia', 20, 'bold'),
              text="3", bg = "powder blue", command = lambda:btnClick(3)).grid(row=3,column=2)
# button for multiplication
mult = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('georgia', 20, 'bold'),
              text="*", bg = "powder blue", command = lambda:btnClick('*')).grid(row=3,column=3)
#=====================================================================================================
# button for 4
btn4 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('georgia', 20, 'bold'),
              text="4", bg = "powder blue", command = lambda:btnClick(4)).grid(row=2,column=0)
# button for 5
btn5 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('georgia', 20, 'bold'),
              text="5", bg = "powder blue", command = lambda:btnClick(5)).grid(row=2,column=1)
# button for 6
btn6 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('georgia', 20, 'bold'),
              text="6", bg = "powder blue", command = lambda:btnClick(6)).grid(row=2,column=2)
# button for subtraction
sub = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('georgia', 20, 'bold'),
              text="-", bg = "powder blue", command = lambda:btnClick('-')).grid(row=2,column=3)
#=====================================================================================================
# button for 7
btn7 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('georgia', 20, 'bold'),
              text="7", bg = "powder blue", command = lambda:btnClick(7)).grid(row=1,column=0)
# button for 8
btn8 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('georgia', 20, 'bold'),
              text="8", bg = "powder blue", command = lambda:btnClick(8)).grid(row=1,column=1)
# button for 9
btn9 = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('georgia', 20, 'bold'),
              text="9", bg = "powder blue", command = lambda:btnClick(9)).grid(row=1,column=2)
# button for addition
add = Button(cal, padx=16, pady=16, bd=8, fg="black", font=('georgia', 20, 'bold'),
              text="+", bg = "powder blue", command = lambda:btnClick('+')).grid(row=1,column=3)



cal.mainloop()