#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:26:48 2019

@author: Lau
"""

#bootstrap
from arch.bootstrap import MovingBlockBootstrap
#from plot_idx import *
from tfg_utils import *
from ts_fractals_tools import *
import numpy as np
import matplotlib.pyplot as plt


def bootstrap_index(k,segment1,segment2,segment3,segment4,h,spect):
    """
    Moving block bootstrap for financial signal
    """
    np.random.seed(1947)
    
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
    suptitle('Bootstrap Exponente de Hurst')
    title(k)
    subplot(2,2,1)
    plt.hist(hurst_segment_1, alpha = 0.5, label = ('Segmento 1'))
    plt.legend()
    subplot(2,2,2)
    plt.hist(hurst_segment_2, alpha = 0.2, label = ('Segmento 2'))
    plt.legend()
    subplot(2,2,3)
    plt.hist(hurst_segment_3, alpha = 0.3, label = ('Segmento 3'))
    plt.legend()
    subplot(2,2,4)
    plt.hist(hurst_segment_4, alpha = 0.4, label = ('Segmento 4'))
    plt.legend()
      
    #Representación mediante histograma del análisis estadístico mediante bootstrap de spectrum
    plt.figure()
    suptitle('Bootstrap para Spectrum')
    title(k)
    subplot(2,2,1)
    plt.hist((np.abs(spectrum_segment_1)-1)/2, alpha = 0.5, label = ('Segmento 1'))
    plt.legend()
    subplot(2,2,2)
    plt.hist((np.abs(spectrum_segment_2)-1)/2, alpha = 0.2, label = ('Segmento 2'))
    plt.legend()
    subplot(2,2,3)
    plt.hist((np.abs(spectrum_segment_3)-1)/2, alpha = 0.3, label = ('Segmento 3'))
    plt.legend()
    subplot(2,2,4)
    plt.hist((np.abs(spectrum_segment_4)-1)/2, alpha = 0.4, label = ('Segmento 4'))
    plt.legend()
    
    #Representación mediante histograma del análisis estadístico mediante bootstrap de h estimada
    spectrum_segment_1 = np.array(spectrum_segment_1)
    spectrum_segment_2 = np.array(spectrum_segment_2)
    spectrum_segment_3 = np.array(spectrum_segment_3)
    spectrum_segment_4 = np.array(spectrum_segment_4)
    h2_est_1f = (np.abs(spectrum_segment_2)-1)/2
    h1_est_1f = (np.abs(spectrum_segment_1)-1)/2
    h3_est_1f = (np.abs(spectrum_segment_3)-1)/2
    h4_est_1f = (np.abs(spectrum_segment_4)-1)/2
    h_est_1f = np.array([h1_est_1f,h2_est_1f,h3_est_1f,h4_est_1f])
    plt.figure()
    suptitle('Bootstrap para H estimada')
    title(k)
    subplot(2,2,1)
    plt.hist(h1_est_1f, alpha = 0.5, label = ('Segmento 1'))
    plt.legend()
    subplot(2,2,2)
    plt.hist(h2_est_1f, alpha = 0.2, label = ('Segmento 2'))
    plt.legend()
    subplot(2,2,3)
    plt.hist(h3_est_1f, alpha = 0.3, label = ('Segmento 3'))
    plt.legend()
    subplot(2,2,4)
    plt.hist(h4_est_1f, alpha = 0.4, label = ('Segmento 4'))
    plt.legend()
    
    #Reoresentación de la desviación del exponente de Hurst
    plt.figure()
    std = [np.std(hurst_segment_1),np.std(hurst_segment_2),np.std(hurst_segment_3),np.std(hurst_segment_4)]
    std_vector = np.array(std)
    plt.errorbar(np.arange(4),h,std_vector,marker='o',label = 'H estimada con RS')
#    suptitle('Desviación para los Exponentes de Hurst')
    title(k)
#    xticks(np.arange(4), ('2001-2004', '2004-2008', '2008-2014', '2014-2019'), rotation= 45)
    plt.tight_layout()
    
    h_e_1f = (np.abs(spect)-1)/2
   # plt.figure()
    std_h_est = [np.std(h1_est_1f),np.std(h2_est_1f),np.std(h3_est_1f),np.std(h4_est_1f)]
    std_vector_h_est = np.array(std_h_est)
    plt.errorbar(np.arange(4),h_e_1f,std_vector_h_est,marker='^', label = 'H estimada con 1f')
 #   suptitle('Desviación para H estimada con método 1/f')
    title(k)
    xticks(np.arange(4), ('2001-2004', '2004-2008', '2008-2014', '2014-2019'), rotation= 45)
    plt.legend()
    plt.ylim((0.3,0.7))
    
    plt.hlines(0.5,0,3,colors = 'r',linestyles=':',linewidth = 0.4)
    plt.tight_layout()
    
    h_1f = (h_e_1f,h1_est_1f,h2_est_1f,h3_est_1f,h4_est_1f)
    hh = (h,hurst_segment_1,hurst_segment_2,hurst_segment_3,hurst_segment_4)
    
    return hh,h_1f
