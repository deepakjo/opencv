# Import everything needed to edit video clips
import sys
import os, os.path

# simple version for working with CWD
from moviepy.editor import *
from moviepy.video.fx import time_mirror, speedx

file_list='/home/deepak/tactification_gif'
numFiles = len([name for name in os.listdir(file_list)])

durations = numFiles * [.1]
clip = ImageSequenceClip(sequence=file_list, durations=durations)
clip.write_gif('post_1.gif', fps=2.0)
