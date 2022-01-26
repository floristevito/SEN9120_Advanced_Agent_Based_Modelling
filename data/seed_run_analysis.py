import pandas as pd

# load the runs with different seeds
results = pd.read_csv('seed_run/variables_EtmEVsModel.csv')

# remove warm-up period
results.drop(results[(results['t'] < 672)].index, inplace=True)
results['t'] = results['t'] - 672

# get stats and save as LaTex table
stats = results.groupby('iteration').mean().describe()
stats.to_latex('seed_table.tex')
