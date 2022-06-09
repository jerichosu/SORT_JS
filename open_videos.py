# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 01:57:41 2022

@author: Jericho
"""
import numpy as np
import cv2

from detector import GroundTruthDetections

cap = cv2.VideoCapture('TownCentreXVID.mp4')



# def vis_result(img, results):
#     for res_i, res in enumerate(results):
#         label, conf, bbox = res[:3]
#         bbox = [int(i) for i in bbox]
#         if len(res) > 3:
#             reid_feat = res[4]
#             print("reid feat dim {}".format(len(reid_feat)))

#         color = label_color[opt.label_name.index(label)]
#         # show box
#         cv2.rectangle(img, (bbox[0], bbox[1]), (bbox[2], bbox[3]), color, 2)
#         # show label and conf
#         txt = '{}:{:.2f}'.format(label, conf)
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         txt_size = cv2.getTextSize(txt, font, 0.5, 2)[0]
#         cv2.rectangle(img, (bbox[0], bbox[1] - txt_size[1] - 2), (bbox[0] + txt_size[0], bbox[1] - 2), color, -1)
#         cv2.putText(img, txt, (bbox[0], bbox[1] - 2), font, 0.5, (255, 255, 255), thickness=1, lineType=cv2.LINE_AA)
#     return img





# while(cap.isOpened()):
#   ret, frame = cap.read()
#   # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#   cv2.imshow('frame',frame)
  
  
#   if cv2.waitKey(15) & 0xFF == ord('q'):
#     cv2.destroyAllWindows()
#     break

# cap.release()
# cv2.destroyAllWindows()

detector = GroundTruthDetections(fname= 'output/townCentreOut.txt')
# detector = GroundTruthDetections()


for n_of_frames in range(0, 4501):
    
    detections = detector.get_detected_items(n_of_frames)
    ret, frame = cap.read()
  
    color = (255, 0, 0)
    thickness = 2
  
    cv2.putText(frame, str(n_of_frames), (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 2)
  
    for i in range(0, len(detections)):
        
        # start_point = (int(detections[i,0]), int(detections[i,1]))
        # end_point = (int(detections[i,2]), int(detections[i,3]))
      
        start_point = (int(detections[i,1]), int(detections[i,2]))
        end_point = (int(detections[i,3]), int(detections[i,4]))
        
        cv2.rectangle(frame, start_point, end_point, color, thickness)
      
        
        txt = '{}'.format(int(detections[i,0]))
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, str(txt), (int(detections[i,1]), int(detections[i,2]) - 2), font, 1, (0, 0, 255), thickness=2, lineType=cv2.LINE_AA)        

    # TypeError: function takes exactly 4 arguments (2 given) happens if any coordinate is not int.
    # https://stackoverflow.com/questions/63737497/typeerror-function-takes-exactly-4-arguments-2-given-in-cv2-rectangle-functio
    
    
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

cap.release()
cv2.destroyAllWindows()