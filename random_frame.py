#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 22:38:40 2021

@author: mbillah
@mail: masum@nwafu.edu.cn
"""

import os
import cv2
import numpy as np
from glob import glob

path = "/home/dragon/Lab/stdLib/stdData/stdVideos/nwafu"
folders = os.listdir(path)

idx = 1
for folder in folders:
    temp = os.path.join(path, folder)
    videos = glob(os.path.join(temp, "*.mp4"))
    
    for video in videos:
        cap = cv2.VideoCapture(video)
        frame_cnt = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        keep = np.random.randint(1, frame_cnt, 1)
        cap.set(cv2.CAP_PROP_POS_FRAMES, keep[0])
        ret, frame = cap.read()
        if ret:
            cv2.imwrite("/home/dragon/Lab/stdLib/stdOut/randFrame/"+str(idx)+".jpg", frame)
            idx += 1
        cap.release()
      

        
