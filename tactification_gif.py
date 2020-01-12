import os
import sys
import json
from moviepy.editor import *
from blur_exp import track_coords

"""
Always have a copy of image with name trial.png for playing
"""
class class_coordinate(object):
    coordinates = ()
    color       = ''
    player_number = ''

    def __init__(self, x=None, y=None, color=None, player_number=None):
        print x, y, color, player_number
        self.coordinates = (x,y)
        self.color = color
        self.player_number = player_number

    def draw_circle(self):
        centre_coordinates = (self.coordinates[0], self.coordinates[1] + 41)
        return self.coordinates, centre_coordinates

    def write_text(self):
        text_coordinates = (self.coordinates[0]-2, self.coordinates[1])
        return text_coordinates

    def draw_arrow(self, img_name):
        arrow_head="l -15,-5  +5,+5  -5,+5  +15,-5 z"

        self.cmd = "convert {:s} -colorspace RGB -fill none -stroke white -draw 'line {:d},{:d} {:d},{:d}' -colorspace sRGB {:s}".format(img_name, self.startCoords[0], self.startCoords[1], self.endCoords[0], self.endCoords[1], img_name)
#        self.cmd = "convert {:s} -size 100x60 xc: -draw 'line {:d},{:d} {:d},{:d}' -draw \"stroke blue fill skyblue path 'M 80,30 {:s}'  \" {:s}".format(img_name, self.startCoords[0], self.startCoords[1], self.endCoords[0], self.endCoords[1], arrow_head, img_name)
        print 'cmd for line', self.cmd
        os.system(self.cmd)
        self.cmd = "convert -size 100x60 {:s} -draw -stroke white -fill white path 'M {:d},{:d} {:s}' {:s}".format(img_name,  self.endCoords[0], self.endCoords[1], arrow_head, img_name)
        print 'cmd for arrow', self.cmd
        os.system(self.cmd)

class Video:
    def __init__(self, name='', t=0, numFrames=0, createImg=0):
        "time format is hr*60+min.millsecong (4534.30 for 01:15:35)"
        self.videoName = name
        self.time = t
        self.numFrames = numFrames
        self.imgDir = '/home/deepak/tactification_gif'
        self.t_start = t
        self.t_end = float(t)+numFrames*.20
        self.timeslots = [float(t)+b*.20 for b in range(numFrames)]
        print 'start:', self.t_start
        print 'end:', self.t_end
        self.clip = VideoFileClip(name)
        self.clip = self.clip.resize((1280, 720))
        self.imgpaths = []
        self.createImg = int(createImg)

    def toImage(self):
        for t in self.timeslots:
            imgpath = os.path.join(self.imgDir, '{}.png'.format(t))
            if self.createImg == 1:
                self.clip.save_frame(imgpath, t)
            self.imgpaths.append(imgpath)


"time format is 01:03:05.35"
_, videoName, start, NumFrames, createImg, idx = sys.argv
print videoName
print start 
print NumFrames 
print createImg

objVideo = Video(videoName, start, int(NumFrames), createImg=createImg)
objVideo.toImage()
objVideo.clip.close()
print '__dict__', objVideo.__dict__

if createImg == '1':
    os.system('rm -rf /home/deepak/bkp_tactification_gif/*')
    os.system('cp /home/deepak/tactification_gif/* /home/deepak/bkp_tactification_gif/') 
    exit() 

idx=int(idx)

with open('positionNumbers.json', 'r') as f:
    team_dict = json.load(f)

print 'executing:', idx
noPlayers1 = len(team_dict['positionNo1'])
noPlayers2 = len(team_dict['positionNo2'])
print videoName, start, noPlayers1, noPlayers2
print 'time:', objVideo.timeslots[idx]
team1_coord = track_coords(videoName, float(objVideo.timeslots[idx]/2), float(objVideo.timeslots[idx]/2)+.0001, noPlayers1) 
team1_player_numbers = team_dict['positionNo1'] 
team2_coord = track_coords(videoName, float(objVideo.timeslots[idx]/2), float(objVideo.timeslots[idx]/2)+.0001, noPlayers2) 
team2_player_numbers = team_dict['positionNo2'] 

print len(team1_coord), len(team1_player_numbers)
print len(team2_coord), len(team2_player_numbers)

assert(len(team1_coord) == len(team1_player_numbers))
assert(len(team2_coord) == len(team2_player_numbers))

team1_objs = []
team2_objs = []

team1_color = 'white'
team2_color = 'black'

for coords, team1_player_number in zip(team1_coord, team1_player_numbers):
    obj = class_coordinate(coords[0], coords[1], team1_color, team1_player_number)
    team1_objs.append(obj)

for coords, team2_player_number in zip(team2_coord, team2_player_numbers):
    obj = class_coordinate(coords[0], coords[1], team2_color, team2_player_number)
    team2_objs.append(obj)

print objVideo.imgpaths[idx]
team1_circle_cmd = 'convert ' + objVideo.imgpaths[idx] + ' -colorspace sRGB -fill none -stroke ' + team1_color + " "
team1_text_cmd = 'convert ' + objVideo.imgpaths[idx] + ' -pointsize 18 -fill none -stroke ' + team1_color + " "
for obj in team1_objs:
    #circle_coords = obj.draw_circle()
    #circle_cmd_str = ' -draw "circle ' + str(circle_coords[0][0]) + ',' + str(circle_coords[0][1]) + ' ' + str(circle_coords[1][0]) + ',' + str(circle_coords[1][1]) + '" ' 
    #print circle_cmd_str
    #team1_circle_cmd += circle_cmd_str

    text_coord = obj.write_text()
    text_cmd_str = ' -draw "text ' + str(text_coord[0]) + ',' + str(text_coord[1]) + " '" + str(obj.player_number) + "'" + '" ' 
    team1_text_cmd += text_cmd_str

team1_circle_cmd += objVideo.imgpaths[idx]
team1_text_cmd += objVideo.imgpaths[idx] 
os.system(team1_circle_cmd)
os.system(team1_text_cmd)

team2_circle_cmd = 'convert ' + objVideo.imgpaths[idx] + ' -colorspace sRGB -fill none -stroke ' + team2_color + " "
team2_text_cmd = 'convert ' + objVideo.imgpaths[idx] + ' -pointsize 18 -fill none -stroke ' + team2_color + " "
for obj in team2_objs:
    #circle_coords = obj.draw_circle()
    #circle_cmd_str = ' -draw "circle ' + str(circle_coords[0][0]) + ',' + str(circle_coords[0][1]) + ' ' + str(circle_coords[1][0]) + ',' + str(circle_coords[1][1]) + '" ' 
    #print circle_cmd_str
    #team2_circle_cmd += circle_cmd_str

    text_coord = obj.write_text()
    text_cmd_str = ' -draw "text ' + str(text_coord[0]) + ',' + str(text_coord[1]) + " '" + str(obj.player_number) + "'" + '" ' 
    team2_text_cmd += text_cmd_str

team2_circle_cmd += " " + objVideo.imgpaths[idx]
team2_text_cmd += " " + objVideo.imgpaths[idx]
os.system(team2_circle_cmd)
os.system(team2_text_cmd)
