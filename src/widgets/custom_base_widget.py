from abc import ABC, abstractmethod

class CustomBaseWidget(ABC):
    @abstractmethod
    def is_empty(self):
        pass
