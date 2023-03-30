import numpy as np

def lj_like_force(self,exp,eps,sigma,r,cutoff=2**(1/6)):
    r'''
        Returns Lennard-Jones-like force at the provided r values for the
        given parameters. Provide the smaller exponent for exp, which should
        be half of the larger exponent.
    '''
    eps_arr=eps*np.ones_like(r)
    eps_arr[r>cutoff]=0
    force = (4*exp*eps_arr)*(2*(sigma/r)**(2*exp)-(sigma/r)**exp)/r
    return force