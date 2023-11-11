from fpgrowth_py import fpgrowth
import pandas as pd


df = pd.read_csv("2023_spotify_ds1.csv")
grouped_df = df.groupby('pid')['track_uri'].apply(list).values.tolist()
freqItemSet, rules = fpgrowth(grouped_df, minSupRatio=0.06, minConf=0.5)
print(rules)  


# TODO store rules