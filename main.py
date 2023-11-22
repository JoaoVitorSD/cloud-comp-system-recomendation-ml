from fpgrowth_py import fpgrowth
import pandas as pd
import json

df = pd.read_csv("/home/datasets/spotify-sample.csv")
grouped_df = df.groupby('pid')
grouped_df_dics =  grouped_df["track_uri"].apply(list).to_dict()
freqItemSet, rules = fpgrowth(grouped_df["track_uri"].apply(list).values.tolist(), minSupRatio=0.07, minConf=0.2)
# print(rules)
def filter_playlist(tracks, rules):
    if not(set(tracks).intersection(rules)):
        # print({track['track_uri']})
        return False
    return True

def find_matchs(rule):
    matchs = []
    # Adicionando a música da regra nas músicas que irão filtras as músicas compatíveis
    musics = rule[0]
    musics.update(rule[1])
    for pid, tracks in grouped_df_dics.items():
        if filter_playlist(tracks, musics):
            matchs.append(pid)
    musics = []
    for m in rule[0]:
        musics.append(m);
    return { "playlists":matchs, "tracks": musics,  "percentage": rule[2]}
    
output = []

for rule in rules:
    output.append(find_matchs(rule))


json_dict = {"recommendationList": output}

with open("/home/joaodepollo/data.json", "w") as fp:
    json.dump(json_dict, fp)