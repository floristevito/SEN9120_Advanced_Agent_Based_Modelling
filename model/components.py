import numpy as np
import math
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
