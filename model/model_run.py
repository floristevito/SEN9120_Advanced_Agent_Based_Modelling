import json
import agentpy as ap
from model import EtmEVsModel

# load model parameters
with open('params.json') as file:
    params = json.load(file)

# run simulation
model = EtmEVsModel(params)
print('starting simulation')
results = model.run()
results.variables.EtmEVsModel.plot()
results.variables.EtmEVsModel['average_battery_percentage'].plot()