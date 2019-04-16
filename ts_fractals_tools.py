#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 18:38:04 2018

@author: obarquero
"""
import numpy as np
import scipy as sc
import scipy.signal as sig
from scipy import stats
import matplotlib.pyplot as plt
from random_walk import *


#compute hurst exponent using rs



def rs_calc(serie):
    """
    function RS = RScalc(rr)
    %RS compute
    N = length(rr);
    mediaDatos = sum(rr)/N; %Data mean
    X = cumsum(rr-mediaDatos);
    R = max(X) - min(X); %Range
    S = sqrt(sum((rr-mediaDatos).^2)/N); %STD
    RS = R/S; %RS 
    """
    N = len(serie)
    mediaDatos = np.mean(serie) #Data mean
    X = np.cumsum(serie-mediaDatos)
    R = np.max(X) - np.min(X) #Range
    S = np.sqrt(np.mean((serie-mediaDatos)**2)) #STD
    RS = R/S #RS
    return RS


def myregress(tC,RSave,plotFlag):
    """
    function [H, rectaReg, barrasError] = myregress(tC,RSave,plotFlag)
    x = [ones(length(tC),1) log2(tC)];
    y = log2(RSave);
    [c,cint,r,rint,stats] = regress(y,x,0.05);
    rectaReg = x*c;
    barrasError = abs(rint(:,1)-r);
    H = abs(c(2));

    %Plot
    if plotFlag
        plot(log2(tC),y,'o-')
        hold on
        plot(log2(tC),rectaReg,'r--');
    end
    """
    x = np.log2(tC)
    y = np.log2(RSave)
    m,n,r_value,p_value,stderr = stats.linregress(x,y)
    #barrasError = np.abs(rint[:,0]-r)
    H = np.abs(m)

    #Plot
    if plotFlag:
        plt.plot(np.log2(tC),y,'o-')
        plt.plot(np.log2(tC),rectaReg,'r--')
        #show()
        
    return H

#rw = random_walk(1100)



def hurst(rw):
    """
    Comentar este método!
    """
    rw = np.diff(rw) #First compute the fGn = diff(fBm)
    maxPot2 = 2**np.floor(np.log2(len(rw)))
    datosAux = rw[0:int(maxPot2)];
    tamCaja = int(maxPot2)
    numIter = 1
    RSave = []
    cajas = 1
    tC = [tamCaja]
    while(tamCaja >= 8):
        inds = []
        m = 0 #index in python begins in 0
        for l in range(cajas): #Index for this segment lenght
            indsaux = np.arange(m,m+tamCaja)
            m = m + tamCaja
            inds.append(indsaux)

    
        RSiter = []
        for ind in inds: #RS compute for this segment length
            RSaux = rs_calc(datosAux[ind])
            RSiter.append(RSaux)   
    
        RSave.append(np.mean(RSiter))
        numIter = numIter + 1
        tamCaja = int(tamCaja / 2)
        cajas = 2**(numIter-1)
        tC.append(tamCaja)

    tC = tC[0:-1]

    H = myregress(tC,RSave,0)

    return H
"""matlab code
rr = diff(rr); %First compute the fGn = diff(fBm).
maxPot2 = 2.^floor(log2(length(rr)));
datosAux = rr(1:maxPot2);
tamCaja = maxPot2;
numIter = 1;
RSave = [];
cajas = 1;
tC = [tamCaja];
while (tamCaja >= 8)
    inds = [];
    m = 1;
    for l = 1:cajas %Index for this segment lenght
        indsaux = (m : m+tamCaja-1) ;
        m = m + tamCaja;
        inds = [inds; indsaux];   
    end
    
    RSiter = [];
    for g = 1:size(inds,1) %RS compute for this segment length
        RSaux = RScalc(datosAux(inds(g,:)));
        RSiter = [RSiter; RSaux];    
    end
    RSave = [RSave;mean(RSiter)];    
    numIter = numIter + 1;
    tamCaja = tamCaja / 2;
    cajas = 2.^(numIter-1);
    tC = [tC;tamCaja];
end
tC = tC(1:end-1);


"""
#funcion calculo de exponente 1/f^alpha

def spectrum1f(signal,welch = True):
    """
    Estimate power fractal exponent using psd 1/f
    if welch == True then spectrum is estimated using Welch's periodogram. Otherwise periodogram is used.
    """
    
    #psd estimaton
    if welch:
        f_aux, pxx = sig.welch(signal)
        f = f_aux[f_aux>0]
        pxx = pxx[f_aux>0]
    else:
        sig_fft = np.fft.fft(signal)
        pxx = 1/len(signal)*np.abs(sig_fft)**2
        f_aux = np.fft.fftfreq(len(signal))
        pxx = np.fft.fftshift(pxx)
        f_aux = np.fft.fftshift(f_aux)
        f = f_aux[f_aux>0]
        pxx = pxx[f_aux>0]
        
    #power-law exponent estimation
    eps = np.finfo(float).eps
    x = np.log(f + eps)
    y = np.log(pxx)

    w1, w0, r_value, p_value, std_err = stats.linregress(x,y)
    return f, pxx, w1, w0