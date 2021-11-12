import tkinter as tk

switch = False

def add(exp: tk.StringVar, s: str):
    if s == "( )":
        global switch
        if switch:
            s = ")"
            switch = False
        else:
            s = "("
            switch = True
    elif s == "^":
        s = "**"
            
    expression = exp.get() + s
    exp.set(expression)
    
def clear(exp: tk.StringVar):
    exp.set("")
    
def delete(exp: tk.StringVar):
    if len(exp.get()) > 0:
        expression = exp.get()[:-1]
        exp.set(expression)
    
def equal(exp: tk.StringVar):
    try:
        result = eval(exp.get())
    except SyntaxError: 
        exp.set("SYNTAX ERROR !")
    except ZeroDivisionError:
        exp.set("ZERO DIVISION ERROR !")
    else:
        exp.set(f"{result}")