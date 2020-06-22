import healpy as hp
import numpy as np
from prepare import tSZ


class CILC:

    def __init__(self, alms, lmax, nu):

        self.alms = alms
        self.lmax = lmax
        self.nu = nu
        self.len = len(self.nu)

    #calculate Cl
    def get_Cl(self):

        Cl = np.zeros((self.lmax+1, self.len, self.len))
        for i in range(self.len):
            for j in range(self.len):
                pre_Cl = hp.alm2cl(self.alms[i], self.alms[j], lmax = self.lmax)

                for l in range(self.lmax+1):
                    Cl[l][i][j] = pre_Cl[l]

        return Cl

    #calculate inverse Cl
    def get_inv_Cl(self):

        Cl = self.get_Cl()

        inv_Cl = []
        for l in range(self.lmax+1):
            inv = np.linalg.inv(Cl[l])
            inv_Cl.append(inv)

        return np.array(inv_Cl)

    #calculate weight
    def get_weight(self):

        inv_Cl = self.get_inv_Cl()

        a = np.ones((self.len, 1))
        b = tSZ(self.nu).reshape(self.len, 1)

        ainvCl = np.dot(a.T, inv_Cl)
        binvCl = np.dot(b.T, inv_Cl)

        ainvCla = np.dot(ainvCl, a)
        binvClb = np.dot(binvCl, b)
        ainvClb = np.dot(ainvCl, b)

        weight = (binvClb*ainvCl - ainvClb*binvCl) / (ainvCla*binvClb - ainvClb**2)
        return weight.reshape(self.lmax+1, self.len)

    #CILCをする
    def do_CILC(self):

        weight = self.get_weight()

        alm_clean = np.zeros(len(self.alms[0]), dtype = complex)
        for l in range(self.lmax+1):
            for m in range(l+1):
                j = hp.sphtfunc.Alm.getidx(self.lmax, l, m)

                for i in range(self.len):
                        alm_clean[j] += weight[l][i] * self.alms[i][j]

        return alm_clean
