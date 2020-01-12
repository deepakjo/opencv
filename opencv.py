import sys
import cv2
import imutils
import argparse
from moviepy.editor import *
from moviepy.video.fx import time_mirror, speedx

#This function is to grab an image from video and save it.
def grabImage(stream, CAP_PROP_POS_MSEC=0):
    #Set the time in the video which user want to grab
    stream.set(cv2.CAP_PROP_POS_MSEC, CAP_PROP_POS_MSEC)
    success,image = stream.read()
    if success is True:
        cv2.imwrite('sample.jpg', image)
       
def readImage():
    image = cv2.imread("seeman.jpg") 
    (h, w, d) = image.shape
    print("width={}, height={}, depth={}".format(w, h, d))
    return image

def resizeImage(image):
    #resize image to 842, 1272 and 1696
    resize_640 = imutils.resize(image, width=640)
    cv2.imwrite('seeman_640.jpg', resize_640)
    cv2.imshow("Imutils Resize", resize_640)
    cv2.waitKey(0)

    resize_960 = imutils.resize(image, width=960)
    cv2.imwrite('seeman_960.jpg', resize_960)
    cv2.imshow("Imutils Resize", resize_960)
    cv2.waitKey(0)

    resize_1215 = imutils.resize(image, width=1215)
    cv2.imwrite('seeman_1215.jpg', resize_1215)
    cv2.imshow("Imutils Resize", resize_1215)
    cv2.waitKey(0)

def grabSubClip(clipName, start, end):
    clip1 = VideoFileClip(clipName).subclip(start, end)
    concatVid= concatenate_videoclips([clip1], method='compose')

    # Say that you want it to appear 10s at the center of the screen
    _txt_=TextClip("www.tactification.com", fontsize=50, color='white')
    _txt_=_txt_.set_position('center').set_duration(2)
    txt = CompositeVideoClip( [_txt_], size=concatVid.size)
    final = concatenate_videoclips([txt, concatVid])

    # Write the result to a file (many options available !)
    final.write_videofile("tactification_post_52.mp4")

#ap = argparse.ArgumentParser()
#ap.add_argument("-v", "--video", required=True,
#                help="Path to input video")
#ap.add_argument("-t", "--time", required=True,
#                help="time in millisecond")
#args = vars(ap.parse_args())
#print('args:{}'.format(args))
#
#stream = cv2.VideoCapture(args['video'])
#if stream:
#    grabImage(stream, CAP_PROP_POS_MSEC=int(args['time']))
#    image = readImage()
#    resizeImage(image)
