import numpy as np
import math
import random
import agentpy as ap

"""
All model compontents
"""


class EV(ap.Agent):
    """[summary]

    Args:
        ap ([type]): [description]
    """

    def setup(self):
        self.charging_speed = self.p.charging_speed
        self.departure_time = random.triangular(self.model.p.l_dep,self.model.p.m_dep, self.model.p.h_dep)
        self.dwell_time = random.triangular(self.model.p.l_dwell, self.model.p.m_dwell, self.model.p.h_dwell)
        self.current_location = 'home'
        self.arrival_time_home = None
        self.arrival_time_work = None
        self.moving = False
        self.return_time = self.departure_time + self.dwell_time
        self.battery_volume = random.triangular(self.model.p.l_vol, self.model.p.m_vol, self.model.p.h_vol)
        self.energy_rate = random.triangular(self.model.p.l_energy, self.model.p.m_energy, self.model.p.h_energy)
        self.current_battery_volume = None

    def choose_cheapest_hours(self, starting_time, ending_time, charge_needed):
        '''This function will tell you the most economic (cheap) way of getting to a full charge within the time window, if possible
           The start and end time are ticks of 1 hour atm
           Charge needed still abstract/dimensionless, the amount of energy the car needs e.g. full or like 75% idc


           Function use:
           input starting and ending time of charge
           function outputs cheapest predicted hours (ticks count of hour)
           hours can be set to charging? = true using this
        '''
        pass
    
    def departure_work(self):
        self.current_location = 'onroad'
        self.moving = True 
        self.arrival_time_work = self.model.t + self.travel_time
    
    def departure_home(self):
        self.current_location = 'onroad'
        self.moving = True 
        self.arrival_time_home = self.model.t + self.travel_time
    
    def arrive_work(self):
        self.current_location = 'work'
        self.moving = False
        self.return_time = self.model.t + self.dwell_time
    
    def arrive_home(self):
        self.current_location = 'home'
        self.moving = False

    def step(self):
        # determine location and destination
        if (self.model.t % self.departure_time == 0) and (self.current_location == 'home'):
            self.departure_work()
        elif (self.model.t == self.arrival_time_work) and (self.current_location == 'onroad'):
            self.arrive_work()
        elif (self.model.t % self.return_time == 0) and (self.current_location == 'work'):
            self.departure_home()
        elif (self.model.t == self.arrival_time_home) and (self.current_location == 'onroad'):
            self.arrive_home()
        # battery volume changes
        if self.current_location == 'onroad':
            self.current_battery_volume -= self.energy_rate * (self.model.p.average_driving_speed * 0.25)
        else:
            self.current_battery_volume += 5

class Municipality(ap.Agent):
    """[summary]

    Args:
        ap ([type]): [description]
    """
    def setup(self):
        self.name = None
        self.OD = None
        self.id = None
        self.inhabitants = None
        self.location = None
        self.total_charging_spots = None
        self.available_charging_spots = None
        self.mun_tot_EV_buffer_cap = None
        self.mun_tot_charging_power_demand = None
