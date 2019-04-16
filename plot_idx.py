#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 12:49:02 2019

@author: Lau
"""
from tfg_utils import *
from ts_fractals_tools import *

for k in idx.keys():
    ii = idx[k] #array index, k=noun index
    fechas = ii[0]  #date index
    i = ii[1]   #price index
    
    #get date position
    
    pos0 = np.where(fechas == '05.01.2001')
    pos1 = np.where(fechas == '02.01.2004')
    pos2 = np.where(fechas == '02.01.2008')
    pos3 = np.where(fechas == '02.01.2014')
    pos4 = np.where(fechas == '02.01.2019')
        
    print(pos0,pos1, pos2, pos3, pos4, k)

    #plot each index
    plt.figure()
    plt.plot(i)
    print(k)
    plt.legend([k])
    plt.legend(loc='upper right')
    title('Representación índices')
    xlabel('Tiempo')
    plt.xticks([pos0,pos1,pos2,pos3,pos4],[fechas[pos0], fechas[pos1], fechas[pos2], fechas[pos3], fechas[pos4]])
    ylabel('Precio de cierre')
    
    #segment each index
    segment1 = ii[:pos[1]+1]
    segment2 = ii[pos[1]+1:pos[2]+1]
    segment3 = ii[pos[2]+1:pos[3]+1]
    segment4 = ii[pos[3]+1:pos[4]+1]
    segment5 = ii[pos[4]+1:]
    
    #hurst
    hurst1 = hurst(segment1)
    hurst2 = hurst(segment2)
    hurst3 = hurst(segment3)
    hurst4 = hurst(segment4)
    hurst5 = hurst(segment5)
    
    #spectrum
    spectrum1 = spectrum1f(segment1)
    w = w1
    spectrum2 = spectrum1f(segment2)
    w2 = w1
    spectrum3 = spectrum1f(segment3)
    w3 = w1
    spectrum4 = spectrum1f(segment4)
    w4 = w1
    spectrum5 = spectrum1f(segment5)