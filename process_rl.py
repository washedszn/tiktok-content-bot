from asyncio import subprocess
from moviepy.editor import *
from moviepy.video import *
from moviepy.video.fx.all import crop
from skimage.filters import _gaussian
import subprocess

def blur(image):
    return _gaussian.gaussian(image.astype(float), sigma=6)

def run_rl(clip_path):    
    # delete bad audio channel
    subprocess.call('ffmpeg -y -i "' + clip_path + '" -map 0:2 ./input/temprl.mp3', shell=True)

    clip = VideoFileClip(clip_path)
    audio = AudioFileClip('./input/temprl.mp3')

    facecam = crop(clip, x1=28, y1=682, x2=468, y2=924).resize(width=300).set_position((136, 94))
    gameplay = crop(clip, x1=560, y1=0, x2=1360, y2=1080).resize(width=576).set_position((0,150))
    background = crop(clip, x1=656, y1=0, x2=1264, y2=1080)
    scoreboard = crop(clip, x1=784, y1=0, x2=1138, y2=94).resize(width=576)

    # styling
    background = background.fl_image(blur);

    # layer all videos ontop of each other
    tiktok = CompositeVideoClip(size=[576, 1024], clips=[background, gameplay, scoreboard, facecam])

    # apply correct audio channel
    tiktok_final = tiktok.set_audio(audio)

    # write video to output file
    outpath = clip_path.split('\\')[1]
    tiktok_final.write_videofile('./output/tiktok-' + outpath)
    clip.close()