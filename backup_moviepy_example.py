# Import everything needed to edit video clips
import sys
from moviepy.editor import *
from moviepy.video.fx import time_mirror, speedx

# Load myHolidays.mp4 and select the subclip 00:00:50 - 00:00:60
clipName='SEVCEL.mp4'
clip = VideoFileClip(clipName).subclip(1420, 1445)
logo=ImageClip("tactification_logo.png").set_duration(clip.duration).resize(height=120).margin(right=280, top=100, opacity=0).set_pos(("right","top"))
clip_1 = VideoFileClip(clipName).subclip(1506, 1538)

clip=CompositeVideoClip([clip, clip_1, logo])

# Reduce the audio volume (volume x 0.8)
#clip = clip.volumex(0.1)
clip = clip.without_audio()
clip = speedx.speedx(clip, factor=.85)

# Say that you want it to appear 10s at the center of the screen
_txt=TextClip("www.tactification.com", fontsize=70, color='white')
_txt=_txt.set_position('center').set_duration(2)
txt = CompositeVideoClip( [_txt], size=clip.size)

final = concatenate_videoclips([txt, clip ])
# Overlay the text clip on the first video clip

# Write the result to a file (many options available !)
final.write_videofile("post33.mp4", fps=60)
