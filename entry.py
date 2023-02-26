import tkinter as tk

class Entry(tk.Entry):
    def __init__(self, main=None, other=None, **kwargs):
        super().__init__(main, **kwargs)
        self.other = other

        self.bind()