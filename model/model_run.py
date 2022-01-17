import json
import agentpy as ap
from model import EtmEVsModel
from timeit import default_timer as timer


start = timer()
# load model parameters
with open('params2.json') as file:
    params = json.load(file)

# run simulation
model = EtmEVsModel(params)
print('starting simulation')
results = model.run()
results.variables.EtmEVsModel.plot()
results.variables.EtmEVsModel['average_battery_percentage'].plot()

end = timer()

print("---Run Completed---")
print("Completed run in {} seconds".format(end - start))
