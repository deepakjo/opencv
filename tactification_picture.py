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
    def __init__(self, name='', t=0):
        self.videoName = name
        self.time = t
        self.clip = VideoFileClip(name).subclip(t_start=t)
        self.clip = self.clip.resize((1280, 720))

    def toImage(self, imgName):
        self.clip.save_frame(imgName, t=self.time)

"time format is 01:03:05.35"
_, videoName, start, end = sys.argv
print videoName
print start 
print end 

objVideo = Video(videoName, start)
objVideo.toImage('post.png')
objVideo.clip.close()

with open('positionNumbers.json', 'r') as f:
    team_dict = json.load(f)

noPlayers1 = len(team_dict['positionNo1'])
noPlayers2 = len(team_dict['positionNo2'])
print videoName, start, noPlayers1, noPlayers2

os.system('cp post.png tmp_post.png')
os.system('cp post.png trial.png')

"""che"""
team1_coord = track_coords(videoName, start, end, noPlayers1) 
team1_player_numbers = team_dict['positionNo1'] 
#for i in range(len(team1_coord)):
#    print('player #', i)
#    team1_player_numbers.append(input('team1: player #'))

#team2_coord = [(123,345), (678,456)]
"""hud"""
team2_coord = track_coords(videoName, start, end, noPlayers2) 
team2_player_numbers = team_dict['positionNo2'] 
#for i in range(len(team2_coord)):
#    print('player #', i)
#    team2_player_numbers.append(input('team2: player #'))

print len(team1_coord), len(team1_player_numbers)
print len(team2_coord), len(team2_player_numbers)

assert(len(team1_coord) == len(team1_player_numbers))
assert(len(team2_coord) == len(team2_player_numbers))

team1_objs = []
team2_objs = []

team1_color = 'black'
team2_color = 'white'

for coords, team1_player_number in zip(team1_coord, team1_player_numbers):
	obj = class_coordinate(coords[0], coords[1], team1_color, team1_player_number)
	team1_objs.append(obj)

for coords, team2_player_number in zip(team2_coord, team2_player_numbers):
	obj = class_coordinate(coords[0], coords[1], team2_color, team2_player_number)
	team2_objs.append(obj)

team1_circle_cmd = 'convert trial.png -colorspace sRGB -fill none -stroke ' + team1_color + " "
team1_text_cmd = 'convert trial.png -pointsize 18 -fill none -stroke ' + team1_color + " "
for obj in team1_objs:
	#circle_coords = obj.draw_circle()
	#circle_cmd_str = ' -draw "circle ' + str(circle_coords[0][0]) + ',' + str(circle_coords[0][1]) + ' ' + str(circle_coords[1][0]) + ',' + str(circle_coords[1][1]) + '" ' 
	#print circle_cmd_str
	#team1_circle_cmd += circle_cmd_str

	text_coord = obj.write_text()
	text_cmd_str = ' -draw "text ' + str(text_coord[0]) + ',' + str(text_coord[1]) + " '" + str(obj.player_number) + "'" + '" ' 
	team1_text_cmd += text_cmd_str

team1_circle_cmd += " trial.png"
team1_text_cmd += " trial.png"
os.system(team1_circle_cmd)
os.system(team1_text_cmd)

team2_circle_cmd = 'convert trial.png -colorspace sRGB -fill none -stroke ' + team2_color + " "
team2_text_cmd = 'convert trial.png -pointsize 18 -fill none -stroke ' + team2_color + " "
for obj in team2_objs:
	#circle_coords = obj.draw_circle()
	#circle_cmd_str = ' -draw "circle ' + str(circle_coords[0][0]) + ',' + str(circle_coords[0][1]) + ' ' + str(circle_coords[1][0]) + ',' + str(circle_coords[1][1]) + '" ' 
	#print circle_cmd_str
	#team2_circle_cmd += circle_cmd_str

	text_coord = obj.write_text()
	text_cmd_str = ' -draw "text ' + str(text_coord[0]) + ',' + str(text_coord[1]) + " '" + str(obj.player_number) + "'" + '" ' 
	team2_text_cmd += text_cmd_str

team2_circle_cmd += " trial.png"
team2_text_cmd += " trial.png"
os.system(team2_circle_cmd)
os.system(team2_text_cmd)
