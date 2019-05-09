#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 12:49:02 2019

@author: Lau
"""
from tfg_utils import *
from ts_fractals_tools import *

idx = get_indices()


for k in ['AEX']:
    ii = idx[k] #array index, k=noun index
    fechas = ii[0]  #date index
    price = ii[1]   #price index
    
    #to reverse data
    price = price[-1::-1]
    
    #get date position
    pos = []
    
    pos.append(np.where(fechas == '05.01.2001')[0])
    pos.append(np.where(fechas == '02.01.2004')[0])
    pos.append(np.where(fechas == '02.01.2008')[0])
    pos.append(np.where(fechas == '02.01.2014')[0])
    pos.append(np.where(fechas == '02.01.2019')[0])
    pos = np.array(pos)
    pos = pos.flatten()
    pos = pos[-1::-1]
    
    print(pos, k)

    #plot each index
    plt.figure()
    plt.plot(price, label = k)
    print(k)
    #plt.legend(k)
    plt.legend(loc='upper right')
    title('Representación índices')
    xlabel('Tiempo')
    
    #plt.xticks([for k in pos],[fechas[for k in pos]])
    plt.xticks([pos0,pos1,pos2,pos3,pos4],[fechas[pos4], fechas[pos3], fechas[pos2], fechas[pos1], fechas[pos0]], size = 'small', rotation = 45)
    ylabel('Precio de cierre')
    
    #segment each index
    segment1 = price[:pos[1]]
    segment2 = price[pos[1]+1:pos[2]]
    segment3 = price[pos[2]+1:pos[3]]
    segment4 = price[pos[3]+1:pos[4]]
    segment5 = price[pos[4]+1:]
    
    #hurst
    hurst1 = hurst(segment1)
    hurst2 = hurst(segment2)
    hurst3 = hurst(segment3)
    hurst4 = hurst(segment4)
    hurst5 = hurst(segment5)
    
    #spectrum, get the last value for w1a
    spectrum1 = spectrum1f(segment1)
    w1 = spectrum1[-1]
    spectrum2 = spectrum1f(segment2)
    w2 = spectrum2[-1]
    spectrum3 = spectrum1f(segment3)
    w3 = spectrum3[-1]
    spectrum4 = spectrum1f(segment4)
    w4 = spectrum4[-1]
    spectrum5 = spectrum1f(segment5)
    w5 = spectrum5[-1]