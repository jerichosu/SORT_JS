# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 01:57:41 2022

@author: Jericho
"""
import numpy as np
import cv2

from detector import GroundTruthDetections

cap = cv2.VideoCapture('TownCentreXVID.mp4')


# while(cap.isOpened()):
#   ret, frame = cap.read()
#   # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#   cv2.imshow('frame',frame)
  
  
#   if cv2.waitKey(15) & 0xFF == ord('q'):
#     cv2.destroyAllWindows()
#     break

# cap.release()
# cv2.destroyAllWindows()

detector = GroundTruthDetections(fname= 'output/townCentreOut.top')
# detector = GroundTruthDetections()


for n_of_frames in range(0, 4501):

  detections = detector.get_detected_items(n_of_frames)
  
  ret, frame = cap.read()
  
  color = (255, 0, 0)
  thickness = 2
  
  cv2.putText(frame, str(n_of_frames), (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 2)
  
  for i in range(0, len(detections)):
      start_point = (int(detections[i,0]), int(detections[i,1]))
      end_point = (int(detections[i,2]), int(detections[i,3]))
      cv2.rectangle(frame, start_point, end_point, color, thickness)
  
  # TypeError: function takes exactly 4 arguments (2 given) happens if any coordinate is not int.
  # https://stackoverflow.com/questions/63737497/typeerror-function-takes-exactly-4-arguments-2-given-in-cv2-rectangle-functio
  
  cv2.imshow('frame',frame)
  
  if cv2.waitKey(15) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
    break

cap.release()
cv2.destroyAllWindows()