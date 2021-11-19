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
        
    def drive(self):
        self.energy -= 1
    
    def charge(self):
        self.energy += 1
    
    def step(self):
        self.energy -= 1
        print('Vehicle {} has {} energy left'.format(self.id, self.energy))
    
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
