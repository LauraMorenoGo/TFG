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
    
    #reverse fechas
    fechas = fechas[-1::-1]
    
    #to reverse data
    price = price[-1::-1]
    
    t = np.arange(len(price))

    #get date position
    pos = []
    
    pos.append(np.where(fechas == '05.01.2001')[0])
    pos.append(np.where(fechas == '02.01.2004')[0])
    pos.append(np.where(fechas == '02.01.2008')[0])
    pos.append(np.where(fechas == '02.01.2014')[0])
    pos.append(np.where(fechas == '02.01.2019')[0])
    pos = np.array(pos)
    pos = pos.flatten()
    #pos = pos[-1::-1]
    
    print(pos, k)

    #plot each index
    plt.figure(1)
    plt.plot(price, label = k)
    print(k)
    plt.legend(loc='upper right')
    title('Representación índices')
    xlabel('Periodos más representativos')
    ylabel('Precios de cierre')

    #index with colours 
    plt.plot(t[:pos[0]],price[0:pos[0]])
    plt.plot(t[pos[0]:pos[1]],price[pos[0]:pos[1]])
    plt.plot(t[pos[1]:pos[2]],price[pos[1]:pos[2]])
    plt.plot(t[pos[2]:pos[3]],price[pos[2]:pos[3]])
    plt.xticks(pos,fechas[pos], size = 'small', rotation = 45)
    
    
    #segment each index
    segment1 = price[:pos[1]]
    segment2 = price[pos[1]+1:pos[2]]
    segment3 = price[pos[2]+1:pos[3]]
    segment4 = price[pos[3]+1:pos[4]]
    segment5 = price[pos[4]+1:]
    
    #xcorr for segment1
    x = segment1
    y = segment1
    xcorr1= plt.xcorr(x, y, normed=True, usevlines=True, maxlags=10, data=None)
    plt.figure(2)
    plt.plot(xcorr1, label = 'Autocorrelación segmento 1')
    plt.legend(loc='upper right')
    #plt.hold(False)

    #xcorr for segment2
    x = segment2
    y = segment2
    xcorr2= plt.xcorr(x, y, normed=True, usevlines=True, maxlags=10, data=None)
    plt.figure(3)
    plt.plot(xcorr2, label = 'Autocorrelación segmento 2')
    plt.legend(loc='upper right')

    #xcorr for segment3
    x = segment3
    y = segment3
    xcorr3= plt.xcorr(x, y, normed=True, usevlines=True, maxlags=10, data=None)
    plt.figure(4)
    plt.plot(xcorr3, label = 'Autocorrelación segmento 3')
    plt.legend(loc='upper right')
    plt.show()

    #xcorr for segment4
    x = segment4
    y = segment4
    xcorr4= plt.xcorr(x, y, normed=True, usevlines=True, maxlags=10, data=None)
    plt.figure(5)
    plt.plot(xcorr4, label = 'Autocorrelación segmento 4')
    plt.legend(loc='upper right')

    #xcorr for segment5
    x = segment5
    y = segment5
    xcorr5= plt.xcorr(x, y, normed=True, usevlines=True, maxlags=10, data=None)
    plt.figure(6)
    plt.plot(xcorr5, label = 'Autocorrelación segmento 5')
    plt.legend(loc='upper right')
    
    #hurst
    hurst1 = hurst(segment1)
    hurst2 = hurst(segment2)
    hurst3 = hurst(segment3)
    hurst4 = hurst(segment4)
    hurst5 = hurst(segment5)
    h = np.array([hurst1,hurst2,hurst3,hurst4,hurst5])
    plt.figure(7)
    plt.plot(h,'o', label = k)
    plt.legend(loc='upper right')
    title('Exponente de Hurst')

    
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