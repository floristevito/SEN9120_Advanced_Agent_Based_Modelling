import agentpy as ap
import pandas as pd
import json
from model import EtmEVsModel

# load defualt model parameters
with open('params.json') as file:
    params = json.load(file)

# remove seed and sample
del params['seed']

exp = ap.Experiment(EtmEVsModel, params, iterations=20, record=True)
results = exp.run(n_jobs=-1, verbose=10)

results.save(path='../data/seed_run')