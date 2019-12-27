import sys
import pickle

import spotipy
import spotipy.util as util

from datetime import datetime
from dateutil import parser

scope = 'user-library-read'
SESSION_FILENAME = "_session.py"

def store_infos(tz):
    """Save pickle file"""
    with open(SESSION_FILENAME, 'wb') as outfile:
        pickle.dump(datetime.now(tz), outfile)

def load_infos():
    """Load pickle file"""
    try:
        with open(SESSION_FILENAME, 'rb') as outfile:
            return pickle.load(outfile)
    except FileNotFoundError as e:
        return

def notify_new_tracks(tracks):
    """Notify tracks added since last execution"""
    last_execution = load_infos()
    for track in tracks:
        track_added_at = parser.parse(track["added_at"])
        if not last_execution or  track_added_at > last_execution:
            print("{} added by {}".format(
                track["track"]["name"],
                track["added_by"]["id"],
                ))
    if track_added_at:
        store_infos(track_added_at.tzinfo)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Usage: {} username".format(sys.argv[0],))
        sys.exit()

    token = util.prompt_for_user_token(username, scope)

    if token:
        sp = spotipy.Spotify(auth=token)
        user = 'kraymer'

        tracks = sp.user_playlist_tracks(user, playlist_id="3X06jiX5M4MTat3aKJKMRL")['items']
        notify_new_tracks(tracks)

    else:
        print("Can't get token for {}".format(username))
