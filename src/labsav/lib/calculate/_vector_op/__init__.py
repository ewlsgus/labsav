import os, sys
from pathlib import Path

class vector_op():
    r'''
        Initialize vector operations class. These operations are one either to a
        single array of vectors or between two arrays of vectors. Provide only
        "r1" for single array operations and provide "r1" AND "r2" for vector
        operations between the two arrays. Provide "box" ([Lx, Ly, Lz]) if
        calculation across the periodic boundary is necessary.
    '''
    def __init__(self,**kwargs):
        self.r1=kwargs.get('r1',None)
        self.r2=kwargs.get('r2',None)
        self.box=kwargs.get('box',[0,0,0])

    def get_super(self):
        return self
    
    import _vector_op._displacement as displacement
    import _vector_op._distance as distance