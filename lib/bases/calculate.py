from pathlib import Path
import os, sys
sys.path.append(os.path.join(Path(__file__).resolve().parents[1], 'calculate'))

class Calculate:
    r'''Define useful calculation functions'''
    def __init__(self):
        pass

    def get_super(self):
        return self
    
    from _displacement import displacement
    from _distance import distance
    from _lj_like_potential import lj_like_potential
    from _lj_like_force import lj_like_force
    from _virial import virial