import agentpy as ap

"""
All model compontents
"""
class EV(ap.Agent):
    
    def setup(self):
        self.name = name
        self.charge_init = charge_init
        self.charging_speed = 10
        self.price_memory = [[] for i in range(24)]
        self.average_price_memory = []
        
    def fill_memory(self, current_hour, electricity_price):
        '''
        Fills the memory of agents with the previous prices
        
        SHOULD BE DONE ON SUPERCLASS LEVEL TO SAVE DATA AND COMPUTATIONS
        
        '''
        
        self.price_memory[(current_hour %24) - 1].append(electricity_price)
        
    def average_memory(self):
        '''
        From self.price_memory creates avarage prices for a 24h cycle
        
        Could be expanded to a 7*24h cycle if wanted
        
        '''
        self.average_price_memory = [round(np.mean(self.price_memory[i]),2) for i in range(len(self.price_memory))]
    
    def choose_cheapest_hours(self,starting_time,ending_time,charge_needed):
        '''This function will tell you the most economic (cheap) way of getting to a full charge within the time window, if possible
           The start and end time are ticks of 1 hour atm
           Charge needed still abstract/dimensionless, the amount of energy the car needs e.g. full or like 75% idc
           
           
           Function use:
           input starting and ending time of charge 
           function outputs cheapest predicted hours (ticks count of hour)
           hours can be set to charging? = true using this
        '''
        if starting_time%24 < ending_time%24:
            total_time_window = self.average_price_memory[starting_time%24:ending_time%24] #e.g. charging from 1AM to 3PM is from 1:00 - 3:00
        else:
            total_time_window = self.average_price_memory.copy()
            del total_time_window[ending_time%24:starting_time%24]
            print('time_window:')
            print(total_time_window)
        hours_needed = math.ceil(charge_needed/self.charging_speed)
        if hours_needed > (abs(ending_time-starting_time)):
            print('total time is insufficient to charge to full. Charging commencing immediately')
            return starting_time

        timewindow_copy = total_time_window.copy()
        timewindow_copy.sort()
        cheapest_values = timewindow_copy[:hours_needed]
        cheapest_starting_hours = [total_time_window.index(i) + starting_time for i in cheapest_values]

        print('the cheapest hour to start are hours {} with a total value of {}'.format(cheapest_starting_hours,cheapest_values))
class Municipality(ap.Agent):
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

