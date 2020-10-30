from flask import Flask, request, render_template
import flask
from song_functions import get_track_ID,get_track_audio,get_track_features,get_predictions
import os

app = Flask(__name__)

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
        #get_track_features(track_id)
        name,audio_preview,cover_art = get_track_audio(track_id)
        track_features = get_track_features(track_id)
        prediction = get_predictions(track_features)
        print(audio_preview)
        return flask.render_template('song_predictor.html',prediction=prediction,name=name,artist=artist,
                                  audio=audio_preview,cover_art=cover_art)
    except:
        return flask.render_template("error.html")



## This just gets flask running
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
