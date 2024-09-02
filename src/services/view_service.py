# class ViewService:
#     def __init__(self, view):
#         self.view = view

#     def get_settings(self):
#         settings = {}
#         for key, widget in self.view.widgets.items():
#             widget_type = self.view.widget_configs[key].get_type()
#             widget_value = widget.get()

#             if isinstance(widget_value, tuple):
#                 settings[key] = tuple(widget_type(value) for value in widget_value)
#             else:
#                 settings[key] = widget_type(widget_value)
#         return settings

#     def set_settings(self, settings):
#         for key, value in settings.items():
#             widget = self.view.widgets[key]
#             widget_type = self.view.widget_configs[key].get_type()

#             if isinstance(value, tuple):
#                 converted_value = tuple(widget_type(v) for v in value)
#                 widget.set(converted_value)
#             else:
#                 widget.set(widget_type(value))