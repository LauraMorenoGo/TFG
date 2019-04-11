#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 20:56:48 2019

@author: Lau
"""
from plot_idx import *
from tfg_utils import *
#segment each index

segment1 = idx[:pos[1]+1]
segment2 = idx[pos[1]+1:pos[2]+1]
segment3 = idx[pos[2]+1:pos[3]+1]
segment4 = idx[pos[3]+1:pos[4]+1]
segment5 = idx[pos[4]+1:]

print(segment1)