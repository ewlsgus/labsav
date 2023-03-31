import numpy as np

def potential(self,r,hard=False):
    r'''
        Returns Lennard-Jones-like potential at the provided r values for the
        given parameters. Provide the smaller exponent for exp, which should
        be half of the larger exponent.
    '''
    r=np.array(r)
    eps_arr=self.epsilon*np.ones_like(r)
    if hard:
        eps_arr[r>self.cutoff]=0
    potential=(4*eps_arr)*((self.sigma/r)**(self.n)-(self.sigma/r)**self.m)
    return potential
