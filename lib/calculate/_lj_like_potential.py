import numpy as np

def lj_like_potential(self, exp, eps, sigma, r, cutoff=2**(1/6)):
    r'''
        Returns Lennard-Jones-like potential at the provided r values for the
        given parameters. Provide the smaller exponent for exp, which should
        be half of the larger exponent.
    '''
    eps_arr = eps * np.ones_like(r)
    eps_arr[r>cutoff] = 0
    potential = (4 * exp * eps_arr) * ((sigma / r) ** (2*exp) -\
                                        (sigma / r) ** exp)
    return potential