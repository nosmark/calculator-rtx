import os
import math
from tkinter import *
from tkinter import ttk
from src import calc_logic
from src import calc_history


class Calc_UI:
    def __init__(self, root):
        self.root = root
        self.root.title("RTX Calculator")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)  

        self.display_var = StringVar(value=0)

        frame = ttk.Frame(root)
        frame.grid(column=0, row=0, sticky=NSEW)
        frame.columnconfigure((0,1,2,3), weight=1)
        frame.rowconfigure((0,1,2,3,4), weight=1)
        entry = ttk.Entry(frame, textvariable=self.display_var, font=("Arial", 20), justify=RIGHT)
        entry.grid(row=0, column=0, columnspan=4, sticky=NSEW, padx=5, pady=5)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row_val = 1
        col_val = 0
        for btn_txt in buttons:
            action = lambda x=btn_txt: self.on_click(x)
            ttk.Button(frame, text=btn_txt, command=action).grid(row=row_val, column=col_val, sticky=NSEW, padx=2, pady=2)

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_click(self, char):
        if char == "C":
            self.display_var.set("0")
        elif char == "=":
            nums = self.display_var.get()
            for op in ["+", "-", "*", "/"]:
                if op in nums:
                    parts = nums.split(op)
                    first_num = float(parts[0])
                    second_num = float(parts[1])
                    break
            self.display_var.set(calc_logic.calculator(op, first_num, second_num))
        else:
            current = self.display_var.get()
            if current == "0":
                self.display_var.set(char)
            else:
                self.display_var.set(current + char)




root = Tk()
calculator = Calc_UI(root)

root.mainloop()        

