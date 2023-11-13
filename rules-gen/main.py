from fpgrowth_py import fpgrowth
import pandas as pd

df = pd.read_csv("test.csv")
grouped_df = df.head(10).groupby('pid')
grouped_df_dics =  grouped_df.apply(lambda group: group.to_dict(orient='records')).to_dict()
freqItemSet, rules = fpgrowth(grouped_df["track_uri"].apply(list).values.tolist(), minSupRatio=0.06, minConf=0.01)

def filter_playlist(playlist, rules):
    for rule in rules:
        if any({track['track_uri']} == rule for track in playlist):
            return False
    return True

def find_matchs (rule):
    matchs = []
    for pid, tracks in grouped_df_dics.items():
        if filter_playlist(tracks, rule):
            matchs.append(pid)
    return { "playlists":matchs, "rule": [rule[0], rule[1]], "percentage": rule[2]}
    
output = []

for rule in rules:
    output.append(find_matchs(rule))

print(output)