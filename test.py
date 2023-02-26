import tkinter as tk

class EntryClear(tk.Entry):
    def __init__(self, master=None, other=None, **kwargs):
        super().__init__(master, **kwargs)
        self.other = other

        # Bind the event of user typing in the entry
        self.bind('<KeyRelease>', self.on_key_release)

    def on_key_release(self, event):
        # Get the current value in this entry
        current_value = self.get()

        # Set the value in the other entry to empty if it's not already empty
        if current_value and self.other.get() != '':
            self.other.delete(0, tk.END)

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        # Create two entry widgets side by side
        self.left_entry = EntryClear(self, width=10)
        self.right_entry = EntryClear(self, width=10, other=self.left_entry)

        self.left_entry.pack(side='left')
        self.right_entry.pack(side='right')


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.mainloop()
