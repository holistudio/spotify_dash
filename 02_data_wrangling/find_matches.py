import pandas as pd
import os
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

print('')
track_ids = []
total_rows = len(tracks_df['track_id'].unique())

print('Finding matching track_ids...')
with open("match_track_ids.txt", "a") as f:  # "a" = append mode
    start_time = datetime.datetime.now()
    for i,track_id in enumerate(tracks_df['track_id'].unique()):
        
        if (i*100/total_rows) % 10 == 0:
            print(f"{datetime.datetime.now() - start_time}: Row# {i}, Progress = {i*100/total_rows:.2f}%, Matches found = {len(track_ids)}")
        
        # get track_id
        track_id = tracks_df.iloc[i]['track_id']
        track_uri = f'spotify:track:{track_id}'

        # search for matches in mp_df_list
        for mp_df in mp_df_list:
            filter = mp_df['track_uri'] == track_uri
            if len(mp_df[filter]) > 0:
                
                track_ids.append(track_id)

                # Write a new line in a text file with the track_id
                f.write(track_id + "\n")
                print(f"{datetime.datetime.now() - start_time}: Row# {i}, Progress = {i*100/total_rows:.2f}%, Matches found = {len(track_ids)}")
                break