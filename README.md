# tiktok-content-bot
Automatically edits gaming clips from my Twitch stream for TikToks video format.

## How to

**Optimised for OBS replay buffer clips, my audio channels and my specific stream overlay setup. You need to change all the values so it fits your stream/audio channels**

1) Clip something from you stream
2) Add clip to the `./input` directory
3) Run the `run.py` file 
4) Wait for the program to finish... This takes a while *(I haven't implemented any GPU usage)*
5) Once finished the output videos will be in `./output` and the original clip will be moved to `./completed`

## Game support

Currently supports the following games: 
 * Rocket League
 * Trackmania
