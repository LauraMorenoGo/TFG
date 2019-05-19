#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 12:49:02 2019

@author: Lau
"""
from tfg_utils import *
from ts_fractals_tools import *

idx = get_indices()

for k in idx:
#for k in ['AEX']:
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
    plt.figure()
    plt.plot(price, label = k)
    print(k)
    plt.legend(loc='upper right')
    plt.xticks(pos,fechas[pos], size = 'small', rotation = 45)
    title('Representación índices')
    xlabel('Periodos más representativos')
    ylabel('Precios de cierre')
 
    #index with colours 
    plt.plot(t[:pos[0]],price[0:pos[0]])
    plt.plot(t[pos[0]:pos[1]],price[pos[0]:pos[1]])
    plt.plot(t[pos[1]:pos[2]],price[pos[1]:pos[2]])
    plt.plot(t[pos[2]:pos[3]],price[pos[2]:pos[3]])
    plt.plot(t[pos[3]:pos[4]],price[pos[3]:pos[4]])
    plt.xticks(pos,fechas[pos], size = 'small', rotation = 45)
    suptitle('Representación índices')
    title(k)
    xlabel('Periodos más representativos')
    ylabel('Precios de cierre')
    
    
    #segment each index
    segment1 = price[:pos[1]]
    segment2 = price[pos[1]+1:pos[2]]
    segment3 = price[pos[2]+1:pos[3]]
    segment4 = price[pos[3]+1:pos[4]]
    
    #xcorr for segment1
    x = segment1
    y = segment1
    plt.figure()
    xcorr1= plt.xcorr(x, y, normed=True, usevlines=True, maxlags=None)
    plt.plot(xcorr1[0],xcorr1[1],'-')
    title('Autocorrelación segmento 1')
    
    #xcorr for segment2
    x = segment2
    y = segment2
    plt.figure()
    xcorr2= plt.xcorr(x, y, normed=True, usevlines=True, maxlags=None)
    plt.plot(xcorr2[0],xcorr2[1],'-')
    title('Autocorrelación segmento 2')

    #xcorr for segment3
    x = segment3
    y = segment3
    plt.figure()
    xcorr3= plt.xcorr(x, y, normed=True, usevlines=True, maxlags=None)
    plt.plot(xcorr3[0],xcorr3[1],'-')
    title('Autocorrelación segmento 3')

    #PREGUNTAR SI EN LA MEMORIA, EN EL CASO DE QUERER LAS AUTOCORRELACIONES SEPARADAS, PONGO LA FIGURA QUE SALE NEGRA O EL CONTORNO SOLO
    #xcorr for segment4
    x = segment4
    y = segment4
    plt.figure()
    xcorr4= plt.xcorr(x, y, normed=True, usevlines=True, maxlags=None)
    plt.plot(xcorr4[0],xcorr4[1],'-')
    title('Autocorrelación segmento 4')

    #NO BORRAR, PREGUNTAR SI ME SIRVE O ES MEJOR POR SEPARADO
    #Representación de todas las autocorrelaciones juntas
    plt.figure()
    plt.plot(xcorr1[0],xcorr1[1],'-', label = ('Autocorrelación segmento 1'))
    plt.plot(xcorr2[0],xcorr2[1],'-', label = ('Autocorrelación segmento 2'))
    plt.plot(xcorr3[0],xcorr3[1],'-', label = ('Autocorrelación segmento 3'))
    plt.plot(xcorr4[0],xcorr4[1],'-', label = ('Autocorrelación segmento 4'))
    title(k)
    suptitle("Autocorrelación")
    plt.legend(loc='upper right')
    
    #hurst
    hurst1 = hurst(segment1)
    hurst2 = hurst(segment2)
    hurst3 = hurst(segment3)
    hurst4 = hurst(segment4)
    h = np.array([hurst1,hurst2,hurst3,hurst4])
    plt.figure()
    plt.plot(h,'o', label = k)
    plt.legend(loc='upper right')
    suptitle('Exponente de Hurst')
    title(k)
    
    #spectrum, get the last value for w1a
    spectrum1 = spectrum1f(segment1)
    w1 = spectrum1[-2]
    spectrum2 = spectrum1f(segment2)
    w2 = spectrum2[-2]
    spectrum3 = spectrum1f(segment3)
    w3 = spectrum3[-2]
    spectrum4 = spectrum1f(segment4)
    w4 = spectrum4[-2]
    spect = np.array([w1,w2,w3,w4])
    plt.figure()
    plt.plot(h,'o', label = k)
    plt.legend(loc='upper right')
    suptitle('Spectrum')
    title(k)
