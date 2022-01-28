# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 06:53:26 2022

@author: Jericho
"""
import numpy as np

# trks = np.zeros((0,5))

# for t,trk in enumerate(trks):
#     print(t)
#     print(trk)
    
# trks = np.ma.compress_rows(np.ma.masked_invalid(trks))


arr1 = np.arange(0, 9, dtype=float).reshape(3, 3)
arr1[0][1] = np.NAN  # 无效值
arr1[1][0] = np.PINF  # 无效值
print('arr1:\n', '{arr1}'.format(arr1=arr1))

arr1_m = np.ma.masked_invalid(arr1)  # 把数组arr1中的无效值设置为masked(用--表示)
print('arr1_m:\n', '{arr1_m}'.format(arr1_m=arr1_m))

arr1_c = np.ma.compress_rows(arr1_m) # 把arr1中设置为mask的元素所在的行与列进行屏蔽。
print('arr1_c:\n', '{arr1_c}'.format(arr1_c=arr1_c))

