from abc import ABC, abstractmethod

class BaseLevel(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def unload(self):
        pass