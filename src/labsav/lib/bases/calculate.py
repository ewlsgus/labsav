import os, sys
from pathlib import Path

sys.path.append(os.path.join(Path(__file__).resolve().parents[1], 'calculate'))

class Calculate():
    r'''Define useful calculation functions'''
    def __init__(self):
        pass

    def get_super(self):
        return self
    
    import _vector_op as vector_op
    from _lj_like import lj_like
    from _virial import virial