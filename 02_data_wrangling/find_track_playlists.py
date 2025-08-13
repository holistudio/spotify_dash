import pandas as pd
import os
import json
import datetime

tracks_dir = os.path.join('..','..','datasets','spotify_tracks_dataset')
tracks_file_path = os.path.join(tracks_dir,'table.pkl')
print('Loading Kaggle Track File...')
tracks_df = pd.read_pickle(tracks_file_path)
print('...done')

mp_dir = os.path.join('..','..','datasets','spotify_million_playlist_dataset','pkl')
mp_df_list = []
file_count = 0
start_time = datetime.datetime.now()
print('Loading Million Playlist Files...')
for filename in os.listdir(mp_dir):
    file_path = os.path.join(mp_dir, filename)
    if os.path.isfile(file_path):  # skip subdirectories
        df = pd.read_pickle(file_path)
        mp_df_list.append(df)
        file_count += 1
print('...done')

print('Loading matching track_ids...')
with open("match_track_ids.txt", "r") as f:
    test = f.readlines()
track_ids = [x[:-1] for x in test]
total_tracks = len(track_ids)
print('...done')

track_ids = track_ids[:10]

print('')
# Create a blank DataFrame with same columns + one extra
play_df = pd.DataFrame(columns=tracks_df.columns.tolist() + ['playlist_names'])

playlist_dict = {}
for track_id in track_ids:
    playlist_dict[track_id]=[]

start_time = datetime.datetime.now()
n = 0

for track_id in track_ids:
    # get matching row from tracks_df
    find_track = tracks_df['track_id'] == track_id
    track_row = tracks_df[find_track].iloc[0].copy()

    # add blank playlist_names
    track_row['playlist_names'] = ""

    track_uri = f'spotify:track:{track_id}'

    # search for matches in mp_df_list
    for mp_df in mp_df_list:
        filter = mp_df['track_uri'] == track_uri
        if len(mp_df[filter]) > 0:
            filter_df = mp_df[filter]
            for i, row in filter_df.iterrows():
                # print(row['playlist_name'])
                playlist_dict[track_id].append(row['playlist_name'])
    
    # fill in playlist_names
    track_row['playlist_names'] = ', '.join(playlist_dict[track_id])  # Or keep as list: test_list

    # Append to play_df
    play_df = pd.concat([play_df, pd.DataFrame([track_row])], ignore_index=True)
    
    # track progress
    n +=1

    t_elapsed = datetime.datetime.now()-start_time
    perc_complete = n*100/total_tracks
    rate = t_elapsed.total_seconds()/perc_complete
    t_remaining = (100 - perc_complete) * rate
    print(f"{track_id}, {n*100/total_tracks:.2f}%, {t_elapsed}, Est. Time Remaining={t_remaining/60:.2f} mins")


with open("playlist_names.json",'w') as f:
    json.dump(playlist_dict,f)

play_df.to_pickle('tracks_playlists_df.pkl')