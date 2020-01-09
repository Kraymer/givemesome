import json
import sys
import pickle
from datetime import datetime
from dateutil import parser

import click
import requests
import spotipy
import spotipy.util as util

SESSION_FILENAME = "_session.py"
__VERSION__ = "0.0.1"


def store_infos(tz):
    """Save pickle file
    """
    with open(SESSION_FILENAME, "wb") as outfile:
        pickle.dump(datetime.now(tz), outfile)


def load_infos():
    """Load pickle file
    """
    try:
        with open(SESSION_FILENAME, "rb") as outfile:
            return pickle.load(outfile)
    except FileNotFoundError as e:
        return


def slack(slack_url, user, icon_url, msg):
    """Post message to slack
    """
    payload = {
        "username": user,
        "icon_url": icon_url,
        "as_user": False,
        "unfurl_links": False,
        "unfurl_media": False,
        "text": msg,
    }
    data = {"payload": json.dumps(payload)}
    res = requests.post(slack_url, data, verify=False)


def notify_new_tracks(slack_url, tracks):
    """Notify tracks added since last execution
    """
    last_execution = load_infos()
    for idx, track in enumerate(tracks):
        track_added_at = parser.parse(track["added_at"])
        if (not last_execution or track_added_at > last_execution):
            slack(
                slack_url,
                user=track["added_by"]["id"],
                icon_url=track["track"]["album"]["images"][0]["url"],
                msg="<{}|{} - {}>".format(
                    track["track"]["external_urls"]["spotify"],
                    track["track"]["artists"][0]["name"],
                    track["track"]["name"],
                ),
            )
    if track_added_at:
        store_infos(track_added_at.tzinfo)


def auth(username):
    """Prompt for user token
    """
    scope = "user-library-read"
    token = util.prompt_for_user_token(username, scope)
    if not token:
        print("Can't get token for {}".format(username))
        exit(1)
    return token


def strip_uri(ctx, param, value):
    """Remove 'spotify:playlist:' prefix from URI
    """
    return value.split(":")[-1]


@click.command(
    context_settings=dict(help_option_names=["-h", "--help"]),
    help=(
        "Post slack notification on slack when a song get added to a spotify playlist"
    ),
)
@click.argument("user", type=str, metavar="USER", nargs=1)
@click.argument(
    "playlist_uri", type=str, metavar="PLAYLIST_URI", nargs=1, callback=strip_uri
)
@click.argument(
    "slack_url", type=str, metavar="SLACK_CHANNEL_URL", nargs=1
)
@click.option("-v", "--verbose", count=True)
@click.version_option(__VERSION__)
def sporadub(user, playlist_uri, slack_url, verbose):
    token = auth(user)
    sp = spotipy.Spotify(auth=token)

    tracks = sp.user_playlist_tracks(user, playlist_id=playlist_uri)["items"]
    notify_new_tracks(slack_url, tracks)


if __name__ == "__main__":
    sporadub()
