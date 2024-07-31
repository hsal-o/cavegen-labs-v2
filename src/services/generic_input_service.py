# Singleton 
class GenericInputService:
    _instance = None

    @staticmethod
    def get_instance():
        if GenericInputService._instance is None:
            GenericInputService()
        return GenericInputService._instance

    def __init__(self):
        if GenericInputService._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            GenericInputService._instance = self
