from tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tires_wear: list):
        self.tires_wear = tires_wear
    
    def needs_service(self):
        if sum(self.tires_wear) >= 3:
            return True
        else:
            return False