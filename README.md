# Constrained_ILC

***Nonparametric component separation for Cosmic Microwave Background observations in harmonic space***

## Description

CILC(Constrained Internal Linear Combination) is the foreground removal method.  
You can subtract foreground and noise from observation imaps using this method　**in consideration of thermal SZ**, and get clean CMB map.  
You should note that this method is perforemed in **harmonic space**.  
For detail, see paper <a href="https://academic.oup.com/mnras/article/410/4/2481/1007333">'CMB and SZ effect separation with constrained Internal Linear Combinations'(R. Mathieu, D. Jacques et al., MNRAS, 410, 2481)

## Usage

```CILC(alms, lmax, nu).get_Cl()```:return covariance matrix  
```CILC(alms, lmax, nu).get_weight()```:return weight  
```CILC(alms, lmax, nu).do_ILC()```: return clean_alm of CMB  

If you want hint for this modules, you can use Examples.ipynb

## Requirement

- numpy(=1.18.1)
- healpy(=1.12.10)
- matplotlib(=3.2.1)

## Contributors

- Eiichiro Komatsu (MPA, KavliIPMU)

