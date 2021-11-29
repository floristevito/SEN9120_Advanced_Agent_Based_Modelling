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
        self.home_location = None           #location of the home of the agent                      [unit: - (municipality agent)]
        self.work_location = None           #location of the work of the agent                      [unit: - (municipality agent)]
        self.battery_level = None           #current amount of energy in the battery                [unit: kWh]
        self.total_battery_cap = None       #total energy storage size of the battery               [unit: kWh]      
        self.fuel_use_rate = None           #the rate it consumes energy to travel                  [unit: kWh/km] 
        self.is_moving = False              #indicator whether the agent is moving                  [unit: boolean, True/False]
        self.is_charging = False            #indicator whether the agent is charging                [unit: boolean, True/False]
        self.VTG_percentage = None                   #indicates the percentage of battery allowed for VTGS   [unit: percentage 0-100%]
        self.current_buffer_cap = None      #current battery capacity available for VTGS            [unit: kWh]
        self.current_buffer_wattage = None  #equals the wattage of the attached charger             [unit: KW]
        self.current_power_demand = None    #the amount of wattage it needs to charge               [unit: KW]
        self.destination = None             #the location of where the agent is headed              [unit: - (municipality agent)]
        
        ######## old parameters
        self.energy = 5
        self.status = None
        self.charger = None
        self.charge_time = None
        
    def drive(self):
        self.status = 'driving'
        self.energy -= 1
    
    def step(self):
        if self.status != 'charging' and self.energy > 0:
            self.drive()
    
class Municipality(EmtAgent):
    def setup(self):
        self.name = None
        self.OD = None
        self.id = None
        self.location = None
        self.total_charging_spots = None
        self.available_charging_spots = None
        self.mun_tot_EV_buffer_cap = None
        self.mun_tot_charging_power_demand = None

