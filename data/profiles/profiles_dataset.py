import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#df = pd.read_csv('variables_EtmEVsModel.csv')
df = pd.read_csv('../all_profiles.csv')
#fmri = sns.load_dataset("fmri")
print(df.columns)
#relplot

sns.relplot(
    data=df, kind="line",
    x="t", y="total_VTG_capacity", col = "pref_home",
    col_wrap=3
)

plt.savefig('pref_home.png')