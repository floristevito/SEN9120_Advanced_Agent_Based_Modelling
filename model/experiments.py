import agentpy as ap
import pandas as pd
import multiprocessing as mp
from model import EtmEVsModel

profiles = pd.read_csv('../data/scenarios_full_test.csv').to_dict(orient='records')

exp = ap.Experiment(EtmEVsModel, profiles, record=True)
pool = mp.Pool(mp.cpu_count() - 2)
results = exp.run(pool)
