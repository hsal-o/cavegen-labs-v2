# Original: https://stackoverflow.com/questions/3221956/how-do-i-display-tooltips-in-tkinter
import tkinter as tk

import util.config

class CreateToolTip(object):
    def __init__(self, widget, text='widget info'):
        self.waittime = 500     # milliseconds
        self.wraplength = 180   # pixels
        self.widget = widget
        self.text = text

        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def use_tooltip(self):
        return util.config.USE_TOOLTIP

    def enter(self, event=None):
        if self.use_tooltip():
            self.schedule()

    def leave(self, event=None):
        if self.use_tooltip():
            self.unschedule()
            self.hidetip()

    def schedule(self):
        if self.use_tooltip():
            self.unschedule()
            self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        if self.use_tooltip():
            x = y = 0
            x, y, cx, cy = self.widget.bbox("insert")
            x += self.widget.winfo_rootx() + 25
            y += self.widget.winfo_rooty() + 20
            # creates a toplevel window
            self.tw = tk.Toplevel(self.widget)
            # Leaves only the label and removes the app window
            self.tw.wm_overrideredirect(True)
            self.tw.wm_geometry("+%d+%d" % (x, y))
            label = tk.Label(self.tw, text=self.text, justify='left',
                           background="#ffffff", relief='solid', borderwidth=1,
                           wraplength=self.wraplength)
            label.pack(ipadx=1)

    def hidetip(self):
        if self.use_tooltip():
            tw = self.tw
            self.tw = None
            if tw:
                tw.destroy()
