import tkinter as tk
from tkinter import ttk

from widgets.util.custom_base_widget import CustomBaseWidget
from widgets.label_double_entry import LabelDoubleEntry
from util.constants import WIDGET_WIDTH
from util.grid_position import GridPosition 

class PositionSelector(tk.Frame, CustomBaseWidget):
    def __init__(self, parent, label="", default=GridPosition.CENTER):
        super().__init__(parent)

        # Configure grid columns to have equal weight
        self.grid_columnconfigure(0, weight=1, uniform="1")
        self.grid_columnconfigure(1, weight=1, uniform="1")

        self.grid_rowconfigure(0)
        self.grid_rowconfigure(1)

        ### Create and place the label
        label = tk.Label(self, text=label, wraplength=WIDGET_WIDTH*7, anchor="w", justify="left")
        label.grid(row=0, column=0, sticky="w")

        ### Create and place the combobox
        combobox_container = tk.Frame(self, width=WIDGET_WIDTH)
        combobox_container.grid(row=0, column=1, sticky="ew")

        combobox_options = [e.name.replace("_", " ").title() for e in GridPosition]
        self.combobox = ttk.Combobox(combobox_container, width=0, values=combobox_options, state="readonly")
        self.combobox.pack(fill=tk.BOTH, expand=True)
        self.combobox.bind("<<ComboboxSelected>>", self.on_select)
        self.combobox.current(default.value) # Set default selection

        ### Create and place the optional customdouble entry
        self.entry_container = tk.Frame(self)
        self.entry_container.grid_columnconfigure(0, weight=1)
        self.entry_container.grid_columnconfigure(1, weight=1)

        # Create and place the left entry
        self.entry_left = ttk.Entry(self.entry_container, width=0) 
        self.entry_left.grid(row=0, column=0, sticky="ew")

        # Create and place the right entry
        self.entry_right = ttk.Entry(self.entry_container, width=0)
        self.entry_right.grid(row=0, column=1, sticky="ew")

        if default == GridPosition.CUSTOM:
            self.show_custom_entry()
        else:
            self.hide_custom_entry()

    def show_custom_entry(self):
        self.entry_container.grid(row=1, column=1, sticky="ew")

    def hide_custom_entry(self):
        self.entry_container.grid_forget()

    def on_select(self, event=None):
        selection = self.combobox.current()
        position = GridPosition(selection)

        if position == GridPosition.CUSTOM:
            self.show_custom_entry()
        else:
            self.hide_custom_entry()

    def get(self):
        selection = self.combobox.current()
        position = GridPosition(selection)

        if(position == GridPosition.CUSTOM):
            return GridPosition.determine(position, x=int(self.entry_left.get()), y=int(self.entry_right.get()))
        else:
            return GridPosition.determine(position)

    def set(self, value):
        self.combobox.set(value.value)

    # Implementing parent methods
    def is_empty(self):
        selection = self.combobox.current()
        position = GridPosition(selection)
        return (position == GridPosition.CUSTOM and not (self.entry_left.get().strip() and self.entry_right.get().strip()))
