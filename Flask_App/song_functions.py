import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

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

    # meta
    name = meta['name']
    artist = meta['album']['artists'][0]['name']
    length = meta['duration_ms']

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

    track = [track, artist, uri, danceability, acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, time_signature]
    return track

def get_track_audio(track_id):
    song_uri = 'spotify:track:{}'.format(track_id)

    track = sp.track(song_uri)
    name = track['name']
    audio_preview = track['preview_url']
    cover_art = track['album']['images'][0]['url']
    return name,audio_preview,cover_art
