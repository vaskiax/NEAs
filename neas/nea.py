class Nea():
    def __init__(self):
        self.nea_id = None
        self.name = None    
        self.diameter = None
        self.hazardous = None    
    
    
    
    def __str__(self):
        return f"NEA {self.nea_id}:\
              {self.name} ({self.diameter}m) -\
                  {'Hazardous' if self.hazardous else 'Not Hazardous'}"