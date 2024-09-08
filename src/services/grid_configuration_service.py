
from controllers.label_frame_controller import LabelFrameController

class GridConfigurationService(LabelFrameController):
    _instance = None

    def __new__(cls, view=None):
        if cls._instance is None:
            if view is not None:
                cls._instance = super(GridConfigurationService, cls).__new__(cls)
                cls._instance.view = view
                view.set_controller(cls._instance)
            else:
                raise ValueError("View must be provided for the first instantiation")
        return cls._instance

    def __init__(self, view=None):
        if view is not None:
            self.view = view
            view.set_controller(self)

    def get_width_entry(self):
        return self.view.get_width_entry()
    
    def get_height_entry(self):
        return self.view.get_height_entry()

    def get_seed_entry(self):
        return self.view.get_seed_entry()
    
    def set_seed_entry(self, seed):
        self.view.set_seed_entry(seed)
    