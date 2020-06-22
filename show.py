import healpy as hp
import numpy as np
import matplotlib.pyplot as plt


def moview(alm, nside = 512, fwhm = 1.0):

    map = hp.alm2map(alm, nside = nside, fwhm = fwhm*np.pi/180, verbose=False)
    hp.mollview(map, cmap = 'jet', max = 0.2, min = -0.2)
    plt.show()

def Dl(alm, lmax):

    l = np.arange(lmax+1)
    Cl = hp.alm2cl(alm, lmax = lmax)
    Dl = Cl*l*(l+1)/(2*np.pi)*10**6

    plt.plot(l, Dl, label = 'Dl')
    plt.xscale('log')

    plt.xlabel('Multipole l')
    plt.ylabel('Dl[μK^2]')

    plt.xlim([2, lmax])
    plt.ylim([0, 6000])
    plt.show()
