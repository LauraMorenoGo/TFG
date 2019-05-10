#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:26:48 2019

@author: Lau
"""

#bootstrap
from arch.bootstrap import MovingBlockBootstrap

block_size = 20 #let's use a different according to acf

bs = MovingBlockBootstrap(block_size,segment1)

hurst_segment_1 = []
for pos_data, kwdata in bs.bootstrap(500):
    print(pos_data)
    
    print(kwdata)
    
    boots_series = pos_data[0]
    
    #calcular hurst para este remuestreo
    hurst_segment_1.append(hurst(boots_series))