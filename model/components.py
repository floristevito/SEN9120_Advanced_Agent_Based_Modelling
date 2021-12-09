import numpy as np
import random
import agentpy as ap
import logging

"""
All model compontents
"""


class EV(ap.Agent):
    """[summary]

    Args:
        ap ([type]): [description]
    """

    def setup(self):
        self.charging_speed = random.uniform(
            self.p.charging_speed_min, self.p.charging_speed_max)
        self.departure_time = int(random.triangular(
            self.model.p.l_dep, self.model.p.m_dep, self.model.p.h_dep))
        self.dwell_time = int(random.triangular(
            self.model.p.l_dwell, self.model.p.m_dwell, self.model.p.h_dwell))
        self.current_location = 'home'
        self.arrival_time_home = None
        self.arrival_time_work = None
        self.moving = False
        self.return_time = self.departure_time + self.dwell_time
        self.battery_volume = random.triangular(
            self.model.p.l_vol, self.model.p.m_vol, self.model.p.h_vol)
        self.energy_rate = random.triangular(
            self.model.p.l_energy, self.model.p.m_energy, self.model.p.h_energy)
        self.current_battery_volume = None
        self.battery_percentage = 100
        self.energy_required = None




    def choose_cheapest_timesteps(self,starting_time,ending_time,charge_needed):
        '''This function will tell you the most economic (cheap) way of getting to a full charge within the time window, if possible
           The start and end time are ticks of 1 hour atm
           Charge needed still abstract/dimensionless, the amount of energy the car needs e.g. full or like 75% idc
           
           
           Function use:
           input starting and ending time of charge 
           function outputs cheapest predicted hours (ticks count of hour)
           hours can be set to charging? = true using this
        '''
        if starting_time%96 < ending_time%96:
            total_time_window = self.model.average_price_memory[starting_time%96:ending_time%96] #e.g. charging from 1AM to 3PM is from 1:00 - 3:00
        else:
            total_time_window = self.model.average_price_memory[starting_time%96:] + self.model.average_price_memory[:ending_time%96]
        timesteps_needed = math.ceil(charge_needed/self.charging_speed)
        if timesteps_needed > (abs(ending_time-starting_time)):
            print('total time is insufficient to charge to full. Charging commencing immediately')
            return starting_time

        timewindow_copy = total_time_window.copy()
        timewindow_copy.sort()
        cheapest_values = timewindow_copy[:timesteps_needed]
        cheapest_starting_timesteps = [total_time_window.index(i) + starting_time for i in cheapest_values]

        print('the cheapest hour to start are hours {} with a total value of {}'.format(cheapest_starting_timesteps,cheapest_values))

    def departure_work(self):
        self.current_location = 'onroad' # go onroad
        self.moving = True 
        self.arrival_time_work = self.model.t + self.travel_time # ETA
        self.departure_time += 96 # update departure time

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
        # move, determine location and destination
        if (self.model.t % self.departure_time == 0) and (self.current_location == 'home'):
            if self.current_battery_volume >= self.energy_required: 
                self.departure_work()
            else:
                logging.debug('charge too low to go in morning, should not happen')
        elif (self.model.t == self.arrival_time_work) and (self.current_location == 'onroad'):
            self.arrive_work()
        elif (self.model.t % self.return_time == 0) and (self.current_location == 'work'):
            # check if enough charge, else wait at work
            if self.current_battery_volume >= self.energy_required: 
                self.departure_home()
            else:
                # if not enough charge, wait untill enough charge is available
                self.return_time += 1
        elif (self.model.t == self.arrival_time_home) and (self.current_location == 'onroad'):
            self.arrive_home()
        
        # battery volume changes
        if self.current_location == 'onroad':
            self.current_battery_volume -= self.energy_rate * \
                (self.model.p.average_driving_speed *
                 0.25)  # energy consumption per 15min
        else:
            if self.current_battery_volume < self.battery_volume:
                increase = self.charging_speed * 0.25  # potential battery increase in 15min
                # check if potential increase does not exceed battery volume
                if self.current_battery_volume + increase < self.battery_volume:
                    self.current_battery_volume += increase  # charge
                    logging.debug('charging')
                else:
                    self.current_battery_volume = self.battery_volume  # set to max
        # determine current battery percentage
        self.battery_percentage = (self.current_battery_volume / self.battery_volume) * 100


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
