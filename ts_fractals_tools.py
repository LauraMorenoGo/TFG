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


rw = random_walk(1100)
rw = np.diff(rw) #First compute the fGn = diff(fBm)

maxPot2 = 2**np.floor(np.log2(len(rw)))
datosAux = rw[0:int(maxPot2)];
