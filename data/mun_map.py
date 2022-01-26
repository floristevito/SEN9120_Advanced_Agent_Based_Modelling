import pandas as pd

# local path, file too big
results = pd.read_csv('/home/tevito/Documents/EPA/Year2/Q2/SEN9120/vm_results/vm1_results/experiment1_results/EtmEVsModel_1/variables_Municipality.csv', \
    nrows=1000000)

# take one run
results = results[results['sample_id'] == 0]

# remove first week (warm-up)
results.drop(results[(results['t'] < 672)].index, inplace=True)
results['t'] = results['t'] - 672

# calculate per mun
results = results.groupby('obj_id').mean()

# save
results.to_csv('mun_mean.csv')