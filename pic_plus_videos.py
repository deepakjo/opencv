# Import everything needed to edit video clips
import sys
from moviepy.editor import *
from moviepy.video.fx import time_mirror, speedx

img = ['/home/deepak/spainTrip/peniscola_selfie.jpg', '/home/deepak/spainTrip/peniscola_selfie.jpg', '/home/deepak/spainTrip/peniscola_selfie.jpg']

clips = [ImageClip(m).set_duration(1) for m in img]
imgclip = concatenate_videoclips(clips, method="compose")
imgclip.write_videofile("imgVideo.mp4", fps=24)
img_clip = VideoFileClip("imgVideo.mp4")

# Load myHolidays.mp4 and select the subclip 00:00:50 - 00:00:60
clipName='/home/deepak/spainTrip/sijo_wants_to_live_more.mp4'
clip1 = VideoFileClip(clipName).subclip(1850, 1860)
#clipName='/home/deepak/football_matches/YTFraVsArg.mkv'
#clip2 = VideoFileClip(clipName).subclip(212, 237)
#logo_1=ImageClip("tactification_logo.png").set_duration(clip_1.duration).resize(height=75).margin(right=40, top=10, opacity=0).set_pos(("right","top"))

                        #logo_1])

# Reduce the audio volume (volume x 0.8)
#clip = clip.volumex(0.1)

concatVid= concatenate_videoclips([img_clip, clip1], method='compose')
# Overlay the text clip on the first video clip

# Say that you want it to appear 10s at the center of the screen
_txt_=TextClip("Hello", fontsize=50, color='white')
_txt_=_txt_.set_position('center').set_duration(2)
txt = CompositeVideoClip( [_txt_], size=concatVid.size)
final = concatenate_videoclips([txt, concatVid])

#logo=ImageClip("tactification_logo.png").set_duration(final.duration).resize(height=75).margin(right=40, top=10, opacity=0).set_pos(("right","top"))
#final=CompositeVideoClip([final, 
#                          logo]) 
# Write the result to a file (many options available !)
final.write_videofile("peniscola.mp4")

clipName='peniscola.mp4'
clip = VideoFileClip(clipName)
_txt_=TextClip("Peniscola(Spain) April 30", fontsize=50, color='white')
_txt_=_txt_.set_position('center').set_duration(2)
txt = CompositeVideoClip( [_txt_], size=clip.size)

final = concatenate_videoclips([txt, clip])

final.write_videofile("Peniscola_1.mp4")
