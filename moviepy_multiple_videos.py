# Import everything needed to edit video clips
import sys
from moviepy.editor import *
from moviepy.video.fx import time_mirror, speedx


clipList1=[(776, 784), (1634, 1640), (1869, 1877)]
# Load myHolidays.mp4 and select the subclip 00:00:50 - 00:00:60
clipName1='/home/deepak/football_matches/CheVsMcity.mp4'

clipList2=[(875, 880), (170, 176)]
# Load myHolidays.mp4 and select the subclip 00:00:50 - 00:00:60
clipName2='/home/deepak/football_matches/CheVsMcity2.mp4'
clips = []

for item in clipList1:
    print 'item', item
    clips.append(VideoFileClip(clipName1).subclip(item[0], item[1]))

for item in clipList2:
    print 'item', item
    clips.append(VideoFileClip(clipName2).subclip(item[0], item[1]))

print 'clips', clips
print 'type(clips)', type(clips)
finalclip=concatenate_videoclips(clips)

# Overlay the text clip on the first video clip

# Write the result to a file (many options available !)
finalclip.write_videofile("ChleseaVsMCity.mp4", fps=60)
clip = VideoFileClip("ChleseaVsMCity.mp4")
logo=ImageClip("tactification_logo.png").set_duration(clip.duration).resize(height=75).margin(right=40, top=10, opacity=0).set_pos(("right","top"))

clip=CompositeVideoClip([clip, 
                        #clip_1, 
                        logo]) 
                        #logo_1])
_txt=TextClip("www.tactification.com", fontsize=70, color='white')
_txt=_txt.set_position('center').set_duration(2)
txt = CompositeVideoClip( [_txt], size=clip.size)

final = concatenate_videoclips([txt, clip ])
# Overlay the text clip on the first video clip

final.write_videofile("ChelseaVsManCity.mp4", fps=60)
