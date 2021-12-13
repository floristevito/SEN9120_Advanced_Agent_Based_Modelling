import numpy as np
import random
import agentpy as ap
import logging
import math

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
        self.offset_dep = int(random.uniform(-self.model.p.offset_dep,self.model.p.offset_dep))
        self.offset_dwell = int(random.uniform(-self.model.p.offset_dwell, self.model.p.offset_dwell))
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
        self.smart = random.random() < self.model.p.p_smart
        self.cheapest_timesteps = []


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
            total_time_window = self.model.ma_price_history[starting_time%96:ending_time%96] #e.g. charging from 1AM to 3PM is from 1:00 - 3:00
        else:
            total_time_window = self.model.ma_price_history[starting_time%96:] + self.model.ma_price_history[:ending_time%96]
        timesteps_needed = math.ceil(charge_needed/self.charging_speed)
        if timesteps_needed > (abs(ending_time-starting_time)):
            # charge all the available times
            self.cheapest_timesteps = [i for i in range(starting_time,ending_time)]
        else:
            # give all indexes + starting_time that are cheapest
            timewindow = np.array(total_time_window.copy())
            idx = np.argpartition(timewindow, timesteps_needed)
            cheapest_timesteps = idx[:timesteps_needed].tolist()
            self.cheapest_timesteps = [i + starting_time for i in cheapest_timesteps]

    def departure_work(self):
        self.current_location = 'onroad' # go onroad
        self.moving = True 
        self.arrival_time_work = self.model.t + self.travel_time # ETA
        self.departure_time += 96  # update departure time

    def departure_home(self):
        self.current_location = 'onroad'
        self.moving = True
        self.arrival_time_home = self.model.t + self.travel_time 

    def arrive_work(self):
        self.current_location = 'work'
        self.moving = False
        self.return_time = self.model.t + self.dwell_time + self.offset_dwell
        if self.smart:
            self.choose_cheapest_timesteps(self.model.t, self.return_time, (max(0, self.energy_required - self.current_battery_volume)))

    def arrive_home(self):
        self.current_location = 'home'
        self.moving = False
        if self.smart:
            self.choose_cheapest_timesteps(self.model.t, self.departure_time + self.offset_dep, (100 - self.current_battery_volume))
    
    def charge(self):
        if self.current_battery_volume < self.battery_volume:
                increase = self.charging_speed * 0.25  # potential battery increase in 15min
                # check if potential increase does not exceed battery volume
                if self.current_battery_volume + increase < self.battery_volume:
                    self.current_battery_volume += increase  # charge
                else:
                    self.current_battery_volume = self.battery_volume  # set to max

    def step(self):
        # move, determine location and destination
        if (self.model.t % (self.departure_time + self.offset_dep) == 0) and (self.current_location == 'home'):
            if self.current_battery_volume >= self.energy_required: 
                self.departure_work()
            else:
                logging.warning('charge too low to go in morning, should not happen')
            
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
            self.offset_dep = int(random.uniform(-self.model.p.offset_dep,self.model.p.offset_dep)) # Offset for the next day
            self.offset_dwell = int(random.uniform(-self.model.p.offset_dwell, self.model.p.offset_dwell)) # Offset for the next day
            logging.debug('{} a new departure offset has been caculated {}'.format(self.model.t, self.offset_dep))
        
        # energy usage when on road
        if self.current_location == 'onroad':
            logging.debug('DISCHARGE')
            self.current_battery_volume -= self.energy_rate * \
                (self.model.p.average_driving_speed *
                 0.25)  # energy consumption per 15min
        # charging
        else:
            if self.smart:
                if any(i % self.model.t == 0 for i in self.cheapest_timesteps):
                    self.charge() # only charge on smart times
                    logging.debug('smart charging')
            else:
                self.charge() # just go ahead and charge
                logging.debug('not smart charging')
                
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
