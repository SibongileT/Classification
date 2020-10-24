from flask import Flask, request, render_template
import flask
from song_functions import get_track_ID,get_track_features,get_track_audio

app = Flask('Hit Predictor')

## Put your work here. You are also free to use static/css and templates/ if you would like
@app.route('/')
def hello_world():
    return flask.render_template('base.html')

@app.route('/hit')
def predict_hit():
    #print(flask.request.args)
    artist = flask.request.args.get("Artist")
    track = flask.request.args.get("Song")
    print(artist)
    print(track)
    try:
        track_id = get_track_ID(artist,track)
        get_track_features(track_id)
        name,audio_preview,cover_art = get_track_audio(track_id)
        print(audio_preview)
        return flask.render_template('song_predictor.html',hit = 'Hit',name=name,
                                  audio=audio_preview,cover_art=cover_art)
    except:
        return flask.render_template("error.html")



## This just gets flask running
app.run(port=5000, debug=True)
