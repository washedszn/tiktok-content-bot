from os import getcwd
from process_rl import run_rl
from process_tm import run_tm
import glob
import re
import subprocess

clips = glob.glob('./input/*.mp4')

for clip in clips:
    if (re.search('Rocket League', clip)):
        run_rl(clip_path=clip)
    if (re.search('Trackmania', clip)):
        run_tm(clip_path=clip)

    # move clip to completed directory
    subprocess.call('MOVE "' + clip.replace('/', '\\') + '" completed\\', shell=True)