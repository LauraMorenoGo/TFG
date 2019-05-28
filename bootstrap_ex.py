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


def bootstrap_index(segment1,segment2,segment3,segment4):
    """
    
    """
    np.random.seed('1947')
    
    block_size = 200 #let's use a different according to acf
    
    bs1 = MovingBlockBootstrap(block_size,segment1)
    
    hurst_segment_1 = []
    spectrum_segment_1 = []
    
    for pos_data, kwdata in bs1.bootstrap(100):
        print(pos_data)
        
        print(kwdata)
        
        boots_series = pos_data[0]
        
        #calcular hurst y spectrum para este remuestreo
        hurst_segment_1.append(hurst(boots_series))
        spectrum_segment_1.append(spectrum1f(boots_series)[-2])
      
    bs2 = MovingBlockBootstrap(block_size,segment2)
    
    hurst_segment_2 = []
    spectrum_segment_2 = []
    
    for pos_data, kwdata in bs2.bootstrap(100):
        print(pos_data)
        
        print(kwdata)
        
        boots_series = pos_data[0]
        
        #calcular hurst y spectrum para este remuestreo
        hurst_segment_2.append(hurst(boots_series))
        spectrum_segment_2.append(spectrum1f(boots_series)[-2])
    
    bs3 = MovingBlockBootstrap(block_size,segment3)
    
    hurst_segment_3 = []
    spectrum_segment_3 = []
    
    for pos_data, kwdata in bs3.bootstrap(100):
        print(pos_data)
        
        print(kwdata)
        
        boots_series = pos_data[0]
        
        #calcular hurst y spectrum para este remuestreo
        hurst_segment_3.append(hurst(boots_series))
        spectrum_segment_3.append(spectrum1f(boots_series)[-2])
        
    bs4 = MovingBlockBootstrap(block_size,segment4)
    
    hurst_segment_4 = []
    spectrum_segment_4 = []
    
    for pos_data, kwdata in bs4.bootstrap(100):
        print(pos_data)
        
        print(kwdata)
        
        boots_series = pos_data[0]
        
        #calcular hurst y spectrum para este remuestreo
        hurst_segment_4.append(hurst(boots_series))
        spectrum_segment_4.append(spectrum1f(boots_series)[-2])

    
    
    #Representación mediante histograma del análisis estadístico mediante bootstrap del exponente de Hurst
    plt.figure()
    subplot(2,2,1)
    plt.hist(hurst_segment_1, alpha = 0.5, label = ('Segmento 1'))
    subplot(2,2,2)
    plt.hist(hurst_segment_2, alpha = 0.2, label = ('Segmento 2'))
    subplot(2,2,3)
    plt.hist(hurst_segment_3, alpha = 0.3, label = ('Segmento 3'))
    subplot(2,2,4)
    plt.hist(hurst_segment_4, alpha = 0.4, label = ('Segmento 4'))
    plt.legend()
    suptitle('Bootstrap Exponente de Hurst')
    title(k)
    
    
    #Representación mediante histograma del análisis estadístico mediante bootstrap de spectrum
    plt.figure()
    plt.hist(spectrum_segment_1, alpha = 0.5, label = ('Segmento 1'))
    plt.hist(spectrum_segment_2, alpha = 0.2, label = ('Segmento 2'))
    plt.hist(spectrum_segment_3, alpha = 0.3, label = ('Segmento 3'))
    plt.hist(spectrum_segment_4, alpha = 0.4, label = ('Segmento 4'))
    plt.legend()
    suptitle('Bootstrap para Spectrum')
    title(k)
    
    
    
    #Reoresentación de la desviación del exponente de Hurst
    plt.figure()
    std = [np.std(hurst_segment_1),np.std(hurst_segment_2),np.std(hurst_segment_3),np.std(hurst_segment_4)]
    std_vector = np.array(std)
    plt.errorbar(np.arange(4),h,std_vector,marker='o')
    suptitle('Desviación para los exponentes de Hurst')
    title(k)
    
    #Reoresentación de la desviación de spectrum
    plt.figure()
    std_spect = [np.std(spectrum_segment_1),np.std(spectrum_segment_2),np.std(spectrum_segment_3),np.std(spectrum_segment_4)]
    std_vector_spect = np.array(std_spect)
    plt.errorbar(np.arange(4),spect,std_vector_spect,marker='o')
    suptitle('Desviación para Spectrum')
    title(k)
