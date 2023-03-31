import os, sys
from pathlib import Path
import gsd.hoomd
import ovito.io as oi
import freud

sys.path.append(os.path.join(Path(__file__).resolve().parents[1], 'analysis'))

class Analyze:
    r'''Define useful analysis functions'''
    def __init__(self):
        pass

    def get_super(self):
        return self
    
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

    from _msd import msd
    from _rdf import rdf