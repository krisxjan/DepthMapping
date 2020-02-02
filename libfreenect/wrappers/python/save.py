import freenect
import cv2
import frame_convert2
import csv
import numpy as np

def get_depth():
    return frame_convert2.pretty_depth_cv(freenect.sync_get_depth()[0])

def get_video():
    return frame_convert2.video_cv(freenect.sync_get_video()[0])

def image_data(filename, value):
    with open(filename + '.csv', mode='w') as data_file:
        data_writer = csv.writer(data_file)
        data_writer.writerow(value)

fileName = input('Enter name of file')

k = 1
while 1:
    k+=1
    if k==10:
        depth = get_depth()
        vid = get_video()
        file = 'depth/%s.jpg' %fileName
        cv2.imwrite(file, depth)
        file2 = 'video/%s.jpg' %fileName
        cv2.imwrite(file2, vid)
        file3 = 'depth/d_%s' %fileName
        file4 = 'video/vid_%s' %fileName
        image_data(file3,depth)
        image_data(file4,vid)
        break

