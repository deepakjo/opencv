# Import everything needed to edit video clips
import sys
from moviepy.editor import *
from moviepy.video.fx import time_mirror, speedx

# Load myHolidays.mp4 and select the subclip 00:00:50 - 00:00:60
clipName='/home/deepak/videos/stifte_prefinal.mp4'
clip1 = VideoFileClip(clipName)
#logo_1=ImageClip("tactification_logo.png").set_duration(clip_1.duration).resize(height=75).margin(right=40, top=10, opacity=0).set_pos(("right","top"))

                        #logo_1])

# Reduce the audio volume (volume x 0.8)
#clip = clip.volumex(0.1)

#concatVid= concatenate_videoclips([clip1], method='compose')
concatVid= concatenate_videoclips([clip1], method='compose')
# Overlay the text clip on the first video clip

# Say that you want it to appear 10s at the center of the screen
_txt_=TextClip("www.tactification.com", fontsize=40, color='white')
_txt_=_txt_.set_position('center').set_duration(2)
txt = CompositeVideoClip( [_txt_], size=concatVid.size)
final = concatenate_videoclips([txt, concatVid])

#logo=ImageClip("tactification_logo.png").set_duration(final.duration).resize(height=75).margin(right=40, top=10, opacity=0).set_pos(("right","top"))
#final=CompositeVideoClip([final, 
#                          logo]) 
# Write the result to a file (many options available !)
final.write_videofile("stifte_final.mp4")
