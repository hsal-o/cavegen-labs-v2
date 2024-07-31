class BaseController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def set_parameters(self, parameters):
        self.model.set_parameters(parameters)
        output = self.model.generate()
        # Handle output and putting it into output frame