import agentpy as ap
import pandas as pd
from model import EtmEVsModel

profiles = pd.read_csv('../data/scenarios_full_test.csv').to_dict(orient='records')

exp = ap.Experiment(EtmEVsModel, profiles, record=True)
results = exp.run(n_jobs=-1, verbose=10)
