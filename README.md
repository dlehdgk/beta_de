# Contents

This is a directory containing the COBAYA MCMC chains for the beta parameterisation of dark energy.

- noHalo chains: chains without modifying the halofit.f90 file in CAMB, ran for just planck likelihoods
- full chains: chains for modified halofit.f90 file with only planck likelihoods
- act-full chains: chains for modified halofit.f90 ran with planck, ACRDR6 lensing, desi bao, pantheon+ sne likelihoods to constrain $H_0$ and $w_a$
- large chains: chains for modified halofit.f90 with all likelihoods above but with a wider prior range $[-10,10]$
