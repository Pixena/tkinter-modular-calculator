# Создание UI с помощью tkinter
import tkinter as tk
from tkinter import font
from calc_logic import CalculatorLogic
import config

class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Калькулятор')
        self.root.geometry('360x500')
        self.root.resizable(False, False)
        self.root['bg'] = config.BG_COLOR
        self.logic = CalculatorLogic()
        self._make_display()
        self._make_buttons()

    def _make_display(self):
        self.entry = tk.Entry(
            self.root,
            font=(config.FONT_FAMILY, config.FONT_SIZE_DISPLAY),
            bg=config.BG_COLOR,
            fg='white',
            bd=0,
            justify='right'
        )
        self.entry.insert(0, '0')
        self.entry.grid(row=0, column=0, columnspan=4, pady=(20,10), padx=10, sticky='we')

    def _make_buttons(self):
        buttons = [
            ('C',1,0), ('±',1,1), ('%',1,2), ('/',1,3),
            ('7',2,0), ('8',2,1), ('9',2,2), ('*',2,3),
            ('4',3,0), ('5',3,1), ('6',3,2), ('-',3,3),
            ('1',4,0), ('2',4,1), ('3',4,2), ('+',4,3),
            ('0',5,0,2), ('.',5,2), ('=',5,3)
        ]
        for btn in buttons:
            try:
                text, row, col, span = btn
                colspan = span
            except ValueError:
                text, row, col = btn
                colspan = 1
            color = config.BTN_COLOR if text.isdigit() or text == '.' else config.OP_COLOR
            b = tk.Button(
                self.root,
                text=text,
                font=(config.FONT_FAMILY, config.FONT_SIZE_BTN),
                bd=0,
                bg=color,
                fg='white',
                activebackground=config.BG_COLOR,
                command=lambda t=text: self._click(t)
            )
            b.grid(row=row, column=col, columnspan=colspan, sticky='nsew', padx=5, pady=5)
        for i in range(6): self.root.rowconfigure(i, weight=1)
        for j in range(4): self.root.columnconfigure(j, weight=1)

    def _click(self, char):
        current = self.entry.get()
        result = self.logic.process(char, current)
        self.entry.delete(0, tk.END)
        self.entry.insert(0, result)

    def run(self):
        self.root.mainloop()