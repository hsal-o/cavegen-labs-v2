class BaseModel:
    def __init__(self):
        self.parameters = {}

    def set_parameters(self, parameters):
        self.parameters = parameters

    def generate(self):
        raise NotImplementedError("Method not implemented")