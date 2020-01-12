import os
import sys
from moviepy.editor import *

def extract_frames(movie, times, imgdir):
    clip = VideoFileClip(movie)
    time = times[0]
    end_time = times[1]
    while time < end_time:
        imgpath = os.path.join(imgdir, '{}.png'.format(time))
        clip.save_frame(imgpath, time)
        time = time + .01

movie = sys.argv[1] 
imgdir = '/home/deepak/tactification_gif'
times = [756.32, 760.2]

extract_frames(movie, times, imgdir)
