# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 11:07:05 2022

@author: Jericho
"""
import numpy as np

fname = 'output/townCentreOut.top'
# all_dets = np.loadtxt(fname, delimiter=',') #load detections

all_dets = np.loadtxt(fname, delimiter=',') #load detections

frames = int(all_dets[:, 1].max())+1 #0 to 4500 inclusive



# frame = 0
# results = all_dets[all_dets[:, 1] == frame, 8:] # get all bboxes at frame 0

# kk = 0

# if kk:
#     print(1)
# else:
#     print(0)

# detect_prob = 1
# print(int(np.random.choice(2, 1, p=[1 - detect_prob, detect_prob])))