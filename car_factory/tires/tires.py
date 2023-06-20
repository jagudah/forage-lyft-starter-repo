from abc import ABC, abstractmethod

class Tires(ABC):
    @abstractmethod
    def needs_service(self):
        'Must be overriden by Tires objects'
        pass