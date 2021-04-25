import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv

CLIENT_ID = '{client_id}'
CLIENT_SECRET = '{client_secret}'

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp= spotipy.Spotify(client_credentials_manager=client_credentials_manager)

###
# CHANGE THIS VARIABLE TO GENRE - string
###
genre = 'country'

playlist = sp.playlist('4mijVkpSXJziPiOrK7YX4M')
#6gS3HhOiI17QNojjPuPzqc - pop
#3pDxuMpz94eDs7WFqudTbZ - edm
#7dowgSWOmvdpwNkGFMUs6e - rock
#1rLnwJimWCmjp3f0mEbnkY - r&b
#6s5MoZzR70Qef7x4bVxDO1 - rap
#3pBfUFu8MkyiCYyZe849Ks - metal
#5OzAgYmdiqJKWjGvX7cP4Q - lo-fi
#5EyFMotmvSfDAZ4hSdKrbx - jazz
#3HYK6ri0GkvRcM6GkKh0hJ - classical
#4mijVkpSXJziPiOrK7YX4M - country

music_id_list = []
track_details = []

for item in playlist['tracks']['items']:
    music_id_list.append(item['track']['id'])

def get_features(meta):
    meta_t = sp.track(meta)
    meta_af = sp.audio_features(meta)
    metadata= {'genre': genre, 'name': meta_t['name'],
               'danceability': meta_af[0]['danceability'],
               'energy': meta_af[0]['energy'], 'loudness': meta_af[0]['loudness'],
               'speechiness': meta_af[0]['speechiness'],'acousticness': meta_af[0]['acousticness'],
               'instrumentalness': meta_af[0]['instrumentalness'],'liveness': meta_af[0]['liveness'],
               'valence':meta_af[0]['valence'], 'key': meta_af[0]['key'],
               'tempo': meta_af[0]['tempo']}
    return metadata

for i in range(50):
    track_details.append(get_features(music_id_list[i]))

keys = track_details[0].keys()

with open(genre+'.csv', 'w', newline='') as output:
    dict_writer = csv.DictWriter(output, keys)
    dict_writer.writeheader()
    dict_writer.writerows(track_details)