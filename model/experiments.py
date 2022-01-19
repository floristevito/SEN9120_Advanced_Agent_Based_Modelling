import agentpy as ap
import pandas as pd
from model import EtmEVsModel

profiles = pd.read_csv('../data/scenarios_full.csv').to_dict(orient='records')

exp = ap.Experiment(EtmEVsModel, profiles, record=True)
results = exp.run(n_jobs=-1)#, verbose=10)

results.save(path='../data/experiment_results')