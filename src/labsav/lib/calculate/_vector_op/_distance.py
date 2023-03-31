import numpy as np

def distance(self,p1,p2,L=[0, 0, 0]):
    r'''
        Returns the N distance scalars (Nx1) between position_1 (NxM)
        to position_2 (NxM). If the box is periodic,
        provide a box dimension array L(1xM)
    '''
    ##### get displacement vectors
    displacement_vectors=self.get_super().displacement(p1, p2, L)
    ##### square the differences and sum
    displacement_squared=np.einsum(
        'ij, ij->i',
        displacement_vectors,
        displacement_vectors
    )
    ##### take the square root of the sums
    distance_scalars=np.sqrt(displacement_squared)
    return distance_scalars