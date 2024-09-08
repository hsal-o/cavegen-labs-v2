from tkinter import messagebox

from exceptions.empty_field_error import EmptyFieldError


class LabelFrameController:
    def set_settings(self, settings):
        self.view.set_settings(settings)

    def get_settings(self):
        if self.view.has_empty_fields():
            raise EmptyFieldError("A field was left blank")

        return self.view.get_settings()
            