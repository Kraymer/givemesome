## *GiveMeSome* -- bring spotify collaborative playlist selection to slack!

![Legendary Rodigan selecta](https://i.imgur.com/oCsl3oC.jpg)

> **/Give me some.../** :
>   1. **... slack** *(expr.)*: to give one a break
>   2. **... signal** *(expr.)*: to give a DJ a loud appreciation as a gesture to salute his performance

# Description

GiveMeSome is a slack "bot" that helps you build spotify collaborative playlist by posting notifications when songs get added.

Get notified when a colleague adds a tune.  
Argument and select a better one.  
Repeat.

# Installation

`pip3 install givemesome`

Then, register an app as described on https://developer.spotify.com/documentation/general/guides/app-settings/.  
Report the *Client ID*, *Client Secret* and *Redirect Url* in `~/.config/givemesome/config.yaml` like so :  

~~~
SPOTIPY_CLIENT_ID: "xxx"
SPOTIPY_CLIENT_SECRET: "xxx"
SPOTIPY_REDIRECT_URI: "xxx"
~~~

# Usage

~~~
Usage: givemesome.py [OPTIONS] USER PLAYLIST_URI SLACK_CHANNEL_URL  
  Post slack notification when a song got added to playlist since last execution
  
  USER is playlist owner username  
  PLAYLIST_URI is spotify playlist uri (starts by "spotify:playlist")  
  SLACK_CHANNEL_URL is a slack channel webhook url (starts by "https://hooks.slack.com/services/")
~~~

## Advanced usage: monitoring with cron

As its root, givemesome is a simple playlist notifier that don't have practical use.  
Read the [_"Corporate Culture: Music"_ blog post]() to see how it can achieve greater goals when the appropriate environment is setup.


# Screenshot

![](https://i.imgur.com/bBSYojM.jpg)

