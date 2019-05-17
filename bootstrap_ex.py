#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:26:48 2019

@author: Lau
"""

#bootstrap
from arch.bootstrap import MovingBlockBootstrap
from plot_idx import *
from tfg_utils import *
import numpy as np
import matplotlib.pyplot as plt

block_size = 20 #let's use a different according to acf

bs1 = MovingBlockBootstrap(block_size,segment1)

hurst_segment_1 = []
for pos_data, kwdata in bs1.bootstrap(10):
    print(pos_data)
    
    print(kwdata)
    
    boots_series = pos_data[0]
    
    #calcular hurst para este remuestreo
    hurst_segment_1.append(hurst(boots_series))
"""   
bs2 = MovingBlockBootstrap(block_size,segment2)

hurst_segment_2 = []
for pos_data, kwdata in bs2.bootstrap(10):
    print(pos_data)
    
    print(kwdata)
    
    boots_series = pos_data[0]
    
    #calcular hurst para este remuestreo
    hurst_segment_2.append(hurst(boots_series))

bs3 = MovingBlockBootstrap(block_size,segment3)

hurst_segment_3 = []
for pos_data, kwdata in bs3.bootstrap(10):
    print(pos_data)
    
    print(kwdata)
    
    boots_series = pos_data[0]
    
    #calcular hurst para este remuestreo
    hurst_segment_3.append(hurst(boots_series))
    
bs4 = MovingBlockBootstrap(block_size,segment4)

hurst_segment_4 = []
for pos_data, kwdata in bs4.bootstrap(10):
    print(pos_data)
    
    print(kwdata)
    
    boots_series = pos_data[0]
    
    #calcular hurst para este remuestreo
    hurst_segment_4.append(hurst(boots_series))

bs5 = MovingBlockBootstrap(block_size,segment5)

hurst_segment_5 = []
for pos_data, kwdata in bs5.bootstrap(10):
    print(pos_data)
    
    print(kwdata)
    
    boots_series = pos_data[0]
    
    #calcular hurst para este remuestreo
    hurst_segment_5.append(hurst(boots_series))
"""
plt.figure()
plt.hist(hurst_segment_1)
