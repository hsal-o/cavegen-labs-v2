import tkinter as tk

class LabelEntry(tk.Frame):
    def __init__(self, parent, label_text="", entry_value=""):
        super().__init__(parent)
        
        self.label = tk.Label(self, text=label_text)
        self.entry = tk.Entry(self)
        
        self.label.pack(side="left", fill="both", expand=True)
        self.entry.pack(side="right", fill="both", expand=True)
        
        self.entry.insert(0, entry_value)
        
    def get(self):
        return self.entry.get()
    
    def set(self, value):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value)