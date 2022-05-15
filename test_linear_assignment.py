#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 14 18:59:38 2022

@author: 1517suj
"""

from scipy.optimize import linear_sum_assignment as linear_assignment
import numpy as np

iou_matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])

matched_indices = linear_assignment(-iou_matrix)

matched_indices_np = np.asarray(matched_indices)

my_list = [2,3,4,5,6,7,8,9]
print(my_list[:2] + my_list[6:])

lll = [[1],[2]]
ll = [[1,2],[3,4]]

l = lll+ll
