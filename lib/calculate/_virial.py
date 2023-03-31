import numpy as np

def virial(self,r1, r2,lj_like_system, hard):
    r'''
        Returns a virial sum (scalar) by summing r (NxM) \cdot f (NxM) for the
        given interparticle distance and force arrays.
    '''
    r1=np.array(r1)
    r2=np.array(r2)
    neighbor_vec=self.get_super().displacement(r2, r1)
    f_hats=np.einsum('ij,i->ij',neighbor_vec,1/np.linalg.norm(neighbor_vec,axis=1))
    f_dot_r=np.einsum('ij,ij->i',f_hats,neighbor_vec)
    dist=np.sqrt(np.einsum('ij,ij->i',neighbor_vec,neighbor_vec))
    force_values=lj_like_system.force(dist, hard)

    virial_sum=np.einsum('i,i->',f_dot_r,force_values)

    return virial_sum