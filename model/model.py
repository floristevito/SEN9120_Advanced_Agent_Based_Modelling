import agentpy as ap
import pandas as pd
import networkx as nx
from components import *

"""
Main model block
"""

class EmtAgentsModel(ap.Model):
    """Main model that simulates electric vehicles"""
    
    def setup(self):
        self.vehicles = ap.AgentList(self, self.p.vehicles, Vehicle)
        self.chargers = ap.AgentList(self, self.p.chargers, Charger)
    
    def step(self):
        self.vehicles.step()
