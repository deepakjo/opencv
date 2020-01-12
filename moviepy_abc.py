import argparse
from moviepy.editor import *
from moviepy.video.fx import time_mirror, speedx

def grabSubClip(clipName, start, end):
    clip1 = VideoFileClip(clipName).subclip(start, end)
    concatVid= concatenate_videoclips([clip1], method='compose')

    # Say that you want it to appear 10s at the center of the screen
    _txt_=TextClip("www.tactification.com", fontsize=50, color='white')
    _txt_=_txt_.set_position('center').set_duration(2)
    txt = CompositeVideoClip( [_txt_], size=concatVid.size)
    final = concatenate_videoclips([txt, concatVid])

    # Write the result to a file (many options available !)
    final.write_videofile("sample.mp4")
