from tkinter import messagebox


class LabelFrameController:
    def set_settings(self, settings):
        self.view.set_settings(settings)

    def get_settings(self):
        if self.view.has_empty_fields():
            messagebox.showerror("Error", "A field was left blank")

        return self.view.get_settings()
            