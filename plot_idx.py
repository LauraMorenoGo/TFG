#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 12:49:02 2019

@author: Lau
"""


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
    