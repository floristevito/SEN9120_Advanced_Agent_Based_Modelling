import agentpy as ap
import pandas as pd
import networkx as nx
from components import *
from OD_matrix import (generate_OD)

"""
Main model block
"""

class EmtAgentsModel(ap.Model):
    """Main model that simulates electric vehicles"""
    def setup(self):
        # generate the manicipalities according to data prep file
        self.OD = generate_OD(self.p.g)
        self.municipalities_data = pd.read_csv('../data/gemeenten.csv').set_index('GM_CODE')
        self.municipalities = ap.AgentList(self, len(self.OD), Municipality)
        counter = 0 
        for key, value in self.OD.items():
            self.municipalities.id[counter] = key
            self.municipalities.name[counter] = self.municipalities_data.loc[key, 'GM_NAAM']
            self.municipalities.OD[counter] = value
            self.municipalities.inhabitants[counter] = self.municipalities_data.loc[key, 'AANT_INW']
            self.municipalities.number_EVs[counter] = round(self.p.percentage_ev * self.municipalities.inhabitants[counter])
            counter += 1
        
        # generate EV's 
        self.EVs = ap.AgentList(self, sum(self.municipalities.number_EVs), EV)
        counter = 0
        for mun in self.municipalities:
            for ev in range(mun.number_EVs):
                self.EVs.home_location[counter] = mun.name
                mapped_dest = mun.OD.sample(1, weights='p_flow')
                self.EVs.work_lococation_id[counter] = mapped_dest['destination_id'].iloc[0]
                self.EVs.work_location_name[counter] = self.municipalities_data.loc[self.EVs.work_lococation_id[counter], 'GM_NAAM']
                self.EVs.commute_distance[counter] = mapped_dest['distance'].iloc[0]
                counter += 1
    
    def step(self):
        self.EVs.step()
    
    def update(self):
        """ Record a dynamic variable. """
        self.EVs.record('energy')
