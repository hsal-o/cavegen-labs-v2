
from controllers.label_frame_controller import LabelFrameController

class GridConfigurationService(LabelFrameController):
    def __init__(self, view):
        self.view = view
        view.set_controller(self)

    def get_seed_entry(self):
        return self.view.get_seed_entry()
    
    def set_seed_entry(self, seed):
        self.view.set_seed_entry(seed)
    