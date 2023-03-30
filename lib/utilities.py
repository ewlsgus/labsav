

# -*- coding: utf-8 -*-

import ovito.io as oi
import ovito.modifiers as om
import gsd.hoomd
import freud
import matplotlib as mpl
import matplotlib.pyplot as plt

class Calculate():
    r'''Define useful calculation functions'''
    def __init__(self):
        pass
    def displacement(self, p1, p2, L=[0, 0, 0]):
        r'''
            Returns the N displacement vectors (NxM) from position_1 (NxM)
            to position_2 (NxM). If the box is periodic,
            provide a box dimension array L(1xM)
        '''
        if np.shape(p1) != np.shape(p2):
            raise ValueError("Array size mismatch")
        ##### match displacement vector and box dimensions
        if np.nonzero(L)[0].size == 0:
            L = np.zeros(np.shape(p1)[1])
        ##### calculate displacement
        displacement_vectors = p2 - p1
        ##### apply periodic boundary condition
        for i in range(len(L)):
            pbc_idx=(np.abs(displacement_vectors[:, i]) > L[i]/2)
            pbc_direction=np.divide(
                displacement_vectors[:, i] * pbc_idx,
                np.abs(displacement_vectors[:, i]),
                out=np.zeros_like(displacement_vectors[:, i]),
                where=(np.abs(displacement_vectors[:, i]) != 0)
            )
            displacement_vectors[:, i]=displacement_vectors[:, i] + \
                (L[i] * pbc_idx * pbc_direction * -1)
        return displacement_vectors
    def distance(self, p1, p2, L=[0, 0, 0]):
        r'''
            Returns the N distance scalars (Nx1) between position_1 (NxM)
            to position_2 (NxM). If the box is periodic,
            provide a box dimension array L(1xM)
        '''
        ##### get displacement vectors
        displacement_vectors=self.displacement(p1, p2, L)
        ##### square the differences and sum
        displacement_squared=np.einsum(
            'ij, ij->i',
            displacement_vectors,
            displacement_vectors
        )
        ##### take the square root of the sums
        distance_scalars=np.sqrt(displacement_squared)
        return distance_scalars
    def lj_like_potential(self, exp, eps, sigma, r, cutoff=2**(1/6)):
        r'''
            Returns Lennard-Jones-like potential at the provided r values for the
            given parameters. Provide the smaller exponent for exp, which should
            be half of the larger exponent.
        '''
        eps_arr = eps * np.ones_like(r)
        eps_arr[r>cutoff] = 0
        potential = (4 * exp * eps_arr) * ((sigma / r) ** (2*exp) -\
                                           (sigma / r) ** exp)
        return potential
    def lj_like_force(self, exp, eps, sigma, r, cutoff=2**(1/6)):
        r'''
            Returns Lennard-Jones-like force at the provided r values for the
            given parameters. Provide the smaller exponent for exp, which should
            be half of the larger exponent.
        '''
        eps_arr = eps * np.ones_like(r)
        eps_arr[r>cutoff] = 0
        force = (4 * exp * eps_arr) * (2 * (sigma / r) ** (2*exp) -\
                                       (sigma / r) ** exp) / r
        return force
    def virial(self):
        return

class Analysis(Calculate):
    r'''Define useful analysis functions'''
    def init(self, pipeline):
        r'''Initialize the analysis class and specify the trajectory file'''
        self.pipeline=pipeline
        if not os.path.isfile(pipeline):
            raise Exception("cannot specify .gsd file")
    def init_gsd(self):
        r'''Initialize a pipeline with gsd'''
        self.pipeline_gsd=gsd.hoomd.open(self.pipeline)
        self.num_frames=self.pipeline.gsd.__len__()
    def init_ovito(self):
        r'''Initialize a pipeline with OVITO'''
        self.pipeline_ovito=oi.import_file(self.pipeline)
        self.num_frames=self.pipeline_ovito.source.num_frames

    def msd(self, mode='single_frame', write="", start=0, end=0, exclude=[], window_size=10):
        r'''
            Returns the msd values for single frame or outputs the msd values
            for multiple frames to the csv file specified in <write>. For single
            frame values, specify the reference frame in <start> and the
            frame-to-be-analyzed in <end>. To analyze only specific particle
            type(s), specify the list of particle type(s) to be excluded in 
            <exclude>. If multiple frames are analyzed, the mode can be 
            specified as "fixed" or "moving" to calculate either the MSD with 
            respect to the <start> frame up to <end> or the moving average. For the moving 
            average, the window size can be specified with <window_size>.
        '''
        if mode=="single_frame":
            frame_ref=self.pipeline.gsd[start]
            frame_analyze=self.pipeline.gsd[end]
            distance_moved = self.distance(frame_ref, frame_analyze, frame_analyze.configuration.box[0:3])
        elif mode=="fixed":
            pass
        elif mode=="moving":
            pass
        else:
            raise Exception("Incorrect mode specification")
        return
    def rdf(self):
        return
