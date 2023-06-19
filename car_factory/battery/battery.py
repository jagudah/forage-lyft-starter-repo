from abc import ABC, abstractmethod

class Battery(ABC):
    @abstractmethod
    def needs_service(self):
        '''Must be overriden by Battery objects'''
        pass