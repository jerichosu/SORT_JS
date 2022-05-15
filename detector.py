"""
@author: Mahmoud I.Zidan
"""
'''
its purpose is to get the ground truth detection positions per frame.
specifically for Oxford TownCentre dataset
(http://www.robots.ox.ac.uk/~lav/Research/Projects/2009bbenfold_headpose/project.html)

Data format:
personNumber, frameNumber, headValid, bodyValid, headLeft, headTop, headRight, headBottom, bodyLeft, bodyTop, bodyRight, bodyBottom

Note: we ignore using/tracking head detection data
'''

import numpy as np

class GroundTruthDetections:
    def __init__(self, fname= 'TownCentre-groundtruth1.top.txt'):
        self.all_dets = np.loadtxt(fname, delimiter=',') #load detections
        self._frames = int(self.all_dets[:, 1].max())+1 #0 to 4500 inclusive
        self.fname = fname

    '''as in practical realtime MOT, the detector doesn't run on every single frame'''
    def _do_detection(self, detect_prob = .4): # .4 default,  = 1 means always have detections
        if self.fname == 'TownCentre-groundtruth1.top.txt':
            detect_prob = .4
        else:
            detect_prob = 1
        return int(np.random.choice(2, 1, p=[1 - detect_prob, detect_prob]))

    '''returns the detected items positions or [] if no detection'''
    def get_detected_items(self,frame):

        if self._do_detection() or frame == 0:
            if self.fname == 'TownCentre-groundtruth1.top.txt':
                return self.all_dets[self.all_dets[:, 1] == frame, 8:] # get all bboxes at frame 0
                # return self.all_dets[self.all_dets[:, 1] == frame, :1] + self.all_dets[self.all_dets[:, 1] == frame, 8:] # get all bboxes at frame 0
            else:
                # return self.all_dets[self.all_dets[:, 1] == frame, 4:] # for inference
                return np.concatenate((self.all_dets[self.all_dets[:, 1] == frame, :1], self.all_dets[self.all_dets[:, 1] == frame, 4:]),axis = 1)
        else:
            return []

    def get_total_frames(self):
        return self._frames
    
    
    
    
if __name__ == '__main__':
    
    
    detector = GroundTruthDetections(fname= 'output/townCentreOut.txt')
    for n_of_frames in range(0, 4501):
        
        detections = detector.get_detected_items(n_of_frames)
        
        break

      