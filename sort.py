"""
As implemented in https://github.com/abewley/sort but with some modifications
"""

# from __future__ import print_function
import numpy as np
from kalman_tracker import KalmanBoxTracker
# from correlation_tracker import CorrelationTracker
from data_association import associate_detections_to_trackers


class Sort:

  # def __init__(self,max_age=1,min_hits=3, use_dlib = False):
  def __init__(self,max_age=1,min_hits=3):

    """
    Sets key parameters for SORT
    """
    self.max_age = max_age #1
    self.min_hits = min_hits #3
    self.trackers = []
    self.frame_count = 0

    # self.use_dlib = use_dlib

  def update(self,detections,img=None):
    """
    Params:
      dets - a numpy array of detections in the format [[x,y,w,h,score],[x,y,w,h,score],...]
    Requires: this method must be called once for each frame even with empty detections.
    Returns the a similar array, where the last column is the object ID.

    NOTE: The number of objects returned may differ from the number of detections provided.
    """
    self.frame_count += 1 # self.frame_count = 0
    
    #get predicted locations from existing trackers.
    trks = np.zeros((len(self.trackers),5)) # self.trackers = [] /// np.zeros(0,5)???
    to_del = []
    ret = []
    for t,trk in enumerate(trks): # if trk = np.zeros(0,5), then there's no need to predict????
      pos = self.trackers[t].predict(img) # predicted coordinates, img NOT used in kalman tracker!!!!!
      #print(pos)
      trk[:] = [pos[0], pos[1], pos[2], pos[3], 0]
      if(np.any(np.isnan(pos))):
        to_del.append(t)
    trks = np.ma.compress_rows(np.ma.masked_invalid(trks)) # see sort_test
    for t in reversed(to_del):
      self.trackers.pop(t)
    if detections != []:
      matched, unmatched_dets, unmatched_trks = associate_detections_to_trackers(detections,trks)

      #update matched trackers with assigned detections
      for t,trk in enumerate(self.trackers):
        if(t not in unmatched_trks):
          d = matched[np.where(matched[:,1]==t)[0],0]
          trk.update(detections[d,:][0],img) ## for dlib re-intialize the trackers ?!

      #create and initialise new trackers for unmatched detections
      for i in unmatched_dets:
        # if not self.use_dlib:
        trk = KalmanBoxTracker(detections[i,:]) #create object for each bbox
        # else:
          # trk = CorrelationTracker(dets[i,:],img)
        self.trackers.append(trk) # self.trackers: a list contains 14 objects

    i = len(self.trackers)
    for trk in reversed(self.trackers): # assign ID????
        if detections == []:
          trk.update([],img)
        d = trk.get_state()  #get ith bbox coordinate (this is NOT state estimate)       # self.min_hits = 3
        if((trk.time_since_update < 1) and (trk.hit_streak >= self.min_hits or self.frame_count <= self.min_hits)): # if A and (B or C)
          ret.append(np.concatenate((d,[trk.id+1])).reshape(1,-1)) # +1 as MOT benchmark requires positive
        i -= 1
        #remove dead tracklet
        if(trk.time_since_update > self.max_age): #self.max_age = 1
          self.trackers.pop(i)
    if(len(ret)>0):
      return np.concatenate(ret) # convert list of array to np array
    return np.empty((0,5))