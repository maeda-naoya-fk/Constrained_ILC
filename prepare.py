import healpy as hp
import numpy as np
import os
import warnings
warnings.simplefilter('ignore')

#read imap.fits
def read_imap(lmax):

    path = os.path.dirname(__file__) + '/wmap_band_smth_imap_r9_nineyear_v5'
    os.chdir(path)

    imaps = []
    for b in ['K', 'Ka', 'Q', 'V', 'W']:

        imap_fit = 'wmap_band_smth_imap_r9_9yr_' + b + '_v5.fits'
        imap = hp.read_map(imap_fit, verbose = False)
        imaps.append(imap)

    return np.array(imaps)

#change imap to alm
def map_to_alm(imaps, lmax):

    alms = []
    for imap in imaps:

        alm = hp.map2alm(imap, lmax = lmax, iter = 10)
        alms.append(alm)

    return np.array(alms)


#Calcuate thermal SZ frequency dependence　(reference:eq.(9))
def tSZ(nu):

    h = 6.62607015e-34
    kB = 1.380649e-23
    TCMB = 2.725
    x = h*np.array(nu)*10e9 / (kB*TCMB)
    b = x*(np.exp(x)+1)/(np.exp(x)-1) - 4

    return b
