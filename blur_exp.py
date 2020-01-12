from moviepy.editor import *
from moviepy.video.tools.tracking import manual_tracking

#time format: 01:03:05.35
def track_coords(videoName, start, end, noObj):
    print 'start and end', start, end
    clip = VideoFileClip(videoName).subclip(start, start)
    clip = clip.resize((1280, 720))
    trajectories_team = manual_tracking(clip, t1=start, t2=end, \
                                        fps=1, nobjects=noObj,
                                        savefile="track_t1.txt")

    a=list()
    b=list()
    for coords in trajectories_team:
        a.append(coords.xx.tolist()[0])
        b.append(coords.yy.tolist()[0])
        print a, b

    team_coords=zip(a,b)
    print 'team coordinates', team_coords
    clip.close()
    return team_coords
