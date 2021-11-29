import agentpy as ap
import pandas as pd
from model import EmtAgentsModel

parameters = {
    'vehicles': 10,
    'steps': 10,
    'g': 0.000076,
}

model = EmtAgentsModel(parameters)
results = model.run()