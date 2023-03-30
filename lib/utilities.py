

# -*- coding: utf-8 -*-

import ovito.io as oi
import ovito.modifiers as om
import gsd.hoomd
import freud
import matplotlib as mpl
import matplotlib.pyplot as plt

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
