import os, sys
from pathlib import Path

class lj_like():
    r'''Initialize a LJ-like system for potential and force calculation'''
    def __init__(self,epsilon=1,n=12,m=6,sigma=1.0,cutoff=2**(1/6)*2.5):
        self.epsilon=epsilon
        self.n=n
        self.m=m
        self.sigma=sigma
        self.cutoff=cutoff

    def get_super(self):
        return self
    
    import _lj_like._potential as potential
    import _lj_like._force as force