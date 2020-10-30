import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
import pandas as pd

client_id = 'b69091a51565464da8e8f5315482bfcd'
client_secret = 'ff3e70920cdf42d1bb135adba578aa74'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API

def get_track_ID(artist,track_name):
    searchResults = sp.search(q='artist:{} track:{}'.format(artist, track_name),limit=1)
    spotifyId =  searchResults['tracks']['items'][0]['id']
    return spotifyId

def get_track_features(id):

    meta = sp.track(id)
    features = sp.audio_features(id)
    analysis = sp.audio_analysis(id)
    # meta
    name = meta['name']
    artist = meta['album']['artists'][0]['name']
    duration_ms = meta['duration_ms']

    # features
    acousticness = features[0]['acousticness']
    danceability = features[0]['danceability']
    energy = features[0]['energy']
    instrumentalness = features[0]['instrumentalness']
    liveness = features[0]['liveness']
    loudness = features[0]['loudness']
    speechiness = features[0]['speechiness']
    tempo = features[0]['tempo']
    time_signature = features[0]['time_signature']
    key = features[0]['key']
    mode = features[0]['mode']
    valence = features[0]['valence']

    #audio anaylsis
    chorus_hit = analysis['sections'][0]['duration']*2
    sections = len(analysis['sections'])

    track = [name,artist,danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,duration_ms,time_signature,\
    chorus_hit,sections]
    return track

def get_track_audio(track_id):
    song_uri = 'spotify:track:{}'.format(track_id)

    track = sp.track(song_uri)
    name = track['name']
    audio_preview = track['preview_url']
    cover_art = track['album']['images'][0]['url']
    return name,audio_preview,cover_art

def get_encoded_artist(artist,df,x):
    for col in df.columns:
        if col == artist:
            x[0].append(1)
        else:
            x[0].append(0)
    return x

def get_predictions(track_features):

    scaler = StandardScaler()
    artist_df = pd.read_csv("model/artist_df.csv")
    filename = 'model/finalized_model.sav'
    PREDICT = pickle.load(open(filename, 'rb'))

    scaledfile = 'model/finalized_scale.sav'
    scaler = pickle.load(open(scaledfile, 'rb'))

    x = [track_features[2:]]

    x = get_encoded_artist(track_features[1],artist_df,x)

    x_scaled = scaler.transform(x)
    result = PREDICT.predict(x_scaled)
    if result[0]==1:
        return 'Hit'
    else:
        return 'Flop'
