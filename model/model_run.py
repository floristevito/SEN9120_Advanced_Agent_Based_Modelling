import agentpy as ap
import pandas as pd
from model import EmtAgentsModel

parameters = {
    'vehicles': 10,
    'chargers': 10,
    'steps': 10
}

model = EmtAgentsModel(parameters)
results = model.run()