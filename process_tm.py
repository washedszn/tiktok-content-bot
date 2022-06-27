from asyncio import subprocess
from moviepy.editor import *
from moviepy.video import *
from moviepy.video.fx.all import crop
from skimage.filters import _gaussian
import subprocess

def blur(image):
    return _gaussian.gaussian(image.astype(float), sigma=8)

def run_tm(clip_path):
    # delete bad audio channel
    subprocess.call('ffmpeg -y -i "' + clip_path + '" -map 0:2 ./input/temptm.mp3', shell=True)

    clip = VideoFileClip(clip_path)
    audio = AudioFileClip('./input/temptm.mp3')

    facecam = crop(clip, x1=36, y1=682, x2=418, y2=883).resize(width=476).set_position((50, 50))
    gameplay = crop(clip, x1=560, y1=0, x2=1360, y2=1080).resize(width=576).set_position((0,150))
    background = crop(clip, x1=656, y1=0, x2=1264, y2=1080)

    # styling
    background = background.fl_image(blur);

    # layer all videos ontop of each other
    tiktok = CompositeVideoClip(size=[576, 1024], clips=[background, gameplay, facecam])
    
    # apply correct audio channel
    tiktok_final = tiktok.set_audio(audio)

    # write video to output file
    outpath = clip_path.split('\\')[1]
    tiktok_final.write_videofile('./output/tiktok-' + outpath)
    clip.close()
