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
        self.OD = generate_OD(self.p.g)
        self.municipalities_data = pd.read_csv('../data/gemeenten.csv').set_index('GM_CODE')
        self.vehicles = ap.AgentList(self, self.p.vehicles, Vehicle)
        self.municipalities = ap.AgentList(self, len(self.OD), Municipality)
        counter = 0 
        for key, value in self.OD.items():
            self.municipalities.id[counter] = key
            self.municipalities.name[counter] = self.municipalities_data.loc[key, 'GM_NAAM']
            self.municipalities.OD[counter] = value
            self.municipalities.inhabitants[counter] = self.municipalities_data.loc[key, 'AANT_INW']
            counter += 1
        
    
    def step(self):
        self.vehicles.step()
    
    def update(self):
        """ Record a dynamic variable. """
        self.vehicles.record('energy')
