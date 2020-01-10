## *GiveMeSome* -- bring the dub-fi-dub subculture to your slack channel!

![Legendary Rodigan selecta](https://i.imgur.com/oCsl3oC.jpg)


GiveMeSome is a slack "bot" that helps you build spotify collaborative playlist by posting notifications when songs get added.

> Get notified when a colleague adds a tune  
> Sharpen your arguments and select a better one  
> Repeat  

# Usage

> Usage: sporadub.py [OPTIONS] USER PLAYLIST_URI SLACK_CHANNEL_URL  
>
> USER is playlist owner username  
> PLAYLIST_URI is spotify playlist uri, it starts by `spotify:playlist:`  
> SLACK_CHANNEL_URL is a slack channel webhook url, it starts by `https://hooks.slack.com/services/`

# Installation

1. clone the repository
2. fill in the required infos in settings.py *[TODO]*
3. add a cron job to check playlist state at regular intervals :
    
    > \# check every minute between 8am and 7pm  
    > */1 8-19 * * 1-5 /home/ubuntu/givemesome/givemesome.py



# Screenshot

![](https://i.imgur.com/bBSYojM.jpg)

