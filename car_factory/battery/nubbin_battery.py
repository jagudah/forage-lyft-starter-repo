from battery import Battery
from datetime import datetime
from dateutil import relativedelta

class NubbinBattery(Battery):
    def __init__(self, last_service_date: datetime, current_date: datetime):
        self.last_service_date = last_service_date
        self.current_date = current_date
    
    def needs_service(self):
        dateInterval = relativedelta.relativedelta(self.current_date, self.last_service_date)
        if dateInterval.years >= 4:
            return True
        else:
            return False