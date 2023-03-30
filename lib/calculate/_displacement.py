import numpy as np

def displacement(self,p1,p2,L=[0, 0, 0]):
    r'''
        Returns the N displacement vectors (NxM) from position_1 (NxM)
        to position_2 (NxM). If the box is periodic,
        provide a box dimension array L(1xM)
    '''
    p1=np.array(p1,dtype=np.float64)
    p2=np.array(p2,dtype=np.float64)
    if np.shape(p1)!=np.shape(p2):
        raise ValueError("Array size mismatch")
    ##### match displacement vector and box dimensions
    if np.nonzero(L)[0].size==0:
        L = np.zeros(np.shape(p1)[1])
    ##### calculate displacement
    displacement_vectors=p2-p1
    ##### apply periodic boundary condition
    for i in range(len(L)):
        pbc_idx=(np.abs(displacement_vectors[:,i])>L[i]/2)
        pbc_direction=np.divide(
            displacement_vectors[:,i]*pbc_idx,
            np.abs(displacement_vectors[:,i]),
            out=np.zeros_like(displacement_vectors[:,i]),
            where=(np.abs(displacement_vectors[:, i])!=0)
        )
        displacement_vectors[:,i]=displacement_vectors[:,i]+\
            (L[i]*pbc_idx*pbc_direction*-1)
    return displacement_vectors