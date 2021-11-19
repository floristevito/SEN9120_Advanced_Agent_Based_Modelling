import agentpy as ap
import pandas as pd
import networkx as nx
from components import Vehicles

"""
Main model block
"""

class EmtAgentsModel(ap.Model):
    """Main model that simulates electric vehicles"""
    
    def setup(self):
        self.agents = ap.AgentList(self, self.p.agents, Vehicles)
    
    def step(self):
        self.agents.agent_method()

    def update(self):
        self.agents.record('my_attribute')

    def end(self):
        self.report('my_measure', 1)