import sys
import spotipy
import spotipy.util as util

scope = 'user-library-read'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: {} username".format(sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    user = 'kraymer'

    last_track = sp.user_playlist_tracks(user, playlist_id="3X06jiX5M4MTat3aKJKMRL")['items'][-1]
    print("{} added by {}".format(
        last_track["track"]["name"],
        last_track["added_by"]["id"],
        ))
else:
    print("Can't get token for {}".format(username))
