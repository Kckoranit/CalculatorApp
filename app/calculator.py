import tkinter as tk 
from .functions import *


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator Application")
        
        self.__expression = tk.StringVar()
        
        self.__lbl = tk.Label(self, font=24, textvariable=self.__expression).pack(fill=tk.BOTH, expand=True) 
        
        self.__frm = tk.Frame(self)
        
        for i in range(4):
            self.__frm.columnconfigure(i, weight=1)
            
        # row : 0
        self.__frm.rowconfigure(0, weight=1)
        self.__btn00 = tk.Button(self.__frm, text="( )", command=lambda: add(self.__expression, "( )") ).grid(row=0, column=0, sticky="nsew")
        self.__btn01 = tk.Button(self.__frm, text=".", command=lambda: add(self.__expression, ".") ).grid(row=0, column=1, sticky="nsew")
        self.__btn02 = tk.Button(self.__frm, text="^", command=lambda: add(self.__expression, "^")  ).grid(row=0, column=2, sticky="nsew")
        self.__btn03 = tk.Button(self.__frm, text="/", command=lambda: add(self.__expression, "/")  ).grid(row=0, column=3, sticky="nsew")
        # row : 1
        self.__frm.rowconfigure(1, weight=1)
        self.__btn10 = tk.Button(self.__frm, text="7", command=lambda: add(self.__expression, "7")  ).grid(row=1, column=0, sticky="nsew")
        self.__btn11 = tk.Button(self.__frm, text="8", command=lambda: add(self.__expression, "8")  ).grid(row=1, column=1, sticky="nsew")
        self.__btn12 = tk.Button(self.__frm, text="9", command=lambda: add(self.__expression, "9")  ).grid(row=1, column=2, sticky="nsew")
        self.__btn13 = tk.Button(self.__frm, text="*", command=lambda: add(self.__expression, "*")  ).grid(row=1, column=3, sticky="nsew")
        # row : 2
        self.__frm.rowconfigure(2, weight=1)
        self.__btn20 = tk.Button(self.__frm, text="4", command=lambda: add(self.__expression, "4")  ).grid(row=2, column=0, sticky="nsew")
        self.__btn21 = tk.Button(self.__frm, text="5", command=lambda: add(self.__expression, "5")  ).grid(row=2, column=1, sticky="nsew")
        self.__btn22 = tk.Button(self.__frm, text="6", command=lambda: add(self.__expression, "6")  ).grid(row=2, column=2, sticky="nsew")
        self.__btn23 = tk.Button(self.__frm, text="-", command=lambda: add(self.__expression, "-")  ).grid(row=2, column=3, sticky="nsew")
        # row : 3
        self.__frm.rowconfigure(3, weight=1)
        self.__btn30 = tk.Button(self.__frm, text="1", command=lambda: add(self.__expression, "1")  ).grid(row=3, column=0, sticky="nsew")
        self.__btn31 = tk.Button(self.__frm, text="2", command=lambda: add(self.__expression, "2")  ).grid(row=3, column=1, sticky="nsew")
        self.__btn32 = tk.Button(self.__frm, text="3", command=lambda: add(self.__expression, "3")  ).grid(row=3, column=2, sticky="nsew")
        self.__btn33 = tk.Button(self.__frm, text="+", command=lambda: add(self.__expression, "+") ).grid(row=3, column=3, sticky="nsew")
        
        # row : 4
        self.__frm.rowconfigure(4, weight=1)
        self.__btn40 = tk.Button(self.__frm, text="0", command=lambda: add(self.__expression, "0") ).grid(row=4, column=0, sticky="nsew")
        self.__btn41 = tk.Button(self.__frm, text="ac", command=lambda: clear(self.__expression) ).grid(row=4, column=1, sticky="nsew")
        self.__btn42 = tk.Button(self.__frm, text="del", command=lambda: delete(self.__expression) ).grid(row=4, column=2, sticky="nsew")
        self.__btn43 = tk.Button(self.__frm, text="=", command=lambda:  equal(self.__expression)).grid(row=4, column=3, sticky="nsew")
        
        self.__frm.pack(fill=tk.BOTH, expand=True)