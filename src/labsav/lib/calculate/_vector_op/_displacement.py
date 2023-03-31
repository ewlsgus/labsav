import numpy as np

def displacement(self):
        r'''
            Returns the N displacement vectors (NxM) from position_1 (NxM)
            to position_2 (NxM). If the box is periodic,
            provide a box dimension array L(1xM)
        '''
        if self.get_super().r1==None or self.get_super().r2==None:
            if self.get_super().r1==None and self.get_super().r2==None:
                raise Exception("At least one array should be given")
            if self.get_super().r1 is None:
                return np.zeros_like(self.get_super().r2)
            if self.get_super().r2 is None:
                return np.zeros_like(self.get_super().r1)
        else:
            if np.shape(self.get_super().r1)!=np.shape(self.get_super().r2):
                raise ValueError("Array size mismatch")
            ##### match displacement vector and box dimensions
            if np.nonzero(L)[0].size==0:
                L = np.zeros(np.shape(self.get_super().r1)[1])
            ##### calculate displacement
            displacement_vectors=self.get_super().r2-self.get_super().r1
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