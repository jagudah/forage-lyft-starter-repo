from tires import Tires

class CarriganTires(Tires):
    def __init__(self, tires_wear: list):
        self.tires_wear = tires_wear
    
    def needs_service(self):
        for wear in self.tires_wear:
            if wear >= 0.9:
                return True
            else:
                return False