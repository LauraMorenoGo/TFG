#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 15:41:45 2019

@author: Lau
"""

import numpy as np

def get_indices(folder = './DATOS_HISTORICOS_INDICES/'):
    """
    """
    
    #create indices dict
    indices = {'AEX':[],'CAC':[],'DAX':[],'FTSE':[],'HSI':[],'IBEX':[],'NIFTY':[],'NIKKEI':[],'SSEC':[]}
    
    #get AEX index
    aex_csv_name = folder+'AEX25/AEX.csv'
    aex_fecha = np.loadtxt(aex_csv_name,skiprows=1,usecols=(0),delimiter = ';',dtype = 'str')
    aex_cierre = np.loadtxt(aex_csv_name,skiprows=1,usecols=(1),delimiter = ';',dtype = 'float')
    
    aex = [aex_fecha,aex_cierre]
    
    #get CAC index
    cac_csv_name = folder+'CAC40/CAC40.csv'
    cac_fecha = np.loadtxt(cac_csv_name,skiprows=1,usecols=(0),delimiter = ';',dtype = 'str')
    cac_cierre = np.loadtxt(cac_csv_name,skiprows=1,usecols=(1),delimiter = ';',dtype = 'float')
    
    cac = [cac_fecha,cac_cierre]
    
    #get DAX index
    dax_csv_name = folder+'DAX/DAX.csv'
    dax_fecha = np.loadtxt(dax_csv_name,skiprows=1,usecols=(0),delimiter = ';',dtype = 'str')
    dax_cierre = np.loadtxt(dax_csv_name,skiprows=1,usecols=(1),delimiter = ';',dtype = 'float')
    
    dax = [dax_fecha,dax_cierre]
    
    #get FTSE index
    ftse_csv_name = folder+'FTSE100/FTSE100.csv'
    ftse_fecha = np.loadtxt(ftse_csv_name,skiprows=1,usecols=(0),delimiter = ';',dtype = 'str')
    ftse_cierre = np.loadtxt(ftse_csv_name,skiprows=1,usecols=(1),delimiter = ';',dtype = 'float')
    
    ftse = [ftse_fecha,ftse_cierre]
    
    #get HSI index
    hsi_csv_name = folder+'HSI/HSI.csv'
    hsi_fecha = np.loadtxt(hsi_csv_name,skiprows=1,usecols=(0),delimiter = ';',dtype = 'str')
    hsi_cierre = np.loadtxt(hsi_csv_name,skiprows=1,usecols=(1),delimiter = ';',dtype = 'float')
    
    hsi = [hsi_fecha,hsi_cierre]
    
    #get IBEX index
    ibex_csv_name = folder+'IBEX35/IBEX35.csv'
    ibex_fecha = np.loadtxt(ibex_csv_name,skiprows=1,usecols=(0),delimiter = ';',dtype = 'str')
    ibex_cierre = np.loadtxt(ibex_csv_name,skiprows=1,usecols=(1),delimiter = ';',dtype = 'float')
    
    ibex = [ibex_fecha,ibex_cierre]
    
    #get NIFTY index
    nifty_csv_name = folder+'NIFTY50/NIFTY50.csv'
    nifty_fecha = np.loadtxt(nifty_csv_name,skiprows=1,usecols=(0),delimiter = ';',dtype = 'str')
    nifty_cierre = np.loadtxt(nifty_csv_name,skiprows=1,usecols=(1),delimiter = ';',dtype = 'float')
    
    nifty = [nifty_fecha,nifty_cierre]
    
    #get NIKKEI index
    nikkei_csv_name = folder+'NIKKEI225/NIKKEI225.csv'
    nikkei_fecha = np.loadtxt(nikkei_csv_name,skiprows=1,usecols=(0),delimiter = ';',dtype = 'str')
    nikkei_cierre = np.loadtxt(nikkei_csv_name,skiprows=1,usecols=(1),delimiter = ';',dtype = 'float')
    
    nikkei = [nikkei_fecha,nikkei_cierre]
    
    #get SSEC index
    ssec_csv_name = folder+'SSEC/SSEC.csv'
    ssec_fecha = np.loadtxt(ssec_csv_name,skiprows=1,usecols=(0),delimiter = ';',dtype = 'str')
    ssec_cierre = np.loadtxt(ssec_csv_name,skiprows=1,usecols=(1),delimiter = ';',dtype = 'float')
    
    ssec = [ssec_fecha,ssec_cierre]
    
    indices['AEX'] = aex
    indices['CAC'] = cac
    indices['DAX'] = dax
    indices['FTSE'] = ftse
    indices['HSI'] = hsi
    indices['IBEX'] = ibex
    indices['NIFTY'] = nifty
    indices['NIKKEI'] = nikkei
    indices['SSEC'] = ssec
    
    return indices
