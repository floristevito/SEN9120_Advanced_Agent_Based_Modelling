import agentpy as ap

"""
All model compontents
"""

class EmtAgent(ap.Agent):
    
    """Base class for all agents in this emt vehicle model"""

    def setup(self):
        pass

class Vehicle(EmtAgent):
    
    def setup(self):
        self.energy = 5
        self.status = None
        self.charger = None
        self.charge_time = None
        
    def drive(self):
        self.status = 'driving'
        self.energy -= 1
    
    def init_charge(self):
        # check if charger left with free capacity 
        available_chargers = self.model.chargers.select(self.model.chargers.current_capacity > 0)
        if available_chargers:
            self.charger = available_chargers.random()
            self.charger.add_car()
            self.status = 'charging'
            self.charge_time = 3
        else:
            self.status = 'waiting for charger'

    def end_charge(self):
        self.charger.remove_car()
        self.status = None
    
    def charge(self):
        self.energy += 1
    
    def step(self):
        if self.status != 'charging' and self.energy > 0:
            self.drive()
        else:
            self.init_charge()
            if self.status == 'charging' and self.charge_time > 0:
                self.charge()
            elif self.charge_time == 0:
                self.end_charge()
        print('Vehicle {} is {} and has {} energy left'.format(self.id, self.status, self.energy))
    
class Charger(EmtAgent):
    
    def setup(self):
        self.total_capacity = 10
        self.current_capacity = 0

    def add_car(self):
        if self.current_capacity < self.total_capacity:
            self.current_capacity += 1
        else:
            print('sorry, charger {} full'.format(self.id))
            
    def remove_car(self):
        self.current_Capacity -= 1
