import pandas as pd

# load profile results
exp1 = pd.read_csv('./profiles/experiment1/variables_EtmEVsModel.csv')
exp2 = pd.read_csv('./profiles/experiment2/variables_EtmEVsModel.csv')
exp3 = pd.read_csv('./profiles/experiment3/variables_EtmEVsModel.csv')

# load samples
exp1_sample = pd.read_csv('./profiles/experiment1/parameters_sample.csv')
exp2_sample = pd.read_csv('./profiles/experiment2/parameters_sample.csv')
exp3_sample = pd.read_csv('./profiles/experiment3/parameters_sample.csv')

# add sample to results
exp1_t = exp1.merge(exp1_sample, on='sample_id', how='left')
exp1_t['sample_id'] = exp1_t['sample_id'] + 1000
exp2_t = exp2.merge(exp2_sample, on='sample_id', how='left')
exp2_t['sample_id'] = exp2_t['sample_id'] + 2000
exp3_t = exp3.merge(exp3_sample, on='sample_id', how='left')
exp3_t['sample_id'] = exp3_t['sample_id'] + 3000

# concat results to 1 file
results = pd.concat([exp1_t, exp2_t, exp3_t])

# remove first week (warm-up)
results.drop(results[(results['t'] < 672)].index, inplace=True)
results['t'] = results['t'] - 672

# save results
results.to_csv('all_profiles.csv', index=False)
